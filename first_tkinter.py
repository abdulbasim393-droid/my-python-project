import tkinter as tk

def add():
    result = int(e1.get()) + int(e2.get())
    lbl_result.config(text="Result: " + str(result))

root = tk.Tk()
root.title("Adder App")

e1 = tk.Entry(root)
e1.pack()

e2 = tk.Entry(root)
e2.pack()

btn = tk.Button(root, text="Add", command=add)
btn.pack()

lbl_result = tk.Label(root, text="Result:")
lbl_result.pack()

root.mainloop()
