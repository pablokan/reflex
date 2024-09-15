"""Home Page de ejercicios de la guía de Programación 1"""
import reflex as rx

from .mg01e01 import *
from .mg01e03 import *
from .mg01e10 import *

def index():
    return rx.container(
        rx.vstack(
            rx.heading("Ejercicios de las Guías", size="9"),
            g01e01(),
            g01e03(),
            g01e10(),
        ),
    )

app = rx.App()
app.add_page(index)
