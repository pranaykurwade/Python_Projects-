from tkinter import *
from tkinter import ttk

result = ""

def calculation(input):
    global result 
    result += str(input)
    text_result.delete(1.0,END)
    text_result.insert(1.0,result)
    
def evaluate_calculation():
    global result 
    try:
        result = str(eval(result))
        text_result.delete(1.0,END)
        text_result.insert(1.0,result)
    except:
        clear_field()
        text_result.insert(1.0,"Error")
        
def clear_field():
    global result 
    result=''
    text_result.delete(1.0,END)
    
root = Tk()
root.geometry("300x275")

text_result = Text(root,height=2,width=30,font="broadway,25",bg="black",fg="lime")
text_result.grid(columnspan = 5)

button_1 = Button(root,text="1",command=lambda:calculation(1),width=5,font="broadway,20",bg="aqua")
button_1.grid(row=2,column=1)
button_2 = Button(root,text="2",command=lambda:calculation(2),width=5,font="broadway,20",bg="aqua")
button_2.grid(row=2,column=2)
button_3 = Button(root,text="3",command=lambda:calculation(3),width=5,font="broadway,20",bg="aqua")
button_3.grid(row=2,column=3)
button_4 = Button(root,text="4",command=lambda:calculation(4),width=5,font="broadway,20",bg="aqua")
button_4.grid(row=3,column=1)
button_5 = Button(root,text="5",command=lambda:calculation(5),width=5,font="broadway,20",bg="aqua")
button_5.grid(row=3,column=2)
button_6 = Button(root,text="6",command=lambda:calculation(6),width=5,font="broadway,20",bg="aqua")
button_6.grid(row=3,column=3)
button_7 = Button(root,text="7",command=lambda:calculation(7),width=5,font="broadway,20",bg="aqua")
button_7.grid(row=4,column=1)
button_8 = Button(root,text="8",command=lambda:calculation(8),width=5,font="broadway,20",bg="aqua")
button_8.grid(row=4,column=2)
button_9 = Button(root,text="9",command=lambda:calculation(9),width=5,font="broadway,20",bg="aqua")
button_9.grid(row=4,column=3)
button_0 = Button(root,text="0",command=lambda:calculation(0),width=5,font="broadway,20",bg="aqua")
button_0.grid(row=5,column=2)
button_close = Button(root,text=")",command=lambda:calculation(')'),width=5,font="broadway,20",bg="aqua")
button_close.grid(row=5,column=3)
button_open = Button(root,text="(",command=lambda:calculation("("),width=5,font="broadway,20",bg="aqua")
button_open.grid(row=5,column=1)
button_plus = Button(root,text="+",command=lambda:calculation("+"),width=5,font="broadway,20",bg="aqua")
button_plus.grid(row=2,column=4)
button_minus = Button(root,text="-",command=lambda:calculation("-"),width=5,font="broadway,20",bg="aqua")
button_minus.grid(row=3,column=4)
button_mul = Button(root,text="*",command=lambda:calculation("*"),width=5,font="broadway,20",bg="aqua")
button_mul.grid(row=4,column=4)
button_div = Button(root,text="/",command=lambda:calculation("/"),width=5,font="broadway,20",bg="aqua")
button_div.grid(row=5,column=4)
button_equal = Button(root,text="=",command=evaluate_calculation,width=11,font="broadway,20",bg="aqua")
button_equal.grid(row=6,column=1,columnspan=2)
button_clear = Button(root,text="C",command=clear_field,width=11,font="broadway,20",bg="aqua")
button_clear.grid(row=6,column=3,columnspan=2)

root.mainloop()