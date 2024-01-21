from tkinter import *
import os

def restart():
	os.system("shutdown /r /t 1")
def restart_Time():
	os.system("shutdown /r /t 5")
def log_Out():
	os.system("shutdown -1")
def shutdown():
	os.system("shutdown /s /t 1")

st=Tk()
st.title("ShutDown App")
st.geometry("265x350")                                                   
st.config(bg="#33A4CB")
st.resizable(0,0)

label = Label(st,text="ShutDown Directly App",font=("Arial",17,"bold"),bg="#1F4260",fg="#9BDAF8")
label.grid(pady=5)

r_button=Button(st,text="Restart",font=("Arial",20,"bold"),
	relief=RAISED,cursor="plus",bg="#52DAEE",fg="orange",command=restart)
r_button.place(x=35,y=90,height=40,width=200)

rt_button=Button(st,text="Restart Time",font=("Arial",20,"bold"),
	relief=RAISED,cursor="plus",bg="#52DAEE",fg="orange",command=restart_Time)
rt_button.place(x=35,y=150,height=40,width=200)

lg_button=Button(st,text="Log Out",font=("Arial",20,"bold"),
	relief=RAISED,cursor="plus",bg="#52DAEE",fg="orange",command=log_Out)
lg_button.place(x=35,y=210,height=40,width=200)

sd_button=Button(st,text="Shut down",font=("Arial",20,"bold"),
	relief=RAISED,cursor="plus",bg="#52DAEE",fg="orange",command=shutdown)
sd_button.place(x=35,y=270,height=40,width=200)

st.mainloop()