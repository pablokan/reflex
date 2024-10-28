import reflex as rx
from rxconfig import config

class DatEd(rx.State):
    clicked_data: str = "Cell clicked: "
    data = [
        [
            "1",
            "Harry James Potter",
            "31 July 1980",
            True,
            "Gryffindor",
            "11'  Holly  phoenix feather",
            "Stag",
            "Half-blood",
        ],
        [
            "2",
            "Ronald Bilius Weasley",
            "1 March 1980",
            True,
            "Gryffindor",
            "12' Ash unicorn tail hair",
            "Jack Russell terrier",
            "Pure-blood",
        ],
        [
            "3",
            "Hermione Jean Granger",
            "19 September, 1979",
            True,
            "Gryffindor",
            "10¾'  vine wood dragon heartstring",
            "Otter",
            "Muggle-born",
        ],
        [
            "4",
            "Albus Percival Wulfric Brian Dumbledore",
            "Late August 1881",
            True,
            "Gryffindor",
            "15' Elder Thestral tail hair core",
            "Phoenix",
            "Half-blood",
        ],
        [
            "5",
            "Rubeus Hagrid",
            "6 December 1928",
            False,
            "Gryffindor",
            "16'  Oak unknown core",
            "None",
            "Part-Human (Half-giant)",
        ],
        [
            "6",
            "Fred Weasley",
            "1 April, 1978",
            True,
            "Gryffindor",
            "Unknown",
            "Unknown",
            "Pure-blood",
        ],
    ]
    cols = [
        {"title": "Title", "type": "str"},
        {
            "title": "Name",
            "type": "str",
            "group": "Data",
            "width": 300,
            "editable": True,
        },
        {
            "title": "Birth",
            "type": "str",
            "group": "Data",
            "width": 150,
            "editable": True,
        },
        {
            "title": "Human",
            "type": "bool",
            "group": "Data",
            "width": 80,
            "editable": True,
        },
        {
            "title": "House",
            "type": "str",
            "group": "Data",
            "editable": True,
        },
        {
            "title": "Wand",
            "type": "str",
            "group": "Data",
            "width": 250,
            "editable": True,
        },
        {
            "title": "Patronus",
            "type": "str",
            "group": "Data",
            "editable": True,
        },
        {
            "title": "Blood status",
            "type": "str",
            "group": "Data",
            "width": 200,
            "editable": True,
        },
    ]

    def click_cell(self, pos):
        self.clicked_data = f"Cell clicked: {pos}"

    def handle_cell_edited(self, pos, data):
        row, col = pos
        self.data[col][row] = data['data']
    
def index() -> rx.Component:
    return rx.box(
        rx.heading(DatEd.clicked_data, align='center'),
        rx.divider(size='4'),
        rx.data_editor(
            columns=DatEd.cols,
            data=DatEd.data,
            on_cell_clicked=DatEd.click_cell,
            on_cell_edited=DatEd.handle_cell_edited,
        ),
    )

app = rx.App()
app.add_page(index)