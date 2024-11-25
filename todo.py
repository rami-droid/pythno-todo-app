from tkinter import *

def KBDaddToList(e):
    on_button_click()

class todo:
    label = Label
    text = Text
    deleteBtn = Button(text="delete")
#adds input to list and sends to display
def on_button_click():
    if todoEntry.get() != "":
        todos.append(todoEntry.get())
        todoText.insert(END, todoEntry.get() + "\n")
        todoEntry.delete(0, len(todoEntry.get()))

#deletes top todo from list
def on_delete_click():
    return

todos = []

#define main window
root = Tk()
root.title = "todo app"
root.minsize(500, 500)

#add to list button
button = Button(root, text="add to list", command=on_button_click)
root.bind('<Return>', KBDaddToList)

deleteBtn = Button(root, text="delete from list", command=on_delete_click)


exitBtn = Button(root, text="exit", command=root.destroy)

todoEntry = Entry(root)

#output for todo list
displayFrame = Frame()
todoText = Text(displayFrame)


#pack everything in windows
button.pack()
deleteBtn.pack()
exitBtn.place(x=600, y=1)
todoEntry.pack()
displayFrame.pack()
todoText.pack()


root.mainloop()