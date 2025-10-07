import tkinter as tk
from abrir_cuenta import ventana_abrir_cuenta
from transferir import ventana_transferir
from movimientos import ventana_movimientos

def menu_principal(nombre_usuario, id_usuario):
    ventana = tk.Tk()
    ventana.title("Menú ")
    ventana.geometry("400x350")
    ventana.config(bg="#ecf0f1")

    tk.Label(
        ventana,
        text=f"Bienvenido, {nombre_usuario} ",
        font=("Arial", 14, "bold"),
        bg="#ecf0f1"
    ).pack(pady=20)

    tk.Button(ventana, text="Abrir Cuenta", command=lambda: ventana_abrir_cuenta(id_usuario),
              bg="#3498db", fg="white", width=20).pack(pady=5)

    tk.Button(ventana, text="Transferir Dinero", command=ventana_transferir,
              bg="#f1c40f", fg="white", width=20).pack(pady=5)

    tk.Button(ventana, text="Ver Movimientos", command=ventana_movimientos,
              bg="#9b59b6", fg="white", width=20).pack(pady=5)

    tk.Button(ventana, text="Cerrar Sesión", command=ventana.destroy,
              bg="#e74c3c", fg="white", width=20).pack(pady=15)

    ventana.mainloop()
