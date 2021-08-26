# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 14:48:51 2021

@author: BEL
"""

import xml.etree.ElementTree as ET
import sys,os
#images path
#img_path = r'C:\Users\BEL\Documents\GKN\Keras-tar\Borderless_table_detection\borderless_tbls_detection-main\images\processed\splitted\train_set'
img_path = input("Enter images path \n")
#annotations path
annot_path=input("Enter annotations path\nh")
#annot_path = r'C:\Users\BEL\Documents\GKN\Keras-tar\Borderless_table_detection\borderless_tbls_detection-main\images\processed\splitted\train_set'

#'/path/to/directory'
for filename in os.listdir(annot_path):
    if filename.endswith('.xml'):
        fullname=os.path.join(annot_path,filename) #full path of xml file
        img=filename.replace('.xml','')
        image_name = img+'.jpg' 
        f=os.path.join(img_path,image_name) #replacing as img_path/filename.jpg 
        mytree = ET.parse(fullname)
        myroot = mytree.getroot()
        for path in myroot.iter('path'):
            path.text = f
        mytree.write(fullname)#writing it to same file 
