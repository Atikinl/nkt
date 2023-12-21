import tkinter as tk
import sqlite3

root = tk.Tk()
root.title("Поиск компьютера")

conn = sqlite3.connect('db.db')
c = conn.cursor()

def search_computer():
    pc_id = pc_id_entry.get()
    c.execute("SELECT * FROM Computers WHERE Id_pc=?", (pc_id,))
    pc = c.fetchone()
    if pc:
        result_label.config(text=f"Найден компьютер: {pc}")
    else:
        result_label.config(text="Компьютер не найден")

root.geometry("500x300")
root.configure(bg='lightgrey')

pc_id_label = tk.Label(root, text="ID компьютера:", bg='lightgrey')
pc_id_entry = tk.Entry(root)
search_button = tk.Button(root, text="Найти", command=search_computer)
result_label = tk.Label(root, text="", bg='lightgrey')

pc_id_label.pack(pady=10)
pc_id_entry.pack()
search_button.pack(pady=10)
result_label.pack()

root.mainloop()
