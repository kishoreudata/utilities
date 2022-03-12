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
for i in range(3,101):
    b="B"+str(i)
    #print(type(b))
    b1="B"+str(2*(i-1))
    if(i<52): 
        bnew=sheet[b1].value
        #print(bnew)
        #print(type(bnew))
        sheet[b]=bnew
    else:sheet[b]=""    
    #print(type("B"+str(i)))
    #print(i)
#save the file
#workbook.save(filename="output.xlsx")
#print("Done");

#convert columns A , B, C in excel sheet to lowercase 
for i in range (1,52):
    a="A"+str(i)
    b="B"+str(i)
    c="C"+str(i)
    aval=sheet[a].value
    bval=sheet[b].value
    cval=sheet[c].value
    if aval is not None:sheet[a]=str.lower(aval)
    if bval is not None:sheet[b]=str.lower(bval)
    if cval is not None:sheet[c]=str.lower(cval)
#workbook.save(filename="output.xlsx")
#print("Done");

#compare column A and B

a = [1, 2, 3, 4, 5,6]
b = [9, 8, 7, 6, 5]
#print(set(a) & set(b))
#print(type(set(a) & set(b)))
a=["abc","def"]
b=["abc","def","ghi"]
test_set=set(a)&set(b)
#for val in test_set:
    #print(val)
    #print(type(val))
#A=[]
A,B=([]for i in range(2))
for i in range(1,52):
    A.append(sheet["A"+str(i)].value)
    B.append(sheet["B"+str(i)].value)
C=set(A)&set(B)
j=2
for c in C:
    sheet["C"+str(j)]=c
    j+=1
    
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