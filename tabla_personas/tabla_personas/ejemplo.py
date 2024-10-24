import reflex as rx
import sqlite3
from dataclasses import dataclass
from typing import List

@dataclass
class Usuario:
    id: str
    nombre: str
    edad: str

class Estado(rx.State):
    usuarios: List[Usuario] = []
    
    def obtener_usuarios(self):
        """Obtiene los usuarios de la base de datos SQLite."""
        conn = sqlite3.connect('persons.db')
        cursor = conn.cursor()
        
        try:
            cursor.execute("SELECT * FROM persons")
            resultados = cursor.fetchall()
            
            self.usuarios = [
                Usuario(id=row[0], nombre=row[1], edad=row[2])
                for row in resultados
            ]
            
        except sqlite3.Error as e:
            print(f"Error al obtener datos: {e}")
            
        finally:
            conn.close()

    # Este método se ejecutará automáticamente cuando se monte el componente
    def on_mount(self):
        """Se ejecuta automáticamente cuando la página se carga."""
        self.obtener_usuarios()

def index():
    return rx.vstack(
        rx.heading("Lista de Usuarios"),
        rx.foreach(
            Estado.usuarios,
            lambda usuario: rx.box(
                rx.text(f"ID: {usuario.id}"),
                rx.text(f"Nombre: {usuario.nombre}"),
                rx.text(f"Email: {usuario.edad}"),
                padding="1em",
                border="1px solid gray",
                margin="0.5em",
                border_radius="0.5em"
            )
        )
    )

# Configuración de la aplicación
app = rx.App()
app.add_page(index)