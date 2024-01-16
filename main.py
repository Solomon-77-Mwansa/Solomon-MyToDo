import tkinter
from tkinter import *
import os
import fileinput

root = Tk()
root.title("To-Do-List")
root.geometry("400x600+400+100")
root.resizable(False, False)
root.config(bg="white")

task_list = []

def deleteTask():
    global task_list
    for task in task_list:
        task_list.remove(task)
        with open("file_tasks/textlist.txt", 'w') as taskfile:
            for task in task_list:
                taskfile.write(task+'\n')

        listbox.delete( ANCHOR)
        
    

def AddTask():
    task = task_entry.get()
    task_entry.delete(0, END)

    if task:
        with open("file_tasks/textlist.txt", 'a') as taskfile:
            taskfile.write(f"\n{task}")
        task_list.append(task)
        listbox.insert(END, task)

def openTaskFile():

    try:
        with open("file_tasks/textlist.txt") as taskfile:
            tasks = taskfile.readlines()

            for task in tasks:
                if task != "\n":
                    task_list.append(task)
                    listbox.insert(END, task)
    except:
        file=open("file_tasks/tasklist.txt", "w")
        file.close()

def Open():
    '''new_file = ".txt"
    file = "file_tasks/.txt"'''
    
    os.startfile("file_tasks")

def createNew():
    fileinput.input("file_tasks/textlist.txt")
    fileinput.FileInput("file_tasks/textlist.txt")
        
def About():
    os.startfile("about_doc/a_bout.txt")
        
#icon
icon_image=PhotoImage(file="Image/task.png")
root.iconphoto(False, icon_image)

#menubar
menubar = tkinter.Menu(root) #create a menu bar
root.config(menu = menubar)  #assign the menu bar to the root window


#filemenu on topbar
filemenu = tkinter.Menu(menubar, tearoff=0) #create a filesubmenu
filemenu.add_command(label="New File",command=createNew  ) #add a command to the filemenu
filemenu.add_command(label="Open", command=Open ) #add another command to filemenu
filemenu.add_separator() # add a seperator line to the filemenu
filemenu.add_command(label="Exit", command=root.destroy) # add a command exit to exit/end the program
menubar.add_cascade(label="File", menu=filemenu) # add the file submenu to the menu bar


#helpmenu
helpmenu = tkinter.Menu(menubar, tearoff=0) # create a healp submenu
helpmenu.add_command(label="About", command=About) # add a command to the help submenu
menubar.add_cascade(label="Help", menu=helpmenu) # add the help submenu

#Edit/Tools
toolmenu = tkinter.Menu(menubar, tearoff=1)
toolmenu.add_command(label="Tools")
menubar.add_cascade(label="Tools", menu=toolmenu)

#frame
frame = Frame(root, width=400, height=100, bg="white")
frame.place(x=0, y=0)

task=StringVar
task_entry=Entry(frame,width=40, font="ariel 12", bd=0.0)
task_entry.place(x=10, y=10)
task_entry.focus()

button=Button(frame, text="ADD", bg="gray", bd=0, command=AddTask)
button.place(x=170, y=60)

#listbox
frame1=Frame(root, bd=2, width=700, height=280, bg="#32405b")
frame1.pack(pady=(110, 0))

listbox=Listbox(frame1, font=("ariel", 14),width=40,height=16,bg="#32405b", fg="white", cursor="hand2", selectbackground="gray")
listbox.pack(side=LEFT, fill=BOTH, padx=1)
scrollbar=Scrollbar(frame1)
scrollbar.pack( side=RIGHT, fill=BOTH)

listbox.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=listbox.yview)

openTaskFile()
#Delete
delete_icon= PhotoImage(file="Image/delete.png")
Button(root, image=delete_icon, bd=0, command=deleteTask).pack(side=BOTTOM, pady=13)
