from tkinter import *
from time import strftime

root=Tk()
root.title("Digital Clock")

label = Label(root,
             background="White",
             foreground="Blue",
             font=("Bolder",80,"bold"))
label.pack(anchor='center')

def time():
  str = strftime("%H:%M:%S %p")
  label.config(text=str)
  label.after(1000,time)

time()
mainloop()