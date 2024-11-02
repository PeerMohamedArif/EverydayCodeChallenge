# def add(*args):
#     sum=0
#     for n in args:
#         sum+=n
#     return sum
#
# # print(add(3,5,6))
#
# def calculate(n,**kwargs):
#     print(kwargs)
#     for key,value in kwargs.items():
#         print(key)
#         print(value)
#     print(kwargs["add"])
#     #print(kwargs[1])
#
#
#     n+=kwargs["add"]
#     print(n)
#     n*=kwargs["multiply"]
#     print(n)
#
# calculate(2,add=3,multiply=5)


from tkinter import *

window= Tk()
window.title("My First GUI Program")
window.minsize(width=500,height=300)

#label
my_label=Label(text=" I am a Label", font=("Arial",24,"bold"))
my_label.pack()

my_label["text"]="New text"
my_label.config(text="New Text")

def button_clicked():
    print("I got clicked")
    new_text=input.get()
    my_label.config(text=new_text)
#Button
button=Button(text="Click Me",command=button_clicked)
button.pack()

#entry
input =Entry(width=10)
input.pack()
print(input.get())


window.mainloop()
