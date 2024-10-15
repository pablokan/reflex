import reflex as rx
from rxconfig import config

from .backend import *
from .otra import otra_pagina

# frontend - vista de usuario (Reflex la traduce de Python a JS)
# los componentes de Reflex para mostrar data en una página web

def about():
    return rx.text("About Page")

def index() -> rx.Component:
    def input3():
        return rx.input( # valores fijos, no deja editar
                        value=FocusState.contenido, 
                        on_focus=FocusState.cambiar_contenido, # envía como argumento oculto el valor anterior
                        on_blur=FocusState.pierdo_foco,
                    )
    
    def radios():
        return rx.radio(
                    RadioState.items, 
                    direction="row", 
                    spacing="9",
                    on_change=RadioState.set_selected # type: ignore
                )

    # ejemplos de varios componentes
    page =  rx.box(
                rx.vstack(
                    rx.heading('Plantilla Base 1.2'),
                    rx.divider(),
                    rx.text('texto normal'),
                    rx.text('texto normal tamaño 6', size='6'),
                    rx.input(),
                    rx.hstack(
                        rx.text('Este input solo acepta números:'),
                        rx.input(type='number'),
                    ),
                    input3(),
                    rx.box(
                        rx.hstack(
                            radios(),
                            rx.text(f'Opción elegida: {RadioState.selected}', size='2'),
                            spacing='9',    
                        ),
                        bg="IndianRed",
                        border_radius="10px",
                        width="50%",
                        padding="10px",
                    ),
                    rx.hstack(
                        rx.image(
                            src="/mahomes.webp", 
                            width="100px", 
                            height="auto",
                            border="2px solid RebeccaPurple",
                        ),

                        rx.select(
                            ComboState.items, 
                            default_value='De qué juega Mahomes?',
                            on_change=ComboState.set_selected # type: ignore
                        ),
                        rx.text(f'Opción elegida: {ComboState.selected}', size='2'),
                        spacing='5'
                    ),

                    # propiedades del rx.vstack
                    spacing='5'
                ),
                rx.divider(),
                rx.link(
                    "Ir a otra página ", 
                    href="/otra",
                    size='9',
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
app.add_page(about)
app.add_page(otra_pagina, route="/otra")
