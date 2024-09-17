import reflex as rx

class St(rx.State):
    cuota: float
    nombre: str
    carrera: str
    localidad: str

    def comprobar(self):
        if self.carrera == 'E' and self.localidad != 'R':
            self.cuota = 100_000 * 0.85
        else:
            self.cuota = 100_000
 
def g01e10():
    return rx.dialog.root(
        rx.dialog.trigger(
            rx.button(
                rx.text("Guía 01 - Ejercicio 10"),
            ),
        ),
        rx.dialog.content(
            rx.hstack(
            rx.input(
                placeholder="Nombre",
                on_blur=St.set_nombre,
            ),
            rx.input(
                placeholder="Carrera",
                on_blur=St.set_carrera,
            ),
            rx.input(
                placeholder="Localidad",
                on_blur=St.set_localidad,
            ),
            rx.button(
                "Comprobar",
                on_click=St.comprobar,
            ),
            ),
            rx.heading(f'{St.nombre} paga una cuota de ${St.cuota}'),
        ),
    )


