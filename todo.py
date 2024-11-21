from tkinter import *

def on_button_click():
    print("button clicked!")


root = Tk()

button = Button(root, text="click me", command=on_button_click)

button.pack(padx=20, pady=20)

root.mainloop()