import reflex as rx

class St(rx.State):
    n1: float = 0
    resu: str = ''

    def comprobar(self):
        if self.n1 > 0:
            self.resu = "es mayor a cero"
        elif self.n1 < 0:
            self.resu = "es menor a cero"
        else:
            self.resu = "es exactamente cero"
 
def g01e03() -> rx.Component:
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.text("Guía 01 - Ejercicio 03"),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
            rx.input(
                placeholder="Ingrese número",
                on_blur=St.set_n1,
            ),
            rx.button(
                "Comprobar",
                on_click=St.comprobar,
            ),
            rx.heading(St.resu),
        ),
        ),
    )

