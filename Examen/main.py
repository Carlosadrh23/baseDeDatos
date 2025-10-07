import tkinter as tk
from login import ventana_login
from registro import ventana_registro

def main():
    raiz = tk.Tk()

    raiz.geometry("400x300")
    raiz.config(bg="#ecf0f1")

    tk.Label(
        raiz,
        text="Bienvenido",
        font=("Arial", 14, "bold"),
        bg="#ecf0f1"
    ).pack(pady=30)

    tk.Button(raiz, text="Iniciar Sesión", command=lambda: ventana_login(raiz),
              width=20, bg="#3498db", fg="white").pack(pady=10)

    tk.Button(raiz, text="Registrarse", command=ventana_registro,
              width=20, bg="#2ecc71", fg="white").pack(pady=10)

    tk.Button(raiz, text="Salir", command=raiz.destroy,
              width=20, bg="#e74c3c", fg="white").pack(pady=20)

    raiz.mainloop()

if __name__ == "__main__":
    main()

