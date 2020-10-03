from tkinter import *
window = Tk()
window.geometry("500x300")
window.title("calculator")
window.config(bg="blue")
def action():
    print("button clicked")
button1= Button(text="ok",command=action)
button2= Button(text="ok",command=action)
button1.grid(row=0,column=0)
button2.grid(row=0,column=1)
label=Label(window,text="welcome",bg="red",fg='blue')





window.mainloop()
