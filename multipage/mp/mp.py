import reflex as rx

from .pages.uno import uno
from .pages.dos import dos
from .pages.tres import tres
from .pages.tabla1 import tabla1
from .pages.tabla2 import tabla2

def index():
    ps = rx.box(
        rx.link('uno', href='/uno'),
        rx.divider(),
        rx.link('dos', href='/dos'),
        rx.divider(),
        rx.link('tres', href='/tres'),
        rx.divider(),
        rx.link('tabla 1', href='/tabla1'),
        rx.divider(),
        rx.link('tabla 2', href='/tabla2')
    )
    return ps

app = rx.App()
app.add_page(index)
app.add_page(uno)
app.add_page(dos)
app.add_page(tres)
app.add_page(tabla1)
app.add_page(tabla2)

