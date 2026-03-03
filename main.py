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

def open_register_window():
    selected_index = listbox.curselection()
    
    if not selected_index:
        messagebox.showwarning("Aviso", "Selecione uma matéria primeiro.")
        return
    
    subject = subjects[selected_index[0]]

    popup = tk.Toplevel(root)
    popup.title(f"Registrar Estudo - {subject.name}")
    popup.geometry("300x250")

    tk.Label(popup, text="Minutos estudados:").pack(pady=5)
    entry_minutes = tk.Entry(popup)
    entry_minutes.pack()

    tk.Label(popup, text="Dificuldade (1-5):").pack(pady=5)
    entry_difficulty = tk.Entry(popup)
    entry_difficulty.pack()

    def save_session():
        try:
            minutes = int(entry_minutes.get())
            difficulty = int(entry_difficulty.get())

            if difficulty < 1 or difficulty > 5:
                raise ValueError

            subject.add_session(minutes, difficulty)

            messagebox.showinfo("Sucesso", "Sessão registrada!")
            popup.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    tk.Button(popup, text="Salvar", command=save_session).pack(pady=15)

btn_register = tk.Button(root, text="Registrar Estudo", command=open_register_window)
btn_register.pack(pady=10)

root.mainloop()