import reflex as rx

class St(rx.State):
    cajas: list[int] = [0] * 5
    numeros: list[int]
    numero: int
    resu: int

    def addNumber(self, numero):
        self.numeros.append(numero)

    def contar23(self):
        self.resu = len([int(n) for n in self.numeros if int(n) > 23])
        self.numeros = []

def inputs(retorno):
    retorno = (
        rx.input(
            type="number",
            on_blur=St.addNumber
        )
    )
    return retorno


def g02e03() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.text("Guía 02 - Ejercicio 03"),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
                rx.foreach(
                    St.cajas,
                    inputs,
                ),
                rx.button(
                    'Contar los mayores a 23',
                    on_click=St.contar23
                ),
                rx.heading(
                    St.resu
                ),
        ),
        ),
    )

