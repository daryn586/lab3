import tkinter as tk

def encrypt_text():
    text = input_text.get("1.0", "end").strip().replace(" ", "").upper()
    key_order = [2, 0, 3, 1]  # Кілт: 3-1-4-2
    encrypted_text = process_text(text, key_order)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", encrypted_text)

def decrypt_text():
    text = input_text.get("1.0", "end").strip().replace(" ", "").upper()
    reverse_key_order = [1, 3, 0, 2]  # Дешифрлау кілті
    decrypted_text = process_text(text, reverse_key_order)
    output_text.delete("1.0", "end")
    output_text.insert("1.0", decrypted_text)

def process_text(text, key_order):
    processed_text = ""

    # Толтыру үшін 'X' қосу (тек шифрлау кезінде қажет)
    if len(text) % 4 != 0:
        text += "X" * (4 - len(text) % 4)

    # 4 таңбадан тұратын топтарға бөлу және орын ауыстыру
    for i in range(0, len(text), 4):
        group = text[i:i + 4]
        new_group = ''.join([group[j] for j in key_order])
        processed_text += new_group

    return processed_text

# Графикалық интерфейс құру
root = tk.Tk()
root.title("Қарапайым орын ауыстыру шифры")

# Жазба енгізу аймағы
tk.Label(root, text="Мәтінді енгізіңіз:").pack()
input_text = tk.Text(root, height=5, width=40)
input_text.pack()

# Нәтиже көрсету аймағы
tk.Label(root, text="Нәтиже:").pack()
output_text = tk.Text(root, height=5, width=40, state="normal")
output_text.pack()

# Батырмалар
encrypt_button = tk.Button(root, text="Шифрлау", command=encrypt_text)
encrypt_button.pack()

decrypt_button = tk.Button(root, text="Дешифрлау", command=decrypt_text)
decrypt_button.pack()

# Бағдарламаны іске қосу
root.mainloop()
