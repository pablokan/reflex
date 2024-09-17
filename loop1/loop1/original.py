import reflex as rx
from rxconfig import config

class St(rx.State):
    colores: list[str] = [
        "red",
        "green",
        "blue",
        "yellow",
        "orange",
        "purple",
    ]


def colored_box_index(color: str, index: int):
    return rx.box(rx.text(f'Número {index+1}'), bg=color)


def index():
    return rx.hstack(
        rx.foreach(
            St.colores,
            lambda color, index: colored_box_index(
                color, index
            ),
        ),
    )

app = rx.App()
app.add_page(index)
