import os
import re

def demicrosoft (fn):

    fn = re.sub('(', '', fn)
    fn = re.sub(')', '', fn)
    for ch in [' ']:
        fn = fn.replace(ch,""+ch)
    return fn

yourpath = os.getcwd()
for root, dirs, files in os.walk(yourpath, topdown=False):
    for name in files:
        out=name.replace('(','')
        o=out.replace(')','')
        f=o.replace(' ','')
        print(f)
        try:
            os.rename(name, f)
        except:
            print("error")
				
				


