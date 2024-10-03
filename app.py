import tkinter as tk
from tkinter import messagebox
from tkinter import simpledialog

root = tk.Tk()
root.title("To-Do List")
root.geometry("700x670")
root.config(bg="#f2f2f2")

# Task list to store tasks
tasks = []

# To update the task list
def update_task_list():
    task_listbox.delete(0, tk.END)
    for task, completed in tasks:
        status = "✓" if completed else "✗"
        task_color = "#78e08f" if completed else "white"  
        task_listbox.insert(tk.END, f"{status} {task}")
        task_listbox.itemconfig(tk.END, {'bg': task_color})
    update_status_bar()

# To update the status bar
def update_status_bar():
    total_tasks = len(tasks)
    completed_tasks = len([task for task in tasks if task[1]])
    pending_tasks = total_tasks - completed_tasks
    status_var.set(f"Pending: {pending_tasks}, Completed: {completed_tasks}, Total: {total_tasks}")

# Fo add a new task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append([task, False])  
        update_task_list()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

# To delete the selected task
def delete_task():
    try:
        task_index = task_listbox.curselection()[0]
        tasks.pop(task_index)
        update_task_list()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

# To clear all tasks
def clear_tasks():
    global tasks
    tasks = []
    update_task_list()

# To toggle the completion status of the selected task
def toggle_task_status():
    try:
        task_index = task_listbox.curselection()[0]
        tasks[task_index][1] = not tasks[task_index][1]
        update_task_list()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to toggle status.")

# To edit the selected task
def edit_task():
    try:
        task_index = task_listbox.curselection()[0]
        current_task = tasks[task_index][0]
        new_task = simpledialog.askstring("Edit Task", f"Edit task: {current_task}")
        if new_task:
            tasks[task_index][0] = new_task
            update_task_list()
    except:
        messagebox.showwarning("Selection Error", "Please select a task to edit.")

# Scrollbar for the listbox
scrollbar = tk.Scrollbar(root)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# GUI layout
task_entry = tk.Entry(root, width=30, font=("monaco", 10), bd=3)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", command=add_task, bg="#6a89cc", fg="white", font=("monaco", 10), bd=3)
add_button.pack(pady=5)

task_listbox = tk.Listbox(root, height=15, width=50, bg="light pink", font=("monaco", 12), yscrollcommand=scrollbar.set)
task_listbox.pack(pady=10)
scrollbar.config(command=task_listbox.yview)

# Button layout
toggle_button = tk.Button(root, text="Toggle Task Status", command=toggle_task_status, bg="#6a89cc", fg="white", font=("monaco", 10), bd=3)
toggle_button.pack(pady=5)

edit_button = tk.Button(root, text="Edit Task", command=edit_task, bg="#6a89cc", fg="white", font=("monaco", 10), bd=3)
edit_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task, bg="#6a89cc", fg="white", font=("monaco", 10), bd=3)

delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_tasks, bg="#6a89cc", fg="white", font=("monaco", 10), bd=3)
clear_button.pack(pady=5)

# Status bar
status_var = tk.StringVar()
status_bar = tk.Label(root, textvariable=status_var, font=("Helvetica", 10), bd=2, relief=tk.SUNKEN, anchor=tk.W)
status_bar.pack(side=tk.BOTTOM, fill=tk.X)
update_status_bar()

# Start the GUI event loop
root.mainloop()
