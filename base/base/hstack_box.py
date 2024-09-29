rx.hstack(
    rx.box(
        rx.radio(
            RadioState.items, 
            direction="row", 
            spacing="9",
            on_change=RadioState.set_selected # type: ignore
        ),
        rx.text(f'Opción elegida: {RadioState.selected}', size='2'),
        bg="red",
        border_radius="3px",
        width="100%",
        padding="10px",
    ),
    spacing='9',
),
