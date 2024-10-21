import reflex as rx

class ListState(rx.State):
    items: list[str] = ["Write Code", "Awake", "Have Not Fun"]
    new_item: str

    def add_item(self):
        self.items.append(self.new_item)

    def finish_item(self, item: str):
        self.items = [i for i in self.items if i != item]


def get_item(item):
    return rx.list.item(
        rx.hstack(
            rx.button(
                on_click=lambda: ListState.finish_item(item), # type: ignore
                height="1.5em",
                border="1px solid blue",
            ),
            rx.text(item, font_size="1.25em"),
        ),
    )


def index():
    return rx.vstack(
        rx.heading("Todos"),
        rx.input(
            on_blur=ListState.set_new_item, # type: ignore
            placeholder="Add a todo...",
        ),
        rx.button(
            "Add", on_click=ListState.add_item
        ),
        rx.divider(),
        rx.list.ordered(
            rx.foreach(
                ListState.items,
                get_item,
            ),
        ),
        padding="1em",
        border_radius="0.5em",
        shadow="lg",
    )

app = rx.App()
app.add_page(index)