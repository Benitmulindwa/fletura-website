from flet import *
from fletura import FlatContainer, FloatingContainer, ConvexContainer


def Paper_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Neumorphic Containers",
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
                                "A set of customizable components(Containers) with neumorphism.",
                                size=18,
                                color="black",
                            ),
                            Row(
                                [
                                    Column(
                                        [
                                            Text(
                                                "FlatContainer",
                                                weight=FontWeight.BOLD,
                                            ),
                                            FlatContainer(
                                                content=Text("Flat Container"),
                                                height=100,
                                                width=100,
                                            ),
                                        ]
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "ConvexContainer",
                                                weight=FontWeight.BOLD,
                                            ),
                                            ConvexContainer(
                                                width=100,
                                                height=100,
                                                border_radius=50,
                                                padding=padding.only(20),
                                                elevation=0.4,
                                                content=Text(
                                                    "Convex Container", color="black"
                                                ),
                                            ),
                                        ]
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "FloatingContainer",
                                                weight=FontWeight.BOLD,
                                            ),
                                            FloatingContainer(100, width=100),
                                        ],
                                    ),
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
