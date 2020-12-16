inv=input()
num=int(inv)
n=list(inv)
leng=len(n)
add=0
if(num>0):
    if(int(n[leng-1])>0):
        if(int(n[leng-2])>0):
            add=int(n[leng-1])+int(n[leng-2])
            if(add%4==0):
                print("yes")
            else:
                print("no")
                
        else:
            add=int(n[leng-1])+int(n[1])
            if(add%4==0):
                print("yes")
            else:
                print("no")
    else:
        add=int(n[leng-1])+int(n[1])
        if(add%4==0):
            print("yes")
        else:
            print("no")
else:
    add=int(n[leng-1])+int(n[1])
    if(add%4==0):
        print("yes")
    else:
        print("no")

        

