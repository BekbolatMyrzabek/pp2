address = "1.1.1.1"
s = ''
for i in range(len(address)):
    if(address[i] == '.'):
        s = s+'[.]'
    else:
        s = s+address[i]
            
return s

#Output: "1[.]1[.]1[.]1"