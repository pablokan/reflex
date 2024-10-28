# todo -> updates: uno x uno o bien borrar la tabla y agregarla completa?
import reflex as rx
from rxconfig import config
from .database import Database

class DatEd(rx.State):
    clicked_data: str = "Cell clicked: "
    gente: list[list] = []
    cabecera: list = []
    
    def obtenerDatos(self) -> None:
        d = Database('tienda')
        self.cabecera = [{'title': c, 'type': 'str'} for c in d.fieldNames] 
        recordSet = d.get_all()
        self.gente = [[str(valor) for valor in registro] for registro in recordSet]

    def click_cell(self, pos) -> None:
        self.clicked_data = f"Cell clicked: {pos}"

    def handle_cell_edited(self, pos, data) -> None:
        col, row = pos
        nuevoValor = data['data']
        self.gente[row][col] = nuevoValor
        id = self.gente[row][0]
        campoModificado = self.cabecera[col]['title']
        d = Database('tienda')
        d.upd(id, campoModificado, nuevoValor)

@rx.page(on_load=DatEd.obtenerDatos)    
def index() -> rx.Component:
    return rx.box(
        rx.heading(DatEd.clicked_data, align='center'),
        rx.divider(size='4'),
        rx.data_editor(
            columns=DatEd.cabecera,
            data=DatEd.gente,
            on_cell_clicked=DatEd.click_cell,
            on_cell_edited=DatEd.handle_cell_edited,
        ),
    )

app = rx.App()
app.add_page(index)