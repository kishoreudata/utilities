import xml.etree.ElementTree as ET
import sys,os
#images path
#img_path = r'C:\Users\BEL\Documents\GKN\Keras-tar\Borderless_table_detection\borderless_tbls_detection-main\images\processed\splitted\train_set'
img_path = input("Enter images path \n")
#annotations path
annot_path=input("Enter annotations path\n")
#annot_path = r'C:\Users\BEL\Documents\GKN\Keras-tar\Borderless_table_detection\borderless_tbls_detection-main\images\processed\splitted\train_set'

#'/path/to/directory'
for filename in os.listdir(annot_path):
    if filename.endswith('.xml'):
        fullname=os.path.join(annot_path,filename) #full path of xml file
        img=filename.replace('.xml','')
        image_name = img+'.png' 
        f=os.path.join(img_path,image_name) #replacing as img_path/filename.jpg 
        mytree = ET.parse(fullname)
        myroot = mytree.getroot()
        for fname in myroot.iter('filename'):
            fname.text=image_name
        for path in myroot.iter('path'):
            path.text = f
        mytree.write(fullname)#writing it to same file
        flag = 1
if(flag==1): print("Done")