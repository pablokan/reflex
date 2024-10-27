import reflex as rx
from .database import Database

# backend
class Data(rx.State):
    cabecera: list = []
    gente: list[list] = []

    def obtenerUsuarios(self):
        d = Database('tienda')
        self.cabecera = d.fieldNames
        self.gente = d.get_all()


# frontend
def mostrarRegistro(record: list):
    records = rx.table.row(
            rx.foreach(
                record,
                lambda x: rx.table.cell(x),
            ),
    )
    return records

@rx.page(on_load=Data.obtenerUsuarios)
def tabla1():
    page = rx.box(
        rx.heading("Tabla de Datos", align='center'),
        rx.table.root(
            rx.table.header(
                rx.table.row(
                    rx.foreach(
                        Data.cabecera,
                        lambda x: rx.table.column_header_cell(x),
                    ),
                ),
            ),
            rx.table.body(
                rx.foreach(
                    Data.gente, mostrarRegistro
                )
            ),
        ),
    )
    return page
