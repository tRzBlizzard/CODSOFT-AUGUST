import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_listbox.itemconfig(tk.END, {'bg': 'lightgreen'})
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def remove_task():
    try:
        selected_task_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_task_index)
    except IndexError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.geometry("600x600") 

task_entry = tk.Entry(root, width=40, bg='lightblue')
task_entry.pack(pady=10)

task_listbox = tk.Listbox(root, selectmode=tk.SINGLE, width=40, height=10, bg='lightyellow')
task_listbox.pack()

add_button = tk.Button(root, text="Add Task", command=add_task, bg='lightgreen')
add_button.pack(pady=5)
add_button.config(relief=tk.RAISED)
add_button.bind('<Enter>', lambda e: add_button.config(relief=tk.SUNKEN))
add_button.bind('<Leave>', lambda e: add_button.config(relief=tk.RAISED))

remove_button = tk.Button(root, text="Remove Task", command=remove_task, bg='lightcoral')
remove_button.pack()
remove_button.config(relief=tk.RAISED)
remove_button.bind('<Enter>', lambda e: remove_button.config(relief=tk.SUNKEN))
remove_button.bind('<Leave>', lambda e: remove_button.config(relief=tk.RAISED))

root.mainloop()
