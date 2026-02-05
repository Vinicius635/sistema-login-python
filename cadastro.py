import customtkinter as ctk
from tkinter import messagebox
import json
import os


def abrir_cadastro(janela_principal, usuarios):
    cadastro = ctk.CTkToplevel(janela_principal)
    cadastro.title("Cadastro de Usuário")
    cadastro.geometry("400x250")

    ctk.CTkLabel(cadastro, text="Novo Cadastro", font=("Arial", 18)).pack(pady=15)

    entry_novo_usuario = ctk.CTkEntry(cadastro, width=250, placeholder_text="Novo usuário")
    entry_novo_usuario.pack(pady=10)

    entry_nova_senha = ctk.CTkEntry(cadastro, width=250, show="*", placeholder_text="Nova senha")
    entry_nova_senha.pack(pady=10)

    def cadastrar():
        user = entry_novo_usuario.get().strip()
        senha = entry_nova_senha.get().strip()

        if not user or not senha:
            messagebox.showwarning("Atenção", "Preencha todos os campos.")
        elif user in usuarios:
            messagebox.showerror("Erro", "Usuário já existe.")
        else:
            usuarios[user] = senha
            messagebox.showinfo("Sucesso", "Usuário cadastrado com sucesso!")
            cadastro.destroy()

    ctk.CTkButton(cadastro, text="Cadastrar", command=cadastrar, width=250).pack(pady=20)