import time
import sqlite3
import os

user_path = os.path.expanduser("~")
desktop_path = user_path + "\\OneDrive\\Escritorio\\"
history_path = user_path + "\\AppData\\Local\\Google\\Chrome\\User Data\\Default\\History"

urls = None
while not urls:
    try:
        # Se conecta a la base de datos de SQLite eb la ruta especificada
        connection = sqlite3.connect(history_path)
        # Se crea el objeto "cursor" para ejecutar comandos de SQLite
        cursor = connection.cursor()
        # hace una consulta SQL En la columna "title, last_visit_time y url" de la tabla urls
        # ordenado desde la ultima visita a la primera descendente
        cursor.execute("SELECT title, last_visit_time, url FROM urls ORDER BY last_visit_time DESC")
        urls = cursor.fetchall()
        for url in urls:
            print(url)

    except sqlite3.OperationalError:
        print("No podemos acceder al historial espera unos Segundos...")
        time.sleep(3)
