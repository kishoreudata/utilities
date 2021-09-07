'''
import pandas as pd
df=pd.read_json(r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.json')
df.to_csv(r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.csv')
#df.to_excel("")
'''

'''
import json
import csv

#with open('G:\Akhil\jsonoutput.json') as json_file:
with open('G:/d_drive/KerasExample/Knife_Dataset/data/training/train.json') as json_file:
    jsondata = json.load(json_file)

#data_file = open('G:\Akhil\jsonoutput.csv', 'w', newline='')
data_file = open('G:/d_drive/KerasExample/Knife_Dataset/data/training/train.csv', 'w', newline='')
csv_writer = csv.writer(data_file)

count = 0
for data in jsondata:
    if count == 0:
        header = data.keys()
        csv_writer.writerow(header)
        count += 1
    csv_writer.writerow(data.values())

data_file.close()
'''
'''
import csv, json, sys

#input = open(sys.argv[1])
input = open(r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.json')
data = json.load(input)
input.close()

output = csv.writer(sys.stdout)

output.writerow(data[0].keys())  # header row

for row in data:
    output.writerow(row.values())
'''

import json
import csv
import pandas as pd
lst_dics = []
filepath = r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.json'
with open(filepath, mode='r', errors='ignore') as json_file:
    for dic in json_file:
        lst_dics.append( json.loads(dic) )
## print the first one
lst_dics[0]


## create dtf = dataframe
dtf = pd.DataFrame(lst_dics)

## filter categories
#dtf = dtf[ dtf["category"].isin(['ENTERTAINMENT','POLITICS','TECH']) ][["category","headline"]]
## rename columns
#dtf = dtf.rename(columns={"category":"y", "headline":"text"})
## print 5 random rows
#dtf.sample(5)

dtf.to_csv(r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.csv')

def to_xml(df, filename=None, mode='w'):
    def row_to_xml(row):
        xml = ['<item>']
        for i, col_name in enumerate(row.index):
            xml.append('  <field name="{0}">{1}</field>'.format(col_name, row.iloc[i]))
        xml.append('</item>')
        return '\n'.join(xml)
    res = '\n'.join(df.apply(row_to_xml, axis=1))

    if filename is None:
        return res
    with open(filename, mode) as f:
        f.write(res)

dtf.to_xml(r'G:\d_drive\KerasExample\Knife_Dataset\data\training\train.xml')