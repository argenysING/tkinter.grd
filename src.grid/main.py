import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()

root = tk.Tk()
root.configure(bg="gray")
root.title("Interfaz Horizontal con Grid")
root.geometry("800x400") 
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

def validar_credenciales():
    user_env = os.getenv("valor_usuario")
    pass_env = os.getenv("valor_password")

    if campo_entrada_usuario.get() == user_env and campo_entrada_password.get() == pass_env:
        lbl_info.config(text="Acceso correcto", fg="green", bg="gray")
    else:
        lbl_info.config(text="Usuario o contraseña incorrectos", fg="red", bg="gray")

# --- FILA 0: USUARIO ---
label_usuario = tk.Label(root, text="Usuario:", bg="black", fg="white", font=("Arial", 18), width=12)
label_usuario.grid(row=0, column=0, sticky="e", padx=10, pady=20) # sticky="e" (East) lo pega a la derecha

campo_entrada_usuario = tk.Entry(root, font=("Arial", 18))
campo_entrada_usuario.grid(row=0, column=1, sticky="w", padx=10, pady=20) # sticky="w" (West) lo pega a la izquierda

# --- FILA 1: CONTRASEÑA ---
label_password = tk.Label(root, text="Contraseña:", bg="black", fg="white", font=("Arial", 18), width=12)
label_password.grid(row=1, column=0, sticky="e", padx=10, pady=20)

campo_entrada_password = tk.Entry(root, font=("Arial", 18), show="*")
campo_entrada_password.grid(row=1, column=1, sticky="w", padx=10, pady=20)


boton = tk.Button(root, text="Capturar", bg="yellow", fg="black", font=("Arial", 18), command=validar_credenciales)
boton.grid(row=2, column=0, columnspan=2, pady=30, ipadx=50)

# --- FILA 3: INFO ---
lbl_info = tk.Label(root, text="", font=("Arial", 16), bg="gray")
lbl_info.grid(row=3, column=0, columnspan=2, pady=10)

root.mainloop()