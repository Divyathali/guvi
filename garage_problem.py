n=input().split(" ")

if(int(n[0])<=4):
    print(10+int(n[1]))

else:
    num=int(n[0])-4
    num=num*15
    print(10+int(n[1])+num)
