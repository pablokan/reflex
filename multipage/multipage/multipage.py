"""Welcome to Reflex! This file outlines the steps to create a basic app."""

import reflex as rx

from rxconfig import config

@rx.page(route="/", title="My Beautiful App")
def index():
    page = rx.container(
        rx.text("Root Page"),
        rx.link("Quienes somos", href="/about")
    )
    return page


def about():
    return rx.text("About Page")


def custom():
    return rx.text("Custom Route")


app = rx.App()

app.add_page(index)
app.add_page(about)
app.add_page(custom, route="/custom-route")
