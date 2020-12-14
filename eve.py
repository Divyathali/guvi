str=input()
str1=list(str)
temp=0
for i in range(len(str1)):
    temp+=int(str[i])
    
if(temp%2==0):
    print("E")
else:
    print("O")
