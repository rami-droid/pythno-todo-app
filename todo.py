from tkinter import *

def on_button_click():
    todos.append(todoEntry.get())
    todoText.insert(END, todoEntry.get() + "\n")
    todoEntry.delete(0, len(todoEntry.get()))
    print(todos)

todos = []

root = Tk()
root.title = "todo app"
root.minsize(500, 500)

button = Button(root, text="add to list", command=on_button_click)
exitBtn = Button(root, text="exit", command=root.destroy)

todoEntry = Entry(root)

displayFrame = Frame()
todoText = Text(displayFrame)

button.pack()
exitBtn.place(x=600, y=1)
todoEntry.pack()
displayFrame.pack()
todoText.pack()

root.mainloop()