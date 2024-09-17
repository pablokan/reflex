import reflex as rx
from rxconfig import config

class St(rx.State):
    numeros: list[int] = [0] * 5
    numero: int

    def add_number(self, numero):
        print(id, numero)
        #self.numeros[id] = n

def inputs(color: str, id: int):
    foo = (
        rx.input(
            f'Númer{id+1}',
            on_blur=St.add_number
            )
    )
    return foo


def index():
    return rx.hstack(
        rx.foreach(
            St.numeros,
            inputs,
        ),
    )

app = rx.App()
app.add_page(index)
