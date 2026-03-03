import tkinter as tk
from tkinter import messagebox
from models import Subject

subjects = []

def add_subject():
    name = subject_entry.get()
    if name:
        subjects.append(Subject(name))
        listbox.insert(tk.END, name)
        subject_entry.delete(0, tk.END)

root = tk.Tk()
root.title("Study Tracker")
root.geometry("400x300")

label = tk.Label(root, text="Enter Subject:")
label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

btn_add = tk.Button(root, text="Adicionar", command=add_subject)
btn_add.pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

root.mainloop()