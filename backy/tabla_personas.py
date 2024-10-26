import reflex as rx
from .comp_table import cTable, Data

def index():
    page = rx.box(
        rx.link(
            rx.button("Componente table", color_scheme="green"),
            href="/tablabase",
            text_decoration="none"
        )
    )
    return page


app = rx.App(state=Data)
app.add_page(index, route="/")
app.add_page(cTable, route="/tablabase")
