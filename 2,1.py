import tkinter as tk
from tkinter import messagebox

def шифрлау():
    мәтін = entry_text.get("1.0", "end-1c").replace(" ", "").upper()
    rows = int(entry_rows.get())
    cols = int(entry_cols.get())
    
    if len(мәтін) > rows * cols:
        messagebox.showerror("Қате", "Мәтін өте ұзын! Кестенің өлшемі жеткіліксіз.")
        return

    кесте = [["" for _ in range(cols)] for _ in range(rows)]
    
    # Кестеге бағандар бойынша мәтінді жазамыз
    idx = 0
    for col in range(cols):
        for row in range(rows):
            if idx < len(мәтін):
                кесте[row][col] = мәтін[idx]
                idx += 1

    # Жолдар бойынша оқып, шифрланған мәтінді аламыз
    шифрланған_мәтін = ""
    for row in range(rows):
        for col in range(cols):
            шифрланған_мәтін += кесте[row][col]
    
    # Нәтижені шығару
    result_text.delete("1.0", "end")
    result_text.insert("1.0", шифрланған_мәтін)

def дешифрлау():
    шифрланған_мәтін = entry_text.get("1.0", "end-1c").replace(" ", "").upper()
    rows = int(entry_rows.get())
    cols = int(entry_cols.get())
    
    if len(шифрланған_мәтін) > rows * cols:
        messagebox.showerror("Қате", "Мәтін өте ұзын! Кестенің өлшемі жеткіліксіз.")
        return

    кесте = [["" for _ in range(cols)] for _ in range(rows)]
    
    # Кестеге жолдар бойынша мәтінді жазамыз
    idx = 0
    for row in range(rows):
        for col in range(cols):
            if idx < len(шифрланған_мәтін):
                кесте[row][col] = шифрланған_мәтін[idx]
                idx += 1

    # Бағандар бойынша оқып, бастапқы мәтінді аламыз
    дешифрланған_мәтін = ""
    for col in range(cols):
        for row in range(rows):
            дешифрланған_мәтін += кесте[row][col]

    # Нәтижені шығару
    result_text.delete("1.0", "end")
    result_text.insert("1.0", дешифрланған_мәтін)

# Пайдаланушы интерфейсін құру
root = tk.Tk()
root.title("Бағандық шифр")

# Мәтін енгізу
tk.Label(root, text="Мәтінді енгізіңіз:").grid(row=0, column=0)
entry_text = tk.Text(root, width=30, height=5)
entry_text.grid(row=0, column=1)

# Жол және баған санын енгізу
tk.Label(root, text="Жол саны:").grid(row=1, column=0)
entry_rows = tk.Entry(root)
entry_rows.grid(row=1, column=1)

tk.Label(root, text="Баған саны:").grid(row=2, column=0)
entry_cols = tk.Entry(root)
entry_cols.grid(row=2, column=1)

# Шифрлау және дешифрлау батырмалары
tk.Button(root, text="Шифрлау", command=шифрлау).grid(row=3, column=0)
tk.Button(root, text="Дешифрлау", command=дешифрлау).grid(row=3, column=1)

# Нәтижені көрсету
tk.Label(root, text="Нәтиже:").grid(row=4, column=0)
result_text = tk.Text(root, width=30, height=5)
result_text.grid(row=4, column=1)

# Терезені іске қосу
root.mainloop()
