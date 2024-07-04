from flet import *
from fletura import Dock


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
