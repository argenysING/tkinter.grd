import tkinter as tk
from dotenv import load_dotenv
import os

load_dotenv()

root = tk.Tk()
root.configure(bg="gray")
root.title("mi primera aplicacion con tkinter")
root.geometry("500x600")

def capturar_Valores():
    valor_usuario = campo_entrada_usuario.get()
    valor_password = campo_entrada_password.get()
   

    user_env = os.getenv("valor_usuario")
    pass_env = os.getenv("valor_password")
    print(user_env, pass_env)

def validar_credenciales():
    user_env = os.getenv("valor_usuario")
    pass_env = os.getenv("valor_password")

    if campo_entrada_usuario.get() == user_env and campo_entrada_password.get() == pass_env:
        lbl_info.config(text="Acceso correcto", fg="green")
    else:
        lbl_info.config(text="usuario o contraseña incorrectos", fg="red")


label_usuario = tk.Label(root, text="usuario",bg="black", fg="white", font=("Arial", 24))
label_usuario.grid(row=0, column=0, padx=10, pady=10)

campo_entrada_usuario = tk.Entry(root, font=("Arial", 18))
campo_entrada_usuario.grid(row=1, column=0, padx=10, pady=10)

label_password = tk.Label(root, text="contraseña",bg="black", fg="white", font=("Arial", 24))
label_password.grid(row=2, column=0, padx=10, pady=10)

campo_entrada_password = tk.Entry(root, font=("Arial", 18), show="*")
campo_entrada_password.grid(row=3, column=0, padx=10, pady=10)

boton = tk.Button(root, text="capturar",bg="yellow", fg="black", font=("Arial", 18), command=validar_credenciales)
boton.grid(row=4, column=0, pady=20)

lbl_info = tk.Label(root, text="", font=("Arial", 18))
lbl_info.grid(row=5, column=0,  pady=20)

root.mainloop()