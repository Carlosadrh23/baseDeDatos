import tkinter as tk
from tkinter import messagebox
import mysql.connector
import hashlib
from o_conexion import o_conexion
from menu_principal import menu_principal

def ventana_registro():
    ventana = tk.Tk()
    ventana.title("Registro de Usuario")
    ventana.geometry("400x400")
    ventana.config(bg="#ecf0f1")

    tk.Label(ventana, text="Registro", font=("Arial", 16, "bold"), bg="#ecf0f1").pack(pady=10)

    tk.Label(ventana, text="Email:", bg="#ecf0f1").pack()
    entry_email = tk.Entry(ventana, width=30)
    entry_email.pack(pady=5)

    tk.Label(ventana, text="Nombre:", bg="#ecf0f1").pack()
    entry_nombre = tk.Entry(ventana, width=30)
    entry_nombre.pack(pady=5)

    tk.Label(ventana, text="Apellidos:", bg="#ecf0f1").pack()
    entry_apellidos = tk.Entry(ventana, width=30)
    entry_apellidos.pack(pady=5)

    tk.Label(ventana, text="Contraseña:", bg="#ecf0f1").pack()
    entry_contrasena = tk.Entry(ventana, show="*", width=30)
    entry_contrasena.pack(pady=5)

    def registrar():
        email = entry_email.get().strip()
        nombre = entry_nombre.get().strip()
        apellidos = entry_apellidos.get().strip()
        contrasena = entry_contrasena.get().strip()

        if not email or not nombre or not apellidos or not contrasena:
            messagebox.showerror("Error", "Todos los campos son obligatorios")
            return

        contrasena_hash = hashlib.sha256(contrasena.encode()).hexdigest()
        conexion = o_conexion()
        if conexion:
            try:
                cursor = conexion.cursor()
                cursor.callproc('registrar_usuario', (email, nombre, apellidos, contrasena_hash))
                conexion.commit()


                cursor.execute("SELECT id_usuario FROM usuarios WHERE email = %s", (email,))
                id_usuario = cursor.fetchone()[0]

                messagebox.showinfo("Éxito", "Usuario registrado correctamente ")
                ventana.destroy()


                menu_principal(nombre, id_usuario)

            except mysql.connector.Error as err:
                if "Email ya registrado" in str(err):
                    messagebox.showerror("Error", "Este correo ya está registrado. Usa otro o inicia sesión.")
                else:
                    messagebox.showerror("Error", f"Ocurrió un error: {err}")
            finally:
                cursor.close()
                conexion.close()

    tk.Button(ventana, text="Registrar", command=registrar, bg="#27ae60", fg="white", width=20).pack(pady=15)
    tk.Button(ventana, text="Cancelar", command=ventana.destroy, bg="#e74c3c", fg="white", width=20).pack(pady=5)
    ventana.mainloop()
