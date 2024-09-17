import reflex as rx
from rxconfig import config

class St(rx.State):
    colores: list[str] = [
        "red",
        "green",
        "blue",
        "black",
        "orange",
        "purple",
    ]


def colored_box_index(color: str, index: int):
    return rx.box(rx.input(f'Núm{index+1}'), bg=color)


def index():
    return rx.hstack(
        rx.foreach(
            St.colores,
            colored_box_index,
        ),
    )

app = rx.App()
app.add_page(index)
