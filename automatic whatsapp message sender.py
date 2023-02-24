from tkinter import *
import pywhatkit as done
def cancle():
    root.destroy()
def submit():
    a=box1.get()
    b=box2.get()
    c=box3.get()
    d=box4.get()

    e=int(c)
    f=int(d)
    done.sendwhatmsg("+91"+a,b,e,f)
    root.destroy()


root = Tk()
root.geometry("5000x5000")
lable=Label(root,text="AUTOMATIC WHATSAPP MESSAGE SENDER",font=("",25),bg="#25D366",fg="white")
lable.place(x=1,y=5,height=200,width=2000)
#
text=Label(root,text="ENTER PHONE NUMBER",font=("",20))
text1=Label(root,text="ENTER MESSAGE",font=("",20))
text.place(x=350,y=300)
text1.place(x=350,y=400)
#
box1=Entry(root,font=("",16))
box2=Entry(root,font=("",16))
box1.place(x=750,y=300,height=30,width=200)
box2.place(x=750,y=400,height=30,width=200)
#
text2=Label(root,text="SET DATE AND TIME",font=("",20))
text2.place(x=350,y=500)
box3=Entry(root,font=("",16))
text3=Label(root,text=":",font=("",30))
text3.place(x=780,y=490)
box4=Entry(root,font=("",16))
box3.place(x=750,y=500,height=30,width=30)
box4.place(x=800,y=500,height=30,width=30)
#
btn1=Button(root,text="submit",font=("",16),bg="white",command=submit)
btn1.place(x=600,y=600)
btn2=Button(root,text="cancle",font=("",16),bg="white",command=cancle)
btn2.place(x=750,y=600)

root.mainloop()
