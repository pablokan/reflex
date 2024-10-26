import reflex as rx
from .database import Database

# backend
class Data(rx.State):
    cabecera: list = []
    gente: list[list] = []

    def obtenerUsuarios(self):
        print('obtener usuarios')
        #fields_def = ['item TEXT', 'qty INTEGER', 'price REAL', 'pic TEXT']
        #d = Database('tienda', *fields_def)
        d = Database('tienda')
        self.cabecera = d.field_names
        self.gente = d.get_all()


# frontend
def show_record(record: list):
    records = rx.table.row(
            rx.foreach(
                record,
                lambda x: rx.table.cell(x),
            ),
    )
    return records

@rx.page(on_load=Data.obtenerUsuarios)
def cTable():
    page = rx.box(
        rx.heading("Tabla de Datos"),
        rx.button('Obtener datos', on_click=Data.obtenerUsuarios),
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
                    Data.gente, show_record
                )
            ),
        ),
    )
    return page

if __name__ == "__main__":
    app = rx.App()
    app.add_page(cTable)
