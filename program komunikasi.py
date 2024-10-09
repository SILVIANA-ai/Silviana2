import tkinter as tk
from tkinter import scrolledtext

# Fungsi untuk enkripsi menggunakan Caesar Cipher
def encrypt(text, shift):
    result = "\nProses Enkripsi:\n"
    encrypted_text = ""
    
    for char in text:
        if char.isupper():
            shifted = (ord(char) + shift - 65) % 26 + 65
            encrypted_text += chr(shifted)
            result += f"{char} -> {chr(shifted)}\n"
        elif char.islower():
            shifted = (ord(char) + shift - 97) % 26 + 97
            encrypted_text += chr(shifted)
            result += f"{char} -> {chr(shifted)}\n"
        else:
            encrypted_text += char
            result += f"{char} tetap -> {char}\n"
    
    return result, encrypted_text

# Fungsi untuk dekripsi menggunakan Caesar Cipher
def decrypt(text, shift):
    result = "\nProses Dekripsi:\n"
    decrypted_text = ""
    
    for char in text:
        if char.isupper():
            shifted = (ord(char) - shift - 65) % 26 + 65
            decrypted_text += chr(shifted)
            result += f"{char} -> {chr(shifted)}\n"
        elif char.islower():
            shifted = (ord(char) - shift - 97) % 26 + 97
            decrypted_text += chr(shifted)
            result += f"{char} -> {chr(shifted)}\n"
        else:
            decrypted_text += char
            result += f"{char} tetap -> {char}\n"
    
    return result, decrypted_text

# Fungsi untuk memproses pengiriman pesan dari Pengirim
def send_message():
    plaintext = entry_text.get()
    shift = int(entry_shift.get())
    
    console_output.delete(1.0, tk.END)
    
    # Pengirim Enkripsi Pesan
    console_output.insert(tk.END, f"Pengirim mengirim pesan: {plaintext}\n")
    encryption_process, encrypted_text = encrypt(plaintext, shift)
    console_output.insert(tk.END, encryption_process)
    console_output.insert(tk.END, f"Hasil Enkripsi (Ciphertext yang dikirim ke Penerima): {encrypted_text}\n")
    
    # Dekripsi pesan
    decryption_process, decrypted_text = decrypt(encrypted_text, shift)
    console_output.insert(tk.END, decryption_process)
    console_output.insert(tk.END, f"Hasil Dekripsi (Pesan asli yang diterima): {decrypted_text}\n")
    
    # Menampilkan label input balasan di bawah proses pesan pengirim
    label_reply.pack(fill='x', pady=5)
    entry_reply.pack(fill='x', pady=5)
    button_reply.pack(fill='x', pady=5)

# Fungsi untuk memproses balasan dari Penerima
def reply_message():
    reply_plaintext = entry_reply.get()
    shift = int(entry_shift.get())
    
    # Menampilkan pesan balasan di text box baru
    reply_output.delete(1.0, tk.END)
    reply_output.insert(tk.END, f"Penerima membalas: {reply_plaintext}\n")
    
    # Enkripsi pesan balasan
    reply_encryption_process, reply_encrypted_text = encrypt(reply_plaintext, shift)
    reply_output.insert(tk.END, reply_encryption_process)
    reply_output.insert(tk.END, f"Hasil Enkripsi Balasan (Ciphertext yang dikirim ke Pengirim): {reply_encrypted_text}\n")
    
    # Dekripsi pesan balasan
    reply_decryption_process, reply_decrypted_text = decrypt(reply_encrypted_text, shift)
    reply_output.insert(tk.END, reply_decryption_process)
    reply_output.insert(tk.END, f"Hasil Dekripsi Balasan (Pesan asli yang diterima oleh Pengirim): {reply_decrypted_text}\n")

# Setup GUI dengan tkinter
window = tk.Tk()
window.title("Komunikasi Dua Arah")

# Label dan entry untuk input nilai shift
label_shift = tk.Label(window, text="Masukkan nilai shift (kunci):")
label_shift.pack(fill='x', pady=5)

entry_shift = tk.Entry(window, width=5)
entry_shift.pack(fill='x', pady=5)

# Label dan entry untuk input pesan dari Pengirim
label_text = tk.Label(window, text="Masukkan pesan dari Pengirim:")
label_text.pack(fill='x', pady=5)

entry_text = tk.Entry(window, width=50)
entry_text.pack(fill='x', pady=5)

# Tombol untuk mengirim pesan
button_send = tk.Button(window, text="Kirim Pesan", command=send_message)
button_send.pack(fill='x', pady=5)

# Text box untuk menampilkan hasil output pengirim
console_output = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, bg='black', fg='white', font=("Consolas", 10))
console_output.pack(fill='x', pady=5)

# Label dan entry untuk input balasan dari Penerima (sembunyikan terlebih dahulu)
label_reply = tk.Label(window, text="Masukkan pesan balasan dari Penerima:")
entry_reply = tk.Entry(window, width=50)
button_reply = tk.Button(window, text="Kirim Balasan", command=reply_message)

# Menampilkan label input balasan di bawah proses pesan pengirim
label_reply.pack(fill='x', pady=5)
entry_reply.pack(fill='x', pady=5)
button_reply.pack(fill='x', pady=5)

# Text box untuk menampilkan hasil output balasan
reply_output = scrolledtext.ScrolledText(window, wrap=tk.WORD, width=50, height=10, bg='black', fg='white', font=("Consolas", 10))
reply_output.pack(fill='x', pady=5)

# Menjalankan aplikasi
window.mainloop()
