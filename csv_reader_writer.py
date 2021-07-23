# -*- coding: utf-8 -*-
"""
Created on Fri Jul 23 12:58:34 2021

@author: Gagan Nigam
"""

# importing csv module
import csv
# csv file name
filename = r"C:\Users\Gagan Nigam\Documents\d_drive\KerasExample\Kangaroo\DroneDetection\new_database\input.csv"
  
# initializing the titles and data list
data=[]

# reading csv file
with open(filename, 'r') as csvfile:
# creating a csv reader object
    csvreader = csv.reader(csvfile)
    j=0
    for i in csvreader:
        data.append(i)
        file_name=data[j][4]
        new_file_name = file_name.replace(".JPEG","")#removing .jpeg name 
        final = new_file_name+'.csv'
        rows=data[j][0:4]
        with open(final, 'w') as f:
            # creating a csv writer object
            writ = csv.writer(f)
            writ.writerow(rows)
            
        j+=1
        tsvfile = final.replace('.csv','.tsv')
            
    
    