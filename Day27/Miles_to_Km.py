from tkinter import *

from sqlalchemy import column

FONT=("New Times Roman",16,"bold")
window=Tk()
window.title("Miles to KM converter")
window.minsize(width=500,height=500)
window.config(padx=100,pady=200)

label= Label(text=" is equal to",font=FONT)
label.grid(row=1,column=0)

entry =Entry(width=10,font=FONT)
entry.grid(row=0,column=1)

answer=Label(text="0",font=FONT)
answer.grid(row=1,column=1)

mile_text=Label(text="Miles",font=FONT)
mile_text.grid(row=0,column=2)

km_text=Label(text="KM",font=FONT)
km_text.grid(row=1,column=2)

def button_clicked():
    solution = round((float(entry.get()) * 1.609), 4)
    answer.config(text=solution)

button=Button(text="Calculate",command=button_clicked)
button.grid(row=2,column=1)
window.mainloop()
