from tkinter import *
root=Tk()
e=Entry(root,width=35,borderwidth=5)
e.grid(row=0,column=0,columnspan=3,padx=30)
nlist=[]
def number_input(number):
    cur=e.get()
    e.delete(0,END)
    e.insert(0,str(cur)+str(number))

def clear_val():
    nlist.clear()
    e.delete(0,END)

def add():
    num1=e.get()
    nlist.append(int(num1))
    e.delete(0,END)

def equals():
    num1=e.get()
    nlist.append(int(num1))
    e.delete(0,END)
    sum=0
    for val in nlist:
        sum+=int(val)

    e.insert(0,str(sum))


#buttons clear equals etc
b9=Button(root,text="9",padx=40,pady=20,command=lambda:number_input(9)).grid(row= 1, column=0)
b8=Button(root,text="8",padx=40,pady=20,command=lambda:number_input(8)).grid(row= 1, column=1)
b7=Button(root,text="7",padx=40,pady=20,command=lambda:number_input(7)).grid(row= 1, column=2)
b6=Button(root,text="6",padx=40,pady=20,command=lambda:number_input(6)).grid(row= 2, column=0)
b5=Button(root,text="5",padx=40,pady=20,command=lambda:number_input(5)).grid(row= 2, column=1)
b4=Button(root,text="4",padx=40,pady=20,command=lambda:number_input(4)).grid(row= 2, column=2)
b3=Button(root,text="3",padx=40,pady=20,command=lambda:number_input(3)).grid(row= 3, column=0)
b2=Button(root,text="2",padx=40,pady=20,command=lambda:number_input(2)).grid(row= 3, column=1)
b1=Button(root,text="1",padx=40,pady=20,command=lambda:number_input(1)).grid(row= 3, column=2)
b0=Button(root,text="0",padx=40,pady=20,command=lambda:number_input(0)).grid(row= 4, column=0)

badd=Button(root,text="+",padx=40,pady=20,command=add).grid(row= 4, column=1,columnspan=2)
b_clear=Button(root,text="clrs",padx=40,pady=20,command=clear_val).grid(row=5 , column=0)
bequal=Button(root,text="=",padx=40,pady=20,command=equals).grid(row=5 , column=1,columnspan=2)


root.mainloop()