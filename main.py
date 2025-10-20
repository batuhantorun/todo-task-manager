# main.py

import tkinter as tk
from tkinter import messagebox, simpledialog
import json
import os

# JSON dosyası
DATA_FILE = "tasks.json"

# Görevleri yükle
def load_tasks():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return []

# Görevleri kaydet
def save_tasks():
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Görev ekle
def add_task():
    title = simpledialog.askstring("Add Task", "Enter task title:")
    if title:
        description = simpledialog.askstring("Add Task", "Enter task description:")
        tasks.append({"title": title, "description": description, "completed": False})
        save_tasks()
        update_listbox()

# Görev sil
def delete_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks.pop(idx)
        save_tasks()
        update_listbox()
    else:
        messagebox.showwarning("Delete Task", "No task selected!")

# Görev düzenle
def edit_task():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        task = tasks[idx]
        title = simpledialog.askstring("Edit Task", "Edit task title:", initialvalue=task["title"])
        if title:
            description = simpledialog.askstring("Edit Task", "Edit task description:", initialvalue=task["description"])
            task["title"] = title
            task["description"] = description
            save_tasks()
            update_listbox()
    else:
        messagebox.showwarning("Edit Task", "No task selected!")

# Görev tamamlandı işareti
def toggle_complete():
    selected = listbox.curselection()
    if selected:
        idx = selected[0]
        tasks[idx]["completed"] = not tasks[idx]["completed"]
        save_tasks()
        update_listbox()
    else:
        messagebox.showwarning("Complete Task", "No task selected!")

# Listbox güncelle
def update_listbox():
    listbox.delete(0, tk.END)
    for task in tasks:
        status = "✔️" if task["completed"] else "❌"
        listbox.insert(tk.END, f"{status} {task['title']} - {task['description']}")

# Ana pencere
root = tk.Tk()
root.title("To-Do Task Manager")

# Görev listesi
tasks = load_tasks()
listbox = tk.Listbox(root, width=50)
listbox.pack(pady=10)

# Butonlar
frame = tk.Frame(root)
frame.pack(pady=5)

tk.Button(frame, text="Add Task", command=add_task, width=12).grid(row=0, column=0, padx=5)
tk.Button(frame, text="Edit Task", command=edit_task, width=12).grid(row=0, column=1, padx=5)
tk.Button(frame, text="Delete Task", command=delete_task, width=12).grid(row=0, column=2, padx=5)
tk.Button(frame, text="Toggle Complete", command=toggle_complete, width=12).grid(row=0, column=3, padx=5)

# Başlat
update_listbox()
root.mainloop()
