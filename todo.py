from tkinter import *

def on_button_click():
    todos.append(todoEntry.get())
    todoEntry.select_clear()
    print(todos)

todos = []

root = Tk()
root.title = "todo app"
root.minsize(500, 500)

button = Button(root, text="click me", command=on_button_click)

todoEntry = Entry(root)

button.pack(padx=20, pady=20)
todoEntry.pack()

root.mainloop()