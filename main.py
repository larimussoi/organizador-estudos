import tkinter as tk
from tkinter import messagebox
from data_manager import load_data, save_data
from models import Subject

subjects = load_data()

def add_subject():
    name = subject_entry.get()
    if name:
        subjects.append(Subject(name))
        listbox.insert(tk.END, name)
        subject_entry.delete(0, tk.END)
        save_data(subjects)

root = tk.Tk()
root.title("Organizador de Estudos")
root.geometry("400x300")

label = tk.Label(root, text="Insira a matéria: ")
label.pack()

subject_entry = tk.Entry(root)
subject_entry.pack()

btn_add = tk.Button(root, text="Adicionar", command=add_subject)
btn_add.pack()

listbox = tk.Listbox(root)
listbox.pack(fill=tk.BOTH, expand=True)

for subject in subjects:
    listbox.insert(tk.END, subject.name)

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
            save_data(subjects)

            messagebox.showinfo("Sucesso", "Sessão registrada!")
            popup.destroy()

        except ValueError:
            messagebox.showerror("Erro", "Insira valores válidos.")

    tk.Button(popup, text="Salvar", command=save_session).pack(pady=15)

btn_register = tk.Button(root, text="Registrar Estudo", command=open_register_window)
btn_register.pack(pady=10)

def show_summary():
    selected_index = listbox.curselection()
    
    if not selected_index:
        messagebox.showwarning("Aviso", "Selecione uma matéria primeiro.")
        return
    
    subject = subjects[selected_index[0]]
    
    total_minutes = subject.total_minutes()
    average_difficulty = subject.average_difficulty()
    total_sessions = len(subject.study_sessions)

    if total_sessions == 0:
        messagebox.showinfo("Resumo", f"Matéria: {subject.name}\nNenhuma sessão registrada.")
        return

    if average_difficulty >= 4:
        insight = "Dificuldade alta, considere revisar os conceitos."
    elif average_difficulty <= 2:
        insight = "Dificuldade baixa, continue assim!"
    else:
        insight = "Dificuldade moderada, mantenha o bom trabalho."

    summary_text = (
        f"Matéria: {subject.name}\n"
        f"Total de Sessões: {total_sessions}\n"
        f"Total de Minutos: {total_minutes}\n"
        f"Dificuldade Média: {average_difficulty:.2f}\n"
        f"Insight: {insight}"
    )

    messagebox.showinfo("Resumo", summary_text)

btn_summary = tk.Button(root, text="Ver Resumo da Matéria", command=show_summary)
btn_summary.pack(pady=5)

root.mainloop()