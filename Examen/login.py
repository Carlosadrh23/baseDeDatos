import tkinter as tk
from tkinter import messagebox
import hashlib
from o_conexion import o_conexion
from menu_principal import menu_principal

def ventana_login(raiz):
    def iniciar_sesion():
        correo = entry_correo.get().strip()
        contrasena = entry_contrasena.get().strip()

        if not correo or not contrasena:
            messagebox.showwarning("Advertencia", "Completa todos los campos")
            return

        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()
        conexion = o_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.execute(
                    "SELECT id_usuario, nombre FROM usuarios WHERE email = %s AND contrasena_hash = %s",
                    (correo, contrasena_hash)
                )
                usuario = cursor.fetchone()

                if usuario:
                    messagebox.showinfo("Éxito", f"Bienvenido {usuario[1]} 👋")
                    raiz.destroy()
                    menu_principal(usuario[1], usuario[0])
                else:
                    messagebox.showerror("Error", "Correo o contraseña incorrectos")
            except Exception as e:
                messagebox.showerror("Error", f"Ocurrió un error:\n{e}")
            finally:
                conexion.close()

    ventana = tk.Toplevel(raiz)
    ventana.title("Iniciar Sesión")
    ventana.geometry("350x250")
    ventana.config(bg="#ecf0f1")

    tk.Label(ventana, text="Correo:", bg="#ecf0f1").pack(pady=5)
    entry_correo = tk.Entry(ventana, width=30)
    entry_correo.pack()

    tk.Label(ventana, text="Contraseña:", bg="#ecf0f1").pack(pady=5)
    entry_contrasena = tk.Entry(ventana, width=30, show="*")
    entry_contrasena.pack()

    tk.Button(ventana, text="Entrar", command=iniciar_sesion, bg="#3498db", fg="white").pack(pady=15)

