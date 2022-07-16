#!/usr/bin/env python
# coding: utf-8

# # Object Detection Demo
# Welcome to the object detection inference walkthrough!  This notebook will walk you step by step through the process of using a pre-trained model to detect objects in an image. Make sure to follow the [installation instructions](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/installation.md) before you start.

# In[1]:

'''
pwd


# In[2]:


cd ..


# In[4]:


get_ipython().run_line_magic('set_env', 'PYTHONPATH=/Projects/Pothole/MaskRCNN/models/research:/Projects/Pothole/MaskRCNN/models/research/slim')
'''

# # Imports

# In[7]:


import numpy as np
import os
import six.moves.urllib as urllib
import sys
import tarfile
import tensorflow as tf
import zipfile

from collections import defaultdict
from io import StringIO
from matplotlib import pyplot as plt
from PIL import Image

# This is needed since the notebook is stored in the object_detection folder.
sys.path.append("..")
from object_detection.utils import ops as utils_ops
from object_detection.utils import label_map_util
from object_detection.utils import visualization_utils as vis_util


# This is needed to display the images.
from IPython import get_ipython
#get_ipython().run_line_magic('matplotlib', 'inline')
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

# ## Env setup

# In[8]:


# This is needed to display the images.
#get_ipython().run_line_magic('matplotlib', 'inline')


# # Model preparation 

# ## Variables
# 
# Any model exported using the `export_inference_graph.py` tool can be loaded here simply by changing `PATH_TO_FROZEN_GRAPH` to point to a new .pb file.  
# 
# By default we use an "SSD with Mobilenet" model here. See the [detection model zoo](https://github.com/tensorflow/models/blob/master/research/object_detection/g3doc/detection_model_zoo.md) for a list of other models that can be run out-of-the-box with varying speeds and accuracies.

# In[17]:

current_path='E:/kishore/my_projects/obj_mrcnn/models/research/object_detection'

#PATH_TO_FROZEN_GRAPH = 'D:/Projects/Pothole/MaskRCNN/models/research/object_detection/inference_graph/frozen_inference_graph.pb'
PATH_TO_FROZEN_GRAPH = current_path+'/inference_graph/frozen_inference_graph.pb'
PATH_TO_LABELS = current_path+'/training/labelmap.pbtxt'


# ## Download Model

# In[ ]:
'''

opener = urllib.request.URLopener()
opener.retrieve(DOWNLOAD_BASE + MODEL_FILE, MODEL_FILE)
tar_file = tarfile.open(MODEL_FILE)
for file in tar_file.getmembers():
  file_name = os.path.basename(file.name)
  if 'frozen_inference_graph.pb' in file_name:
    tar_file.extract(file, os.getcwd())

'''
# ## Load a (frozen) Tensorflow model into memory.

# In[18]:


detection_graph = tf.Graph()
with detection_graph.as_default():
    od_graph_def = tf.GraphDef()
    with tf.gfile.GFile(PATH_TO_FROZEN_GRAPH, 'rb') as fid:
        serialized_graph = fid.read()
        od_graph_def.ParseFromString(serialized_graph)
        tf.import_graph_def(od_graph_def, name='')


# ## Loading label map
# Label maps map indices to category names, so that when our convolution network predicts `5`, we know that this corresponds to `airplane`.  Here we use internal utility functions, but anything that returns a dictionary mapping integers to appropriate string labels would be fine

# In[19]:


category_index = label_map_util.create_category_index_from_labelmap(PATH_TO_LABELS, use_display_name=True)
print(category_index)
# ## Helper code

# In[20]:


def load_image_into_numpy_array(image):
    (im_width, im_height) = image.size
    return np.array(image.getdata()).reshape(
      (im_height, im_width, 3)).astype(np.uint8)


# # Detection

# In[30]:


# For the sake of simplicity we will use only 1 image:
# If you want to test the code with your images, just add path to the images to the TEST_IMAGE_PATHS.
#PATH_TO_TEST_IMAGES_DIR = 'D:/Projects/Pothole/MaskRCNN/models/research/object_detection/test_images'

PATH_TO_TEST_IMAGES_DIR = 'E:/kishore/my_projects/obj_mrcnn/models/research/object_detection/test_images'

#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.jpg'.format(i)) for i in range(1, 2) ]
#TEST_IMAGE_PATHS = [ os.path.join(PATH_TO_TEST_IMAGES_DIR, 'image{}.bmp'.format(i)) for i in range(1, 2) ]
#TEST_IMAGE_PATHS = [ r'E:\kishore\my_projects\obj_mrcnn\models\research\object_detection\images\test\' ]
#TEST_IMAGE_PATHS = [ r'E:\kishore\my_projects\obj_mrcnn\models\research\object_detection\images\test\10426.bmp' ]
#TEST_IMAGE_PATHS = [r'C:\Users\SUPERMICR\Desktop\DATASET\other\gunknife_google\images41.PNG']

#TEST_IMAGE_PATHS =  r'C:\Users\SUPERMICR\Desktop\test_imgs'

# Size, in inches, of the output images.
IMAGE_SIZE = (12, 8)


# In[31]:


def run_inference_for_single_image(image, graph):
  with graph.as_default():
    with tf.Session() as sess:
      # Get handles to input and output tensors
      ops = tf.get_default_graph().get_operations()
      all_tensor_names = {output.name for op in ops for output in op.outputs}
      tensor_dict = {}
      for key in [
          'num_detections', 'detection_boxes', 'detection_scores',
          'detection_classes', 'detection_masks'
      ]:
        tensor_name = key + ':0'
        if tensor_name in all_tensor_names:
          tensor_dict[key] = tf.get_default_graph().get_tensor_by_name(
              tensor_name)
      if 'detection_masks' in tensor_dict:
        # The following processing is only for single image
        detection_boxes = tf.squeeze(tensor_dict['detection_boxes'], [0])
        detection_masks = tf.squeeze(tensor_dict['detection_masks'], [0])
        # Reframe is required to translate mask from box coordinates to image coordinates and fit the image size.
        real_num_detection = tf.cast(tensor_dict['num_detections'][0], tf.int32)
        detection_boxes = tf.slice(detection_boxes, [0, 0], [real_num_detection, -1])
        detection_masks = tf.slice(detection_masks, [0, 0, 0], [real_num_detection, -1, -1])
        detection_masks_reframed = utils_ops.reframe_box_masks_to_image_masks(
            detection_masks, detection_boxes, image.shape[0], image.shape[1])
        detection_masks_reframed = tf.cast(
            tf.greater(detection_masks_reframed, 0.5), tf.uint8)
        # Follow the convention by adding back the batch dimension
        tensor_dict['detection_masks'] = tf.expand_dims(
            detection_masks_reframed, 0)
      image_tensor = tf.get_default_graph().get_tensor_by_name('image_tensor:0')

      # Run inference
      output_dict = sess.run(tensor_dict,
                             feed_dict={image_tensor: np.expand_dims(image, 0)})

      # all outputs are float32 numpy arrays, so convert types as appropriate
      output_dict['num_detections'] = int(output_dict['num_detections'][0])
      output_dict['detection_classes'] = output_dict[
          'detection_classes'][0].astype(np.uint8)
      output_dict['detection_boxes'] = output_dict['detection_boxes'][0]
      output_dict['detection_scores'] = output_dict['detection_scores'][0]
      if 'detection_masks' in output_dict:
        output_dict['detection_masks'] = output_dict['detection_masks'][0]
  return output_dict


# In[32]:


#for image_path in TEST_IMAGE_PATHS:
# do not give r'C:\desktop\' type path i.e., don't give path with backward slashes
p = './test_images'
i=0
for filename in os.listdir(p):
    image_path = p + '/' + filename
    #print(image_path)
    img_name= filename
    file_extension = os.path.splitext(filename)[1]
    if(file_extension!='.png' and file_extension!='.jpg'):continue
    image = Image.open(image_path)
    #print(image_path)
    # the array based representation of the image will be used later in order to prepare the
    # result image with boxes and labels on it.
    image_np = load_image_into_numpy_array(image)
    # Expand dimensions since the model expects images to have shape: [1, None, None, 3]
    image_np_expanded = np.expand_dims(image_np, axis=0)
    # Actual detection.
    output_dict = run_inference_for_single_image(image_np, detection_graph)
    # Visualization of the results of a detection.
    #vis_util.visualize_boxes_and_labels_on_image_array(
    #print('******POSSIBLE SCENES ARE: ')
    predicted_image=vis_util.visualize_boxes_and_labels_on_image_array(
      image_np,
      output_dict['detection_boxes'],
      output_dict['detection_classes'],
      output_dict['detection_scores'],
      category_index,
      instance_masks=output_dict.get('detection_masks'),
      use_normalized_coordinates=True,
      line_thickness=8)
    print(predicted_image[1])
    print(output_dict['detection_boxes'])
    fig = plt.figure(figsize=IMAGE_SIZE)
    ax = fig.gca()
    ax.grid(False)
    plt.imshow(image_np)
    img = Image.fromarray(image_np, 'RGB')
    # img.save('output.png')
    path = "./output/"
    f = path + "output_" + str(i) + ".png"
    img.save(f)
    i=i+1


#for i in output_dict['detection_classes']:
#   mytext= category_index.get(i).get('name')
if(output_dict['detection_classes'][0]==1):


    #categories = label_map_util.create_categories_from_labelmap(PATH_TO_LABELS)
    #classes_dict = categories[0]
    #mytext = classes_dict.get('name') + "detected"
    #print(classes_dict.get('name') )
    class_name=category_index.get(i).get('name')
    mytext = class_name + "detected"
    # Import the required module for text
    # to speech conversion
    from gtts import gTTS
    # The text that you want to convert to audio
    #mytext = 'Welcome to geeksforgeeks!'

    # Language in which you want to convert
    language = 'en'

    # Passing the text and language to the engine,
    # here we have marked slow=False. Which tells
    # the module that the converted audio should
    # have a high speed
    myobj = gTTS(text=mytext, lang=language, slow=False)

    # Saving the converted audio in a mp3 file named
    # welcome
    myobj.save("welcome.mp3")

    # Playing the converted file
    #os.system("mpg321 welcome.mp3")




