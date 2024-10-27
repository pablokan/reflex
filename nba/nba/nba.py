from .backend.backend import State
from .views.navbar import navbar
from .views.table import main_table
from .views.stats import stats_ui
import reflex as rx


def _tabs_trigger(text: str, icon: str, value: str):
    return rx.tabs.trigger(
        rx.hstack(
            rx.icon(icon, size=24),
            rx.heading(text, size="5"),
            spacing="2",
            align="center",
            width="100%",
        ),
        value=value,
    )


def index() -> rx.Component:
    return rx.vstack(
        navbar(),
        rx.tabs.root(
            rx.tabs.list(
                _tabs_trigger("Table", "table-2", value="table"),
                _tabs_trigger("Stats", "bar-chart-3", value="stats"),
            ),
            rx.tabs.content(
                main_table(),
                margin_top="1em",
                value="table",
            ),
            rx.tabs.content(
                stats_ui(),
                margin_top="1em",
                value="stats",
            ),
            default_value="table",
            width="100%",
        ),
        width="100%",
        spacing="6",
        padding_x=["1.5em", "1.5em", "3em", "5em"],
        padding_y=["1.25em", "1.25em", "2em"],
    )


app = rx.App()
app.add_page(
    index,
    on_load=State.load_entries,
    title="NBA Data",
    description="NBA Data for the 2015-2016 season.",
)
