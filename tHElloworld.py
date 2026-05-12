from tkinter import *

window = Tk()

button = Button(window,
                 text="Hello world",
                 font=("Arial", 40, "bold"), 
                 fg="#0000ff", 
                 background="#00ff00")

button.config(activebackground="#00ff00")
button.config(activeforeground="#0000ff")
button.pack()

window.mainloop()