num=int(input("enter nth term of series"))

for i in range(num,0,-1):
    for j in range(1,i+1):
        print(j,end="")
    for j in range(1,2*(num-i)):
        print(" ",end="")
    for j in range(i,0,-1):
        if(j==num):
            continue
        print(j,end="")
    print(" ")

a
