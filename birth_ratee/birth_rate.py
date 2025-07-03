import tkinter as tk
from tkinter import messagebox

def calcular_taxa():
    try:
        nascimentos = int(entry_nascimentos.get())
        populacao = int(entry_populacao.get())

        if populacao <= 0:
            messagebox.showerror("Erro", "A população deve ser maior que zero.")
            return

        taxa = (nascimentos / populacao) * 1000
        resultado_var.set(f"Taxa de natalidade: {taxa:.2f} por mil habitantes")

    except ValueError:
        messagebox.showerror("Erro", "Insira apenas números inteiros.")

#INTERFACE

janela = tk.Tk()
janela.title("Calculadora de Taxa de Natalidade")
janela.geometry("400x250")
janela.configure(bg="#00aaff")

tk.Label(janela, text="Nascimentos:", bg="#00aaff").pack(pady=5)
entry_nascimentos = tk.Entry(janela)
entry_nascimentos.pack()

tk.Label(janela, text="População total:", bg="#00aaff").pack(pady=5)
entry_populacao = tk.Entry(janela)
entry_populacao.pack()

tk.Button(janela, text="Calcular", command=calcular_taxa, bg="#00aaff", fg="white").pack(pady=10)

resultado_var = tk.StringVar()
tk.Label(janela, textvariable=resultado_var, bg="#00aaff", font=("Arial", 12, "bold")).pack(pady=10)

janela.mainloop()
