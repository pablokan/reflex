import reflex as rx
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
        self.contenido = 'no tengo el foco!'

class RadioState(rx.State):
    items: list[str] = ["1", "2", "3"]
    selected: str

class ComboState(rx.State):
    items: list[str] = ['De qué juega Mahomes?', "Tight End", "Running Back", "Quarterback", "Wide Receiver", "Left Tackle"]
    selected: str
