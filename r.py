import tkinter as tk
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
from tkinter import END
my_w = tk.Tk()
my_w.geometry("400x300")  # Size of the window 
my_w.title('www.plus2net.com')
my_font1=('times', 18, 'bold')
l1 = tk.Label(my_w,text='My Note Book',width=30,font=my_font1)  
l1.grid(row=1,column=1)

t1 = tk.Text(my_w,  width=40, height=3)
t1.grid(row=2,column=1)

b1 = tk.Button(my_w, text='Save',command=lambda:save_file(), width=20)
b1.grid(row=4,column=1) 
def save_file():
    my_str1=t1.get("1.0",END)  # read from one text box t1
    fob=filedialog.asksaveasfile(filetypes=[('text file','*.txt')],
        defaultextension='.txt',initialdir='D:\\my_data\\my_html',
        mode='w')
    try:
        fob.write(my_str1)
        fob.close()
        t1.delete('1.0',END) # Delete from position 0 till end 
        t1.update()  
        b1.config(text="Saved")
        b1.after(3000, lambda: b1.config(text='Save'))
    except :
        print (" Bill Generated Successfully ")
my_w.mainloop()  # Keep the window open
