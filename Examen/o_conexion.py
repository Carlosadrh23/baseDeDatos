
import mysql.connector

def o_conexion():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="fintech_user",
            password="1234",
            database="fintech_db",
            port=3306
        )
        return conexion
    except mysql.connector.Error as err:
        print(f" Error de conexión: {err}")
        return None
