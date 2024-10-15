import reflex as rx

# backend
class RadioState(rx.State):
    colores: list[str] = ['green', 'red', 'blue']
    colorElegido: str

class ComboState(rx.State):
    deporteElegido: str

# frontend
def index():
    page = rx.box(
            rx.vstack(
                rx.heading('Título'),
                rx.divider(),
                rx.text('hola mundo de nuevo'),
                rx.input(),
                rx.hstack(
                    rx.text('Ingrese un valor:'),
                    rx.input(type='number'),
                ),
                rx.divider(),
                rx.hstack(
                    rx.radio(
                        RadioState.colores,
                        direction='row',
                        on_change=RadioState.set_colorElegido, # type: ignore
                    ),
                ),
                rx.text(f'Color seleccionado {RadioState.colorElegido}'),
                
                rx.select(
                    ['Basquet', 'Fútbol', 'Tenis'],
                    default_value='Tenis',
                    on_change=ComboState.set_deporteElegido, # type: ignore
                ),
                rx.text(f'Deporte elegido: {ComboState.deporteElegido}'),
                rx.image(
                    src='/scaloni.jpeg',
                    width='123px',
                    height='auto',
                    border="5px dashed MediumTurquoise",
                ),
                rx.text('Línea final'),
                spacing='2',
            ),
            background=RadioState.colorElegido, # fondo del box
            padding='27px', # distancia al borde del box
           )
    
    return page


app = rx.App()
app.add_page(index)
