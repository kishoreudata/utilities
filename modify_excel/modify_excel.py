from openpyxl import load_workbook

#load excel file
workbook = load_workbook(filename="nifty.xlsx")

#open workbook
sheet = workbook.active

#modify the desired cell
sheet["A1"] = "NIFTY50"
#print(type("NIFTY50")) 
#print(type("A1"))
#print("hi")
#print(type(sheet["A1"]))
bs=[]
'''
for i in range(3,99):
    b1="B"+str(2*(i-1))
    bs.append(sheet[b1])
#print(type(bs))
for b in bs:print(b)
'''
for i in range(3,99):
    b="B"+str(i)
    #print(type(b))
    b1="B"+str(2*(i-1))
    if(i<50): 
        bnew=sheet[b1].value
        #print(bnew)
        #print(type(bnew))
        sheet[b]=bnew
    else:sheet[b]=""    
    #print(type("B"+str(i)))
    #print(i)
#save the file
workbook.save(filename="output.xlsx")
print("Done");
'''
import xlwt
import xlrd
from xlutils.copy import copy

# load the excel file
rb = xlrd.open_workbook('nifty.xlsx')

# copy the contents of excel file
wb = copy(rb)

# open the first sheet
w_sheet = wb.get_sheet(0)

# row number = 0 , column number = 1
w_sheet.write(0,1,'Modified !')

# save the file
wb.save('output.xlsx')
'''