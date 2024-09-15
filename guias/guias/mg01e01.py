import reflex as rx

class St(rx.State):
    n1: int = 0
    n2: int = 0
    resu: int = 0

    def sumar(self):
        self.resu = self.n1 + self.n2
    
def g01e01() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.text("Guía 1 - Ejercicio 1"),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
            rx.input(
                placeholder="Primer número",
                on_blur=St.set_n1,
            ),
            rx.input(
                placeholder="Segundo número",
                on_blur=St.set_n2,
            ),
            rx.button(
                "Incremento",
                on_click=St.sumar,
            ),
            rx.heading(St.resu),
        ),
        ),
    )
