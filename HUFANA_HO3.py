import tkinter as me

window=me.Tk()
window.title("Simple Calculator")
window.geometry("200x200")
window.config(bg="black")

label=me.Label(window,text="Simple Calculation",width=28,height=2)
label.grid(row=0,column=0,columnspan=2)

me.Label(window,text="Enter 1st Number:").place(x=10,y=45)
entry1=me.Entry(window,width=10)
entry1.place(x=120,y=45)

me.Label(window,text="Enter 2nd Number:").place(x=8,y=80)
entry2=me.Entry(window,width=10)
entry2.place(x=120,y=80)

def add():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1+num2
    label.config(text=f"The sum of {num1} + {num2} = {result}")

def subtract():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1-num2
    label.config(text=f"subtracting the number {num1} - {num2} = {result}")

def multiply():
    num1=int(entry1.get())
    num2=int(entry2.get())
    result=num1*num2
    label.config(text=f"The multiplication of {num1} x {num2} = {result}")

def divide():
    num1=float(entry1.get())
    num2=float(entry2.get())
    result=num1/num2
    label.config(text=f"The answer is {num1} / {num2} = {result}")

button_add=me.Button(window,text="Add",command=add)
button_add.place(x=45,y=110)

button_sub=me.Button(window,text="Subtract",command=subtract)
button_sub.place(x=125,y=110)

button_multi=me.Button(window,text="Multiply",command=multiply)
button_multi.place(x=35,y=150)

button_Div=me.Button(window,text="Division",command=divide)
button_Div.place(x=126,y=150)

window.mainloop()