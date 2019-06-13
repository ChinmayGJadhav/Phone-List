# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 13:09:01 2019

@author: chinmay
"""

from tkinter import *
root=Tk()
root.geometry("500x500")
root.title("Phone List")
f=Frame(root,height=100,width=500,bg="Red")
f.pack()
rootlabel = Label(root,text="PhoneList",bg='grey',font=("Times",20,'italic'))
rootlabel.pack(side=RIGHT)
PhoneList=[]

l1= Label(root,text="Name")
l1.place(x=60,y=100)
l2= Label(root,text="Phone NO")
l2.place(x=60,y=150)

#var1=StringVar()
var2=StringVar()
var3=StringVar()
#e1= Entry(root,textvariable=var1,bd=5)
e1= Entry(root,bd=5)
e2= Entry(root,textvariable=var2,bd=5)
t3= Text(root,height=10,width=50,bd=5)
e1.place(x=120,y=100)
e2.place(x=120,y=150)
t3.pack(side=BOTTOM)
#
def add():
    global PhoneList
    name=e1.get()
    PN=var2.get()
    data=[]
    data.append(name)
    data.append(PN)
    PhoneList.append(data)
    print( PhoneList)
    
def delete():
    global PhoneList
    name=e1.get()
    PN=var2.get()
    data=[]
    data.append(name)
    data.append(PN)
    PhoneList.remove(data)
    print( PhoneList)
    
def update():
    global PhoneList
    name=e1.get()
    n=len(PhoneList)
    for i in range(n):
        if PhoneList[i][0]==name:
            PhoneList[i][1]=var2.get()
    print( PhoneList)

def show():
    t3.insert(END,PhoneList)
    t3.insert(END,"\n")
    
b1=Button(root,text="Add",command=add)
b2=Button(root,text="Delete",command=delete)
b3=Button(root,text="Update",command=update)
b4=Button(root,text="Show",command=show)
b1.place(x=100,y=250)
b2.place(x=150,y=250)
b3.place(x=200,y=250)
b4.place(x=250,y=250)
root.mainloop()
