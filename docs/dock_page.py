from flet import *


class Dock(Container):
    def __init__(
        self,
        dock_icon: str = icons.MAIL,
        icon_color: str = "white",
        dock_color: str = "red",
        count: int = 4,
        max_value: int = 9,
        position: str = "top_left",
    ):
        super().__init__()
        self.max_value = max_value
        self.dock_color = dock_color
        self.content = Stack(
            [
                Container(
                    Icon(dock_icon, color=icon_color, size=30),
                    height=50,
                    width=60,
                    margin=margin.only(
                        left=-16 if "right" in position else 5, right=15
                    ),
                ),
                self.create_dock(count, position),
            ]
        )

        self.alignment = alignment.center

    def create_dock(self, count: int, position: str):
        display_count = f"{count}" if count <= self.max_value else f"{self.max_value}+"

        # Adjasting the top container size based on whether a single,2 or 3 digits number are given
        dock_width = 20  # default width for single-digit numbers
        if self.max_value >= 10:
            dock_width = 25  # width for two-digit numbers
        if self.max_value >= 100:
            dock_width = 30  # width for three-digit numbers

        dock = Container(
            Text(
                display_count,
                color="white",
                weight=FontWeight.W_500,
                size=11,
                text_align="center",
            ),
            bgcolor=self.dock_color,
            border_radius=dock_width // 2,
            width=dock_width,
            height=20,
            alignment=alignment.center,
        )
        if position == "top_right":
            dock.bottom = 26
            dock.left = 22
        elif position == "center_left":
            dock.top = 15
            dock.left = 22
        elif position == "bottom_right":
            dock.top = 26
            dock.left = 22
        elif position == "bottom_left":
            dock.top = 26
            dock.right = 50
        else:
            dock.bottom = 26
            dock.right = 50

        return dock


def Dock_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Dock component",
                        size=24,
                        weight=FontWeight.BOLD,
                        color="#223631",
                    ),
                    padding=padding.only(30, bottom=10),
                ),
                Container(
                    content=Column(
                        [
                            Text(
                                "The Dock component is a customizable UI element designed to display notifications or status indicators in a visually appealing manner.",
                                size=18,
                                color="black",
                            ),
                            Row(
                                [
                                    Row(
                                        [
                                            Dock(
                                                dock_icon=icons.MAIL,
                                                count=4,
                                                max_value=99,
                                                position="top_left",
                                            ),
                                            Dock(
                                                dock_icon=cupertino_icons.CART,
                                                count=12,
                                                max_value=99,
                                                position="top_right",
                                                dock_color="green",
                                            ),
                                            Dock(
                                                dock_icon=icons.PERSON_ADD,
                                                count=5,
                                                max_value=99,
                                                position="top_right",
                                                dock_color="blue",
                                            ),
                                            Dock(
                                                dock_icon=icons.NOTIFICATIONS,
                                                count=7,
                                                max_value=99,
                                                position="top_right",
                                                dock_color="orange",
                                            ),
                                        ],
                                        alignment="spaceAround",
                                    )
                                ],
                                scroll="always",
                                spacing=20,
                            ),
                        ],
                    ),
                    padding=padding.only(30, right=30),
                ),
            ],
            scroll="always",
            alignment="start",
            horizontal_alignment="start",
        ),
        visible=False,
        expand=True,
        # height=500,
        width=page.width // 1.1,
        alignment=alignment.top_left,
    )
    # cont.alignment = alignment.center_left

    return cont
