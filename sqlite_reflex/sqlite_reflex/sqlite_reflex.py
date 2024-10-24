import reflex as rx
from rxconfig import config

class State(rx.State):
    """The app state."""

    ...


def index() -> rx.Component:
    page = rx.container(
        rx.vstack(
            rx.heading("SQLite on Reflex", size="9"),
            rx.text(
                'Texto tamaño 5',
                size="5",
            ),
            spacing="5",
        ),
    )
    return page

app = rx.App()
app.add_page(index)
