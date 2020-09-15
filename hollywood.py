import re
from tkinter import*
from tkinter import messagebox


chance=5
def start():
    w=E1.get()
    a=""
    for i in range(len(w)):
        a=a+"_ "
    ab.set(a)
    chances.set(chance)

def guess():
    global chance
    w1=E3.get()[0]
    w2=E2.get()
    w3=E1.get()
    chances.set(chance)
        


    if(chance>1):
        x=w1 in w3
        if(x==True):
            temp=list(w2)
            print(w2)
            matches = re.finditer(w1, E1.get())
            matches_positions = [match.start() for match in matches]
            for values in matches_positions:
                temp[values*2]=w1
                w2="".join(temp)
    
            ab.set(str(w2))
            y=w2.replace(" ","")
            if(y==w3):
                 messagebox.showinfo("YES!", "you won")
                 top.destroy()
        
        else:
            messagebox.showinfo("NO!", "wrong guess")
            chance=chance-1
            

        
            
    else:
        ab.set(w3)
        messagebox.showinfo("NO!", "Game Over")
        
        top.destroy()
        


top=Tk()
top.geometry("250x250+10+10")        



L1=Label(top , text="Enter Name" )
L1.place(x=10,y=20)

E1 = Entry(top, bd = 5, show="*")
E1.place(x=80,y=20)

B=Button(top , text="start", command=start)
B.place(x=100,y=50)

L1=Label(top , text="result" )
L1.place(x=10,y=80)

ab=StringVar()
E2=Entry(top, bd = 5, textvariable=ab)
E2.place(x=80,y=80)

chances=StringVar()
L1=Label(top , textvariable=chances,bd=5 ,padx=5)
L1.place(x=10,y=120)

E3 = Entry(top, bd = 5,)
E3.place(x=80,y=120)

B2=Button(top , text="guess", command=guess)
B2.place(x=70,y=160)




top.mainloop()
