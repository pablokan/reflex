import reflex as rx
from rxconfig import config

class State(rx.State):
    lista: list[int]
    resultado: int

    def agregar(self, n):
        print(self.lista)
        self.lista.append(int(n))
        print(self.lista)

    def contar23(self):
        c = 0
        for n in self.lista:
            if n > 23:
                c += 1
        self.resultado = c
        self.lista = []

def pedir_numero(x):
    return rx.input('', on_blur=State.agregar)

def index() -> rx.Component:
    page =  rx.box(
        rx.text('Ingresar 5 enteros'),
        rx.foreach(
            list(range(5)),
            pedir_numero
        ),
        rx.button('Contar los mayores a 23', on_click=State.contar23),
        rx.heading(State.resultado)
    )
    return page


app = rx.App()
app.add_page(index)