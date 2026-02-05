import customtkinter as ctk
from cadastro import abrir_cadastro
from tkinter import messagebox
import json
import os

# Função para carregar usuários do arquivo
def carregar_usuarios():
    if os.path.exists("usuarios.json"):
        with open("usuarios.json", "r") as f:
            return json.load(f)
    return {}

# Banco de usuários (em memória)
usuarios = {}

# Função de login
def fazer_login(usuario_entry, senha_entry):
    usuario = usuario_entry.get().strip()
    senha = senha_entry.get().strip()

    # 🔁 Recarrega os dados do JSON toda vez
    usuarios = carregar_usuarios()

    if usuario in usuarios and usuarios[usuario] == senha:
        messagebox.showinfo("Login", "Login bem-sucedido!")
    else:
        messagebox.showerror("Erro", "Usuário ou senha incorretos.")

# Inicializa a interface
def iniciar_login():
    ctk.set_appearance_mode("dark")
    ctk.set_default_color_theme("blue")

    app = ctk.CTk()
    app.title("Login")
    app.geometry("400x300")

    ctk.CTkLabel(app, text="Área de Login", font=("Arial", 20)).pack(pady=20)

    entry_usuario = ctk.CTkEntry(app, width=250, placeholder_text="Usuário")
    entry_usuario.pack(pady=10)

    entry_senha = ctk.CTkEntry(app, width=250, show="*", placeholder_text="Senha")
    entry_senha.pack(pady=10)

    ctk.CTkButton(app, text="Entrar",
                  command=lambda: fazer_login(entry_usuario, entry_senha),
                  width=250).pack(pady=15)

    ctk.CTkButton(app, text="Cadastrar",
                  fg_color="gray", hover_color="#444",
                  command=lambda: abrir_cadastro(app, usuarios),
                  width=250).pack()

    app.mainloop()

if __name__ == "__main__":
    iniciar_login()