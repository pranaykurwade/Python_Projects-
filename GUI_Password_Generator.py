from tkinter import *
from tkinter import ttk
import string
import random
import pyperclip

def generate():
    small_letter = string.ascii_lowercase
    capital_letter = string.ascii_uppercase
    numbers = string.digits
    symbols = string.punctuation
    
    weak = small_letter + capital_letter 
    medium = weak + numbers
    strong = medium + symbols
    
    password_length = int(input_box.get()) 
    
    # password = random.sample(word,password_length)
    # Output_field.insert(0,password)
    
    if choice.get() == 1:
        Output_field.insert(0,random.sample(weak,password_length))
    if choice.get() == 2:
        Output_field.insert(0,random.sample(medium,password_length))
    if choice.get() == 3:
        Output_field.insert(0,random.sample(strong,password_length))
        
def copy_password():
    genrated_password = Output_field.get()
    pyperclip.copy(genrated_password)

root=Tk()
root.geometry("275x455")
root.config(bg="Indigo")

choice=IntVar()

label = Label(root,text="Password Generator",font=('Copper Black',20,'bold'),fg="White",bg="Lime")
label.grid(pady=5)

label2 = Label(root,text="Password Type",font=('Arial',20,'bold'),fg="Black",bg="Gray")
label2.grid(pady=5)

Weak_radio_button = Radiobutton(root,text="Weak",value=1,variable=choice,font=('Arial',15,'bold'),fg="Black",bg="Azure") 
Weak_radio_button.grid(pady=5)

Medium_radio_button = Radiobutton(root,text="Medium",value=2,variable=choice,font=('Arial',15,'bold'),fg="Black",bg="Azure") 
Medium_radio_button.grid(pady=5)

Strong_radio_button = Radiobutton(root,text="Strong",value=3,variable=choice,font=('Arial',15,'bold'),fg="Black",bg="Azure") 
Strong_radio_button.grid(pady=5)

label3 = Label(root,text="Password Length",font=('Arial',20,'bold'),fg="Black",bg="Gray")
label3.grid(pady=5)

input_box = Spinbox(root,from_=5,to_=16,width=5,font=('Arial',15,'bold'),fg="Black",bg="Azure")
input_box.grid(pady=5) 

Generate_Button = Button(root,text="Generate",font=('Arial',15,'bold'),fg="Black",bg="Azure",command=generate)
Generate_Button.grid(pady=5)

Output_field = Entry(root,width=23,bd=2,font=('Arial',15,'bold'),fg="Black",bg="Azure")
Output_field.grid(pady=5)

copy_button = Button(root,text="Copy",font=('Arial',15,'bold'),fg="Black",bg="Azure",command=copy_password)
copy_button.grid(pady=5)

root.mainloop()

