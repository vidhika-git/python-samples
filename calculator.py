ans=0
while 1:
    n=int(input("enter 1st no."))
    m=int(input("enter 2nd no."))
    ope=input("enter  any mathematical operation from these: +, - ,* ,/and press '=' if you want to end")
    if(ope=="+"):
        ans=m+n
    elif(ope=="-"):
        if(m>n):
            ans=m-n
        else:
            ans=n-m
    elif(ope=="*"):
        ans=n*m
    elif(ope=="/"):
        if(m>n):
            ans=m/n
        else:
            ans=n/m
    elif(ope=="="):
        break
    print(ans)
print("thanks for using calculator")
    
        
