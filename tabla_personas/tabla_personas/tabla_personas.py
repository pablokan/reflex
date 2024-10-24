import reflex as rx
import sqlite3
       
    
class Data(rx.State):
    gente: list[list] = []

    def obtener_usuarios(self):
        conn = sqlite3.connect('persons.db')
        cursor = conn.cursor()
        cursor.execute('select * from persons')
        self.gente = cursor.fetchall()


# frontend

def show_person(person: list):
    t = rx.table.row(
        rx.table.cell(person[0]),
        rx.table.cell(person[1]),
        rx.table.cell(person[2]),
    )
    return t

@rx.page(on_load=Data.obtener_usuarios)
def index():
    page = rx.box(
        rx.heading("Usuarios", align='center'),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.table.column_header_cell("id"),
                    rx.table.column_header_cell("nombre"),
                    rx.table.column_header_cell("edad"),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    Data.gente, show_person
                )
            ),
            width="100%",
        )
    )
    return page

app = rx.App()
app.add_page(index)
