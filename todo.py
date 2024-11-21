from tkinter import *

#adds input to list and sends to display
def on_button_click(self):
    if todoEntry.get() != "":
        todos.append(todoEntry.get())
        todoText.insert(END, todoEntry.get() + "\n")
        todoEntry.delete(0, len(todoEntry.get()))

todos = []

#define main window
root = Tk()
root.title = "todo app"
root.minsize(500, 500)

#add to list button
button = Button(root, text="add to list", command=on_button_click)
root.bind('<Return>', on_button_click)


exitBtn = Button(root, text="exit", command=root.destroy)

todoEntry = Entry(root)

#output for todo list
displayFrame = Frame()
todoText = Text(displayFrame)


#pack everything in windows
button.pack()
exitBtn.place(x=600, y=1)
todoEntry.pack()
displayFrame.pack()
todoText.pack()

root.mainloop()