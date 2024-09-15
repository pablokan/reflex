from reflex import App, State, hstack, button, heading

class St(State):
    count: int = 0

    def increment(self):
        self.count += 1

    def decrement(self):
        self.count -= 1

def index():
    a = hstack(
        button(
            "Decremento",
            on_click=St.decrement,
        ),
        
        button(
            "Incremento",
            on_click=St.increment,
        ),

        heading(St.count),

    )
    return a


app = App()
app.add_page(index)
