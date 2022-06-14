import pandas as pd

df = pd.read_excel("fp.ods")

d=dict()
d={
    "Signed Longword(4)":"INT_32",
    "1":"int"
}
#print(df.iloc[256])
ans=""
for i in range(len(df)):
    #print(i)
    fieldname=df.iloc[i][0]
    datatype = ""#df.iloc[i][1]
    size = ""#df.ioc[i][2]
    #size = d[df.iloc[i][2]]
    defaultvalue=df.iloc[i][3]
    #print(type(defaultvalue))
    #if(df.iloc[i][3])

    z='<msg_fields field_name = "'+ str(fieldname) +'" data_type = "'+ str(datatype)+'" size= "'+size+'"'+'" default_value= "'+str(defaultvalue)+'"'
    ans+=z+'\n'
    #print(z)
#print(ans)
f = open("newfile.txt", "x")
f = open("newfile.txt", "w")
f.write(ans)
f.close()
