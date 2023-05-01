from tkinter import *
from tkinter import messagebox
from django import
from import tensorflow import keras


window = Tk()


num1 = eval(input("enter num1"))
num2 = eval(input("enter num2"))
sum = int(num1) + int(num2)
print("the sum is", sum)

def adding():
    messagebox.showinfo("the sum iss",sum)

label = Label(window,text = " My Name programme")
button = Button(window,text="Click to find my name",command=adding())
label.pack()
button.pack()

window.mainloop()

