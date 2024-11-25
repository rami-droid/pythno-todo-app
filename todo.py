from tkinter import *

def KBDaddToList(e):
    addTodo()

class todo:
    def __init__(self, parent, todoText) -> None:
        self.frame = Frame(parent)
        self.label = Label(self.frame, text=todoText, width=40, anchor="w")
        self.text = todoText
        self.deleteBtn = Button(self.frame, text="delete", command=self.delete)


        self.label.pack(side=LEFT, padx=5, pady=5)
        self.deleteBtn.pack(side=RIGHT, padx=5, pady=5)

    def pack(self):
        self.frame.pack()

    def delete(self):
        self.frame.destroy()
 


def addTodo():
    todoText = todoEntry.get()
    print(todoText)
    if todoText:
        newTodo = todo(displayFrame, todoText)
        todos.append(newTodo)
        newTodo.pack()
        todoEntry.delete(0, END)


#deletes top todo from list
def on_delete_click():
    return

todos = []

#define main window
root = Tk()
root.title = "todo app"
root.minsize(500, 500)

#add to list button
button = Button(root, text="add to list", command=addTodo)
root.bind('<Return>', KBDaddToList)

buttonFrame = Frame()

exitBtn = Button(root,  text="exit", command=root.destroy)

todoEntry = Entry(root)


#output for todo list
displayFrame = Frame()
# todoText = Text(displayFrame)

#pack everything in windows
button.pack()
exitBtn.pack()
todoEntry.pack()
displayFrame.pack()


root.mainloop()