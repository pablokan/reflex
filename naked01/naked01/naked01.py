import reflex as rx

class St(rx.State):
    nombre: str
    saludo: str
             
    def saludar(self):
        self.saludo = f'Hola {self.nombre}'

def index():
    page = (rx.input(
                placeholder="Nombre",
                on_blur=St.set_nombre, # type: ignore
            ),
            rx.button(
                "Saludar",
                on_click=St.saludar,
            ),
            rx.heading(St.saludo),  
    )
    return page

app = rx.App()
app.add_page(index) # type: ignore
