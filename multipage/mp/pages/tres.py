import reflex as rx

class Algo(rx.State):
    a: str

    def foo(self):
        self.a = 'aaa'

@rx.page(on_load=Algo.foo)
def tres():
    return rx.text(Algo.a)

