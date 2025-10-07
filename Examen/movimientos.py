import tkinter as tk
from tkinter import ttk, messagebox
from o_conexion import o_conexion

def ventana_movimientos():
    conexion = o_conexion()
    if not conexion:
        messagebox.showerror("Error", "No se pudo conectar a la base de datos")
        return

    ventana = tk.Toplevel()
    ventana.title("Movimientos")
    ventana.geometry("700x300")
    ventana.config(bg="#ecf0f1")

    tree = ttk.Treeview(
        ventana,
        columns=("ID", "Tipo", "Monto", "Emisora", "Receptora", "Fecha", "Nota"),
        show="headings"
    )
    tree.pack(fill=tk.BOTH, expand=True)

    for col in ("ID", "Tipo", "Monto", "Emisora", "Receptora", "Fecha", "Nota"):
        tree.heading(col, text=col)
        tree.column(col, width=100)

    try:
        cursor = conexion.cursor()
        cursor.execute("SELECT * FROM movimientos ORDER BY fecha_operacion DESC")
        for fila in cursor.fetchall():
            tree.insert("", tk.END, values=fila)
    except Exception as e:
        messagebox.showerror("Error", f"No se pudieron cargar los movimientos:\n{e}")
    finally:
        conexion.close()
