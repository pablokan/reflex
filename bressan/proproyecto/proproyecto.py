import reflex as rx
from proproyecto.cruddb import Crud

class TableForEachState(rx.State):
    items: list[list] = []

    #obtener lista para monstrar
    def get_data(self):
        self.items = Crud.listar()

    # borrar por id toda (la fila) **poner boton**
    def delete_data(self, component_id):
        Crud.eliminar(component_id)

    #agregar una fila **poner boton**
    def add_data(self):
        #Crud.agregar(tipo, nombre, socket, stock, descripcion, precio, enlace)
        pass

    #editar (edita la fila entera) **ver como hacer que edite de a un valor**
    # **poner boton**
    def edit_data(self, item_id):
        pass

    #ver si puedo cargar una foto y que se suba la ruta o algo
    """
    def cargar_foto (self) 
        pass
    """
    

def show_item(item: list):
    #mostrar objetos en la lista por row
    return rx.table.row(
        rx.table.cell(item[0]),  # ID
        rx.table.cell(item[1]),  # Tipo
        rx.table.cell(item[2]),  # Nombre
        rx.table.cell(item[3]),  # Socket
        rx.table.cell(item[4]),  # Stock
        rx.table.cell(item[5]),  # Descripción
        rx.table.cell(item[6]),  # Precio
        rx.table.cell(item[7]),  # Enlace
    )

@rx.page(on_load=TableForEachState.get_data)
#actualizar pagina al iniciar
def index():
    return rx.table.root(
        rx.table.header(
            #titulos de cada  columna
            rx.table.row(
                rx.table.column_header_cell("ID"),
                rx.table.column_header_cell("Tipo"),
                rx.table.column_header_cell("Nombre"),
                rx.table.column_header_cell("Socket"),
                rx.table.column_header_cell("Stock"),
                rx.table.column_header_cell("Descripción"),
                rx.table.column_header_cell("Precio"),
                rx.table.column_header_cell("Enlace"),
                #rx.table.cell( agregar columna
                # con botones (rx-button))
            ),
        ),
        rx.table.body(
            rx.foreach(
                TableForEachState.items, show_item
            )
        ),
        width="100%",
    )

app = rx.App()
app.add_page(index)