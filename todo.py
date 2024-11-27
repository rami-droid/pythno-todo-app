from customtkinter import *

from tkinter import *
import pickle


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
        todos.remove(self)
        self.frame.destroy()

    def get_data(self):
        return self.text
 


def addTodo():
    todoText = todoEntry.get()
    if todoText:
        newTodo = todo(displayFrame, todoText)
        todos.append(newTodo)
        newTodo.pack()
        todoEntry.delete(0, END)


def save_todos():
    todo_texts = [todo.get_data() for todo in todos]
    with open ("todos.pickle", "wb") as file:
        pickle.dump(todo_texts, file)

def load_todos():
    try:
        with open ("todos.pickle", "rb") as file:
            todo_texts = pickle.load(file)
        for text in todo_texts:
            new_todo = todo(displayFrame, text)
            todos.append(new_todo)
            new_todo.pack()
    except FileNotFoundError:
        pass
    except EOFError:
        pass

#deletes top todo from list
def on_delete_click():
    save_todos()

todos = []

#define main window
root = CTk()
root.title = "todo app"
root.geometry("500x400")

buttonFrame = CTkFrame(master=root)

#add to list button
button = CTkButton(buttonFrame, text="add to list", command=addTodo)
root.bind('<Return>', KBDaddToList)



exitBtn = CTkButton(buttonFrame,  text="save data", command=on_delete_click)

tempBtn = CTkButton(buttonFrame, text="exit", command=root.destroy)

todoEntry = CTkEntry(root)


#output for todo list
displayFrame = CTkScrollableFrame(master=root)
# todoText = Text(displayFrame)
buttonFrame.pack()
#pack everything in windows

button.pack(padx = 2, pady = 2, side=LEFT)
exitBtn.pack(padx = 2, pady = 2, side=LEFT)
tempBtn.pack(padx = 2, pady = 2, side=LEFT)
todoEntry.pack()
displayFrame.pack()

load_todos()
root.mainloop()