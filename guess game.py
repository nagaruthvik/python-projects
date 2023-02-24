from tkinter import *


def isChecked():
    if cb.get() == 5:
        root.destroy()
        import level1

def ischecked():
    if ax.get()==5:
        root.destroy()
        import level2

def button1():
    import about
def button2():
    import help
root=Tk()
root.geometry("500x500")
Label(root,text="GUESS THE NUMBER",font=("",20)).place(x=110,y=110)
cb = IntVar(value=1)
lev1 = Checkbutton(root, text="LEVEL-1", variable=cb, onvalue=5, offvalue=6, command=isChecked)
lev1.place(x=220, y=230)

ax = IntVar(value=1)

lev2 = Checkbutton(root, text="LEVEL-2", variable=ax, onvalue=5, offvalue=6, command=ischecked)
lev2.place(x=220, y=250)

but1=Button(root,text="About",width=5,height=2,bg="blue",fg="white",command=button1).place(x=200,y=340)
but2=Button(root,text="Help",width=5,height=2,bg="blue",fg="white",command=button2).place(x=280,y=340)
root.mainloop()
