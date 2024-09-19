import reflex as rx
from rxconfig import config

# backend - atributos y métodos (variables y funciones)
# todos los datos y las operaciones aquí
class State(rx.State):
    nombre: str
    edad: int
    altura: float
    lista: list[str]

    def agregar_nombre(self):
        self.lista.append(self.nombre)

    def es_mayor(self):
        return self.edad >= 18

class FocusState(rx.State):
    contenido = "valor inicial"

    def cambiar_contenido(self, argumento_oculto):
        print(argumento_oculto)
        self.contenido = 'tengo el foco!'

    def pierdo_foco(self, argumento_oculto):
        print(argumento_oculto)
        self.contenido = 'perdí el foco!'

class RadioState(rx.State):
    items: list[str] = ["1", "2", "3"]
    selected: str

# frontend - vista de usuario (Reflex la traduce de Python a JS)
# los componentes de Reflex para mostrar data en una página web
def index() -> rx.Component:
    # ejemplos de varios componentes
    page =  rx.box(
                rx.vstack(
                    rx.heading('Plantilla Base'),
                    rx.divider(),
                    rx.text('texto normal'),
                    rx.text('texto normal tamaño 6', size='6'),
                    rx.input(),
                    rx.hstack(
                        rx.text('Este input solo acepta números:'),
                        rx.input(type='number'),
                    ),
                    rx.input( # valores fijos, no deja editar
                        value=FocusState.contenido, 
                        on_focus=FocusState.cambiar_contenido, # envía como argumento oculto el valor anterior
                        on_blur=FocusState.pierdo_foco,
                    ),
                    rx.hstack(
                        rx.radio(
                            RadioState.items, 
                            direction="row", 
                            spacing="9",
                            on_change=RadioState.set_selected # type: ignore
                        ),
                        rx.text(f'Opción elegida: {RadioState.selected}', size='2'),

                        spacing='9'
                    ),
                    rx.hstack(
                        rx.image(
                            src="/mahomes.webp", 
                            width="100px", 
                            height="auto",
                            border="5px solid #555",
                        ),

                        rx.select(
                            ['De qué juega Mahomes?', "Tight End", "Running Back", "Quarterback", "Wide Receiver", "Left Tackle"],
                            default_value='De qué juega Mahomes?'
                        ),
                    ),

                    # propiedades del rx.vstack
                    spacing='5'
                ),

                # propiedades del rx.box
                background = 'DarkOliveGreen',
                width="100%",
                height="100vh",
                padding="40px",
            )

    return page


app = rx.App()
app.add_page(index)

