from customtkinter import *

from tkinter import *



def KBDaddToList(e):
    addTodo()

class todo:
    def __init__(self, parent, todoText) -> None:
        self.frame = CTkFrame(master=parent)
        self.label = CTkLabel(self.frame, text=todoText, width=40, anchor="w")
        self.text = todoText
        self.deleteBtn = CTkButton(self.frame, text="delete", command=self.delete)


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
root = CTk()
root.title = "todo app"
root.geometry("500x400")

#add to list button
button = CTkButton(root, text="add to list", command=addTodo)
root.bind('<Return>', KBDaddToList)

buttonFrame = CTkFrame(master=root)

exitBtn = CTkButton(root,  text="exit", command=root.destroy)

todoEntry = CTkEntry(root)


#output for todo list
displayFrame = CTkScrollableFrame(master=root)
# todoText = Text(displayFrame)

#pack everything in windows
button.pack(padx = 2, pady = 2)
exitBtn.pack(padx = 2, pady = 2)
todoEntry.pack()
displayFrame.pack()


root.mainloop()