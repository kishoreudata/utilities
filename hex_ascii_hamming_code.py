# Python code to convert binary number
# into hexadecimal number

# function to convert
# binary to hexadecimal

def binToHexa(n):
	bnum = int(n)
	temp = 0
	mul = 1
	
	# counter to check group of 4
	count = 1
	
	# char array to store hexadecimal number
	hexaDeciNum = ['0'] * 100
	
	# counter for hexadecimal number array
	i = 0
	while bnum != 0:
		rem = bnum % 10
		temp = temp + (rem*mul)
		
		# check if group of 4 completed
		if count % 4 == 0:
			
			# check if temp < 10
			if temp < 10:
				hexaDeciNum[i] = chr(temp+48)
			else:
				hexaDeciNum[i] = chr(temp+55)
			mul = 1
			temp = 0
			count = 1
			i = i+1
			
		# group of 4 is not completed
		else:
			mul = mul*2
			count = count+1
		bnum = int(bnum/10)
		
	# check if at end the group of 4 is not
	# completed
	if count != 1:
		hexaDeciNum[i] = chr(temp+48)
		
	# check at end the group of 4 is completed
	if count == 1:
		i = i-1
		
	# printing hexadecimal number
	# array in reverse order
	print("\n Hexadecimal equivalent of {}: ".format(n), end="")
	str1 = "" 
	while i >= 0:
		print(end=hexaDeciNum[i])
		#print(type(hexaDeciNum[i]))
		str1+=hexaDeciNum[i]
		i = i-1
	print('\n')
	#print(hexaDeciNum.decode())
	#byte_array=bytearray(hexaDeciNum)
	#byte_array = bytearray.fromhex(hexaDeciNum)
	#print(byte_array.decode())

    # traverse in the string  
	#for ele in hexaDeciNum: 
	#	str1 += ele
	#	str1 = ele+str1
	#print(str1)
	#str1.decode("hex")
	#byte_array = bytearray.fromhex(str1)
	#print("corresponding ascii value is:  ",byte_array.decode())
	#print(byte_array.decode())
    
	print("\n Corresponding ASCII value is : ",hexToASCII(str1))
# Python3 program to convert hexadecimal
# string to ASCII format string
 
def hexToASCII(hexx):
 
    # initialize the ASCII code string as empty.
    ascii = ""
 
    for i in range(0, len(hexx), 2):
 
        # extract two characters from hex string
        part = hexx[i : i + 2]
 
        # change it into base 16 and
        # typecast as the character
        ch = chr(int(part, 16))
 
        # add this char to final ASCII string
        ascii += ch
     
    return ascii    
# Driver code
#if __name__ == '__main__':
	#binToHexa('111101111011')



#### DANIEL MUTHAMA
option=int(input('Press 1 for generating hamming code  \nPress 2 for finding error in hamming code\n\t Enter your choice:--\n'))

if(option==1):  # GENERATE HAMMING CODE
    print('Enter the data bits')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,h=0,0,0,0,[]

    while ((len(d)+r+1)>(pow(2,r))):
        r=r+1

    for i in range(0,(r+len(data))):
        p=(2**c)

        if(p==(i+1)):
            h.append(0)
            c=c+1

        else:
            h.append(int(data[j]))
            j=j+1

    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):
            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            ch+=1

    h.reverse()
    print('Hamming code generated would be:- ', end="")
    print(int(''.join(map(str, h))))
    binToHexa(int(''.join(map(str, h))))

elif(option==2): # DETECT ERROR IN RECEIVED HAMMING CODE
    print('Enter the hamming code received')
    d=input()
    data=list(d)
    data.reverse()
    c,ch,j,r,error,h,parity_list,h_copy=0,0,0,0,0,[],[],[]

    for k in range(0,len(data)):
        p=(2**c)
        h.append(int(data[k]))
        h_copy.append(data[k])
        if(p==(k+1)):
            c=c+1
            
    for parity in range(0,(len(h))):
        ph=(2**ch)
        if(ph==(parity+1)):

            startIndex=ph-1
            i=startIndex
            toXor=[]

            while(i<len(h)):
                block=h[i:i+ph]
                toXor.extend(block)
                i+=2*ph

            for z in range(1,len(toXor)):
                h[startIndex]=h[startIndex]^toXor[z]
            parity_list.append(h[parity])
            ch+=1
    parity_list.reverse()
    error=sum(int(parity_list) * (2 ** i) for i, parity_list in enumerate(parity_list[::-1]))
    
    if((error)==0):
        print('\nThere is no error in the hamming code received')

    elif((error)>=len(h_copy)):
        print('\nError cannot be detected')

    else:
        print('\nError is in',error,'bit')

        if(h_copy[error-1]=='0'):
            h_copy[error-1]='1'

        elif(h_copy[error-1]=='1'):
            h_copy[error-1]='0'
            print('\nAfter correction hamming code is:- ')
        h_copy.reverse()
        print(int(''.join(map(str, h_copy))))
        binToHexa(int(''.join(map(str, h_copy))))

else:
    print('\nOption entered does not exist')

