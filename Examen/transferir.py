import tkinter as tk
from tkinter import messagebox
from o_conexion import o_conexion

def ventana_transferir():
    def transferir():
        origen = entry_origen.get()
        destino = entry_destino.get()
        monto = entry_monto.get()

        if not origen or not destino or not monto:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return

        conexion = o_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.callproc("transferir", (int(origen), int(destino), float(monto)))
                conexion.commit()
                messagebox.showinfo("Éxito", "Transferencia realizada ✅")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error:\n{e}")
            finally:
                conexion.close()

    ventana = tk.Toplevel()
    ventana.title("Transferir Dinero")
    ventana.geometry("350x250")
    ventana.config(bg="#ecf0f1")

    tk.Label(ventana, text="Cuenta origen (ID):", bg="#ecf0f1").pack(pady=5)
    entry_origen = tk.Entry(ventana, width=25)
    entry_origen.pack()

    tk.Label(ventana, text="Cuenta destino (ID):", bg="#ecf0f1").pack(pady=5)
    entry_destino = tk.Entry(ventana, width=25)
    entry_destino.pack()

    tk.Label(ventana, text="Monto:", bg="#ecf0f1").pack(pady=5)
    entry_monto = tk.Entry(ventana, width=25)
    entry_monto.pack()

    tk.Button(ventana, text="Transferir", command=transferir, bg="#2980b9", fg="white").pack(pady=15)
