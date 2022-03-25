# Program To Read video
# and Extract Frames
import cv2
import os

# Function to extract frames
def FrameCapture(path):
	
	# Path to video file
	vidObj = cv2.VideoCapture(path)

	# Used as counter variable
	count = 0

	# checks whether frames were extracted
	success = 1   
	#path to save file
	#savepath=input("Enter folder path to save frames  ")
	while success:

		# vidObj object calls read
		# function extract frames
		success, image = vidObj.read()
		# Saves the frames with frame-count
		fname="frame%d.jpg"+str(count)
		#cv2.imwrite(fname, image)
		cv2.imwrite("frame%d.jpg" % count, image)
		#cv2.imwrite(os.path.join(savepath ,fname), image)

		count += 1

# Driver Code
if __name__ == '__main__':

	# Calling the function
	#FrameCapture("C:\\Users\\Admin\\PycharmProjects\\project_1\\openCV.mp4")
	path=input("enter path of video  ")
	FrameCapture(path)
    
