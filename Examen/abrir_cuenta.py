import tkinter as tk
from tkinter import messagebox
from o_conexion import o_conexion

def ventana_abrir_cuenta(id_usuario):
    def abrir():
        saldo = entry_saldo.get()
        if not saldo:
            messagebox.showwarning("Advertencia", "Ingresa un saldo inicial")
            return

        try:
            saldo = float(saldo)
        except ValueError:
            messagebox.showerror("Error", "El saldo debe ser numérico")
            return

        conexion = o_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.callproc("abrir_cuenta", (id_usuario, saldo))
                conexion.commit()
                messagebox.showinfo("Éxito", "Cuenta abierta correctamente ✅")
                ventana.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error:\n{e}")
            finally:
                conexion.close()

    ventana = tk.Toplevel()
    ventana.title("Abrir Cuenta")
    ventana.geometry("300x200")
    ventana.config(bg="#ecf0f1")

    tk.Label(ventana, text="Saldo inicial:", bg="#ecf0f1").pack(pady=10)
    entry_saldo = tk.Entry(ventana, width=25)
    entry_saldo.pack()

    tk.Button(ventana, text="Abrir cuenta", command=abrir, bg="#27ae60", fg="white").pack(pady=20)
