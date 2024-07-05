from flet import *
from fletura import Paper


def Paper_content(page):

    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Paper Component",
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
                                "A component that displays its content on an elevated surface.",
                                size=18,
                                color="black",
                            ),
                            Row(
                                [
                                    Column(
                                        [
                                            Container(
                                                Paper(
                                                    elevation=1,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="white",
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 1", color="black"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=4,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="white",
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 4", color="black"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=8,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="white",
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 8", color="black"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=12,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="white",
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 12", color="black"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                        ]
                                    ),
                                    # _______________Bgcolor=black__________________
                                    Column(
                                        [
                                            Container(
                                                Paper(
                                                    elevation=1,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="black",
                                                    outlined=True,
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 1", color="white"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=4,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="black",
                                                    outlined=True,
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 4", color="white"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=8,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="black",
                                                    outlined=True,
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 8", color="white"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                            Container(
                                                Paper(
                                                    elevation=12,
                                                    width=200,
                                                    height=50,
                                                    bgcolor="black",
                                                    outlined=True,
                                                    alignment=alignment.center,
                                                    content=Text(
                                                        "Elevation 12", color="white"
                                                    ),
                                                ),
                                                padding=padding.only(top=10),
                                            ),
                                        ],
                                    ),
                                ],
                                spacing=30,
                                scroll="always",
                            ),
                        ],
                        scroll="always",
                        alignment="start",
                        horizontal_alignment="start",
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
        width=page.width // 1.1,
        alignment=alignment.top_left,
    )

    return cont
