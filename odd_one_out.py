
def odd_in_couples(a):
    b=[]
    i=0
    while i<(len(a)-1):
        #print(i)
        if(a[i]==a[i+1]):
            i=i+2
        else:
            b.append(a[i])
            i=i+1
    #checking if last element is single
    if(a[len(a)-1]!=a[len(a)-2]):b.append(a[len(a)-1])
    return b

def odd_freq_ele(a):
    d=dict()
    b=[]
    '''
    for i in range(len(a)):
        oldcount=d.get(a[i],0)
        d[a[i]]=oldcount+1
    '''
    for ele in a:
        d[ele]=d.get(ele,0)+1
        
    for key,value in d.items():
        #if(value!=2):b.append(key) #for unordered couples 
        if(value%2!=0):b.append(key)#for odd freq elements
    return b

def remove_file_extension(a):
    i=0
    for ele in a:
        if (ele.endswith('.jpg')):a[i]=ele.replace('.jpg','')
        elif (ele.endswith('.png')):a[i]=ele.replace('.png','')
        elif (ele.endswith('.xml')):a[i]=ele.replace('.xml','')
        i+=1
    return a

if __name__=="__main__":
    '''
    #function to find odd one out of couples
    #a=['a','a','b','c','c']
    #print(a[3])
    #print(type(a))
    #print(type(a[0]))
    #a=['a','b','b','c','c']
    #a=['a','a','b','c','c','d']
    #a=['a','a','b','c','c','d','e','e']
    #a=['a','a','b','c','c','d','e','f','f']
    #a=['abc','abc','def','ghi','ghi','jkl','mno','pqr','pqr']
    #a=['abc','abc','def','ghi','ghi','jkl','mno','pqr']
    b=odd_in_couples(a)
    for i in range(len(b)):
        print(b[i])
    '''
    #a=['1','2','3','2','3']
    #a=['0','1','2','3','2','3','0','4','5']
    #arr=['1.png','2.png','3.png','4.png','1.xml','2.xml']
    arr=['1.png','2.png','3.png','4.png','1.xml','2.xml','1.jpg']
    a=remove_file_extension(arr)
    b=odd_freq_ele(a)
    print("\nfiles which are single (either image or annotation is missing):")
    for i in range(len(b)):print(b[i])