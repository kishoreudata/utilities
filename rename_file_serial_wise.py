# -*- coding: utf-8 -*-
"""
Created on Fri Feb 25 13:06:31 2022

@author: Elite-Systems
"""

# Pythono3 code to rename multiple
# files in a directory or folder

# importing os module
import os


# Function to rename multiple files
def main():
    #folder = r"E:\kishore\BEL_AI_TRAINER\test_images\knife"
    folder = input("enter input images path\n")
    for count, filename in enumerate(os.listdir(folder)):
        if filename.endswith('.jpg'):
            dst = f"IR_aircraft_{str(count)}.png"
            src = f"{folder}/{filename}"  # foldername/filename, if .py file is outside folder
            dst = f"{folder}/{dst}"
            # rename all the files
            os.rename(src, dst)
# Driver Code
if __name__ == '__main__':
    # Calling main() function
    main()