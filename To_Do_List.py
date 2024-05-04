from tkinter import *
from tkinter import ttk

class list:
  def __init__(self,root):
    self.root = root 
    self.root.title("To do List")
    self.root.geometry('650x410+300+150')

    self.label = Label(self.root, text="To-Do-List",font="broadway,25,bold", width=15 , bd=5 ,bg="orchid")
    self.label.pack(side='top',fill=BOTH)
    
    self.label1 = Label(self.root, text="Add Task",font="broadway,20,bold", width=10 , bd=5 ,bg="orchid")
    self.label1.place(x=40,y=55)
    
    self.label2 = Label(self.root, text="Tasks",font="broadway,20,bold", width=10 , bd=5 ,bg="orchid")
    self.label2.place(x=430,y=55)
    
    self.main_text = Listbox(self.root, height=10, bd=15 , width=25, font="broadway,20,bold")
    self.main_text.place(x=350,y=100)
    
    self.text = Text(self.root, bd=10, height=2, width=30, font="broadway,25,bold")
    self.text.place(x=20,y=100)
    
    def add_task():
        task = self.text.get(1.0,END)
        self.main_text.insert(END,task)
        with open('To_Do_List.txt','a') as f :
            f.write(task)
            f.seek(0)
            f.clase()
        self.text.delete(1.0,END)
        
    def delete_task():
        delete_ = self.main_text.curselection()
        line = self.main_text.get(delete_)
        with open('To_Do_List.txt', 'r+') as f :
            f_new = f.readlines()
            f.seek(0)
            for l in f_new:
                item = str(line)
                if item not in l :
                    f.write(l)
            f.truncate()
        self.main_text.delete(delete_)
        
    with open('To_Do_List.txt' , 'r') as f:
        read = f.readlines()
        for i in read:
            ready = i.split()
            self.main_text.insert(END,ready)
        f.close()
        
    self.button = Button(self.root, text="Add", font="broadway,20,bold", width=10 , bd=5 ,bg="orchid",command=add_task)
    self.button.place(x=30,y=180)
        
    self.button2 = Button(self.root, text="Delete", font="broadway,20,bold", width=10 , bd=5 ,bg="orchid",command=delete_task)
    self.button2.place(x=30,y=280)
    
        
def main():
  root = Tk()
  ui = list(root)
  root.mainloop()

if __name__ == "__main__":
  main()