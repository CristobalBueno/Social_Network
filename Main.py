# DESAFIO 7: RED SOCIAL. LA INTERFAZ
# Imagina y diseña tu propia red social. Decide qué grado de interacción vas a permitir a los usuarios y
# diseña el esquema de la misma
# Utiliza sqlite3 para crear una conexión a la base de datos de la red social y crea las tablas que sean necesarias
# Crea la interfaz con la que interaccionarán los usuarios. Ésta debe permitir que se introduzcan datos o
# información por parte de los usuarios
# Utiliza la opción de checkbuttons para permitir la interacción de un usuario con la información generada por otro
# Programa que se vaya almacenando en la base de datos la información generada por los usuarios
# Crea la interfaz de forma que muestre la información mínima necesaria para interaccionar.
# Simula la actividad de 3 usuarios en tu red social de forma que quede recogido en la base de datos.

# PUNTUACIÓN:
# 2 PTOS - Creación de la base de datos, esquema coherente, 4 tablas como mínimo
# 2 PTOS - Creación de la interfaz con opción de interacción usuario-interfaz
#	vinculado a generar registro en la base de datos
# 4 PTOS - Habilitación de opción en la interfaz para interacción usuario - usuario,
#	con llamada a la base de datos y almacenamiento en la misma de la interacción resultante
# * PTOS - Cualquier funcionalidad extra que aporte valor a la red social

import BDD
import Activities.Class_Main_Activities as CLM
import tkinter as tk

if __name__ == '__main__':
    root = tk.Tk()
    app = CLM.Social_Network_App(root)
    conection = BDD.create_connection("Social_network_database.db")

    create_users_table = """
               CREATE TABLE IF NOT EXISTS users (
                   user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   user_name TEXT NOT NULL,
                   user_lastname TEXT,
                   user_email TEXT NOT NULL UNIQUE,
                   user_password TEXT
                   )
               """
    create_conversation_table = """
                   CREATE TABLE IF NOT EXISTS conversation (
                       conversation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                       user_id1 INTEGER NOT NULL,
                       user_id2 INTEGER NOT NULL,
                       reference_conversation TEXT NOT NULL,
                       data BLOB,
                       FOREIGN KEY (user_id1) REFERENCES users(user_id)
                       FOREIGN KEY (user_id2) REFERENCES users(user_id)
                       )
                   """
    BDD.execute_query(create_users_table)
    BDD.execute_query(create_conversation_table)

    print("MAIN -> Finished")

    # conection.close()
    app.mainloop()
