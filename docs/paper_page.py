from flet import *


# A component that displays its content on an elevated surface
class Paper(Container):
    def __init__(
        self,
        outlined: bool = False,
        elevation: int = 1,
        **kwargs,
    ) -> None:
        super().__init__(**kwargs)
        self.elevation: int = elevation
        # Define the shadow parameters based on the distance
        self.shadow_params: dict = {
            0: (0, 0, 0, 0),
            1: (1, 2, 0.1, 1),
            2: (2, 4, 0.15, 2),
            3: (3, 6, 0.2, 3),
            4: (4, 8, 0.25, 4),
            8: (6, 10, 0.3, 8),
            12: (8, 12, 0.35, 12),
            16: (10, 14, 0.4, 16),
            24: (12, 14, 0.4, 16),
        }
        spread_radius, blur_radius, opacity, offset_y = self.shadow_params.get(
            self.elevation, (0, 0, 0, 0)
        )
        # Create the shadow based on the parameters
        shadows = [
            BoxShadow(
                spread_radius=spread_radius,
                blur_radius=blur_radius,
                color=colors.with_opacity(opacity, "black"),
                offset=Offset(0, offset_y),
            )
        ]

        # Create the container with the specified shadow
        if outlined:
            self.border = border.all(width=2, color="#80868B")
        self.shadow = shadows


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
