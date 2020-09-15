from tkinter import  *
from tkinter import messagebox
import random
top = Tk()
top.geometry("200x200")
top.configure(bg="#1B1011")


def start():
   my_list=list(range(1,9))
   b=list(random.sample(my_list,8))
   print(b)
   n1.set(b[0])
   n2.set(b[1])
   n3.set(b[2])
   n4.set(b[3])
   n5.set(b[4])
   n6.set(b[5])
   n7.set(b[6])
   n8.set(b[7])
   n9.set("")

def task(var):
   if(var=="b9"):
      btext=b9['text']
      if(b8['text']==""):
         n8.set(btext)
         n9.set("")
      elif(b6['text']==""):
         n6.set(btext)
         n9.set("")

   elif(var=="b8"):
      btext=b8['text']
      
      if(b7['text']==""):
         n7.set(btext)
         n8.set("")
      elif(b5['text']==""):
         n5.set(btext)
         n8.set("")
      elif(b9['text']==""):
         n9.set(btext)
         n8.set("")
   
      
   
   elif(var=="b7"):
      btext=b7['text']
      if(b4['text']==""):
         n4.set(btext)
         n7.set("")
      if(b8['text']==""):
         n8.set(btext)
         n7.set("")

   elif(var=="b6"):
      btext=b6['text']
      if(b9['text']==""):
         n9.set(btext)
         n6.set("")
      elif(b5['text']==""):
         n5.set(btext)
         n6.set("")
      elif(b3['text']==""):
         n3.set(btext)
         n6.set("")


   elif(var=="b5"):
      btext=b5['text']
      if(b8['text']==""):
         n8.set(btext)
         n5.set("")
      elif(b6['text']==""):
         n6.set(btext)
         n5.set("")
      elif(b4['text']==""):
         n4.set(btext)
         n5.set("")
      elif(b2['text']==""):
         n2.set(btext)
         n5.set("")


   
   elif(var=="b4"):
      btext=b4['text']
      if(b7['text']==""):
         n7.set(btext)
         n4.set("")
      elif(b5['text']==""):
         n5.set(btext)
         n4.set("")
      elif(b1['text']==""):
         n1.set(btext)
         n4.set("")
   
   elif(var=="b3"):
      btext=b3['text']
      if(b6['text']==""):
         n6.set(btext)
         n3.set("")
      elif(b2['text']==""):
         n2.set(btext)
         n3.set("")
   
   elif(var=="b2"):
      btext=b2['text']
      if(b5['text']==""):
         n5.set(btext)
         n2.set("")
      elif(b3['text']==""):
         n3.set(btext)
         n2.set("")
      elif(b1['text']==""):
         n1.set(btext)
         n2.set("")
   
   elif(var=="b1"):
      btext=b1['text']
      if(b4['text']==""):
         n4.set(btext)
         n1.set("")
      elif(b2['text']==""):
         n2.set(btext)
         n1.set("")
   if(b1['text']==1 and b2['text']==2 and b3['text']==3 and b4['text']==4 and b5['text']==5 and b6['text']==6 and b7["text"]==7 and b8['text']==8):
      messagebox.showinfo("yes", "you won")
   

      
      
   

      
   
   

n1=StringVar()
b1=Button(top, textvariable=n1, borderwidth = 5 , command= lambda:task("b1"),bg="#FFC0CB")
b1.place(x=45,y=10)
b1.config(width=3, height=2)

n2=StringVar()
b2=Button(top, textvariable=n2, borderwidth = 5, command= lambda:task("b2"),bg="#FFC0CB" )
b2.place(x=85, y=10)
b2.config(width=3, height=2)



n3=StringVar()
b3=Button(top, textvariable=n3, borderwidth = 5 , command= lambda:task("b3"),bg="#FFC0CB")
b3.place(x=125,y=10)
b3.config(width=3, height=2)

n4=StringVar()
b4=Button(top, textvariable=n4, borderwidth = 5 ,command= lambda:task("b4"),bg="#FFC0CB")
b4.place(x=45,y=60)
b4.config(width=3, height=2)

n5=StringVar()
b5=Button(top, textvariable=n5, borderwidth = 5, command= lambda:task("b5") ,bg="#FFC0CB")
b5.place(x=85,y=60)
b5.config(width=3, height=2)


n6=StringVar()
b6=Button(top, textvariable=n6, borderwidth = 5, command= lambda:task("b6"),bg="#FFC0CB" )
b6.place(x=125,y=60)
b6.config(width=3, height=2)


n7=StringVar()
b7=Button(top, textvariable=n7, borderwidth = 5 ,command = lambda:task("b7"),bg="#FFC0CB")
b7.place(x=45,y=110)
b7.config(width=3, height=2)

n8=StringVar()
b8=Button(top, textvariable=n8, borderwidth = 5 ,command=lambda:task("b8"),bg="#FFC0CB")
b8.place(x=85,y=110)
b8.config(width=3, height=2)

n9=StringVar()
b9=Button(top, textvariable=n9, borderwidth = 5 ,command= lambda:task("b9"),bg="#FFC0CB")
b9.place(x=125,y=110)
b9.config(width=3, height=2)

b=Button(top, text="start", command=start, bg="#FFC0CB")
b.place(x= 85, y =160)
b.config(width=4, height=1)




