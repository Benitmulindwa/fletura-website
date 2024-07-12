from flet import *


class ShadowPosition:
    TOP_RIGHT: tuple = (5, -5)
    TOP_LEFT: tuple = (-5, -5)
    BOTTOM_RIGHT: tuple = (5, 5)
    BOTTOM_LEFT: tuple = (-5, 5)


class FlatContainer(Container):
    def __init__(self, height: int, **kwargs):
        super().__init__(
            bgcolor=colors.GREY_200,
            height=height,
            alignment=alignment.center,
            border_radius=10,
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, colors.BLACK),
                    offset=Offset(2, 2),
                ),
            ],
            **kwargs,
        )


class ConvexContainer(Container):
    def __init__(
        self,
        height: int,
        elevation: float = 0.0,
        shadow1_color: str = "white",
        shadow2_color: str = "black",
        border_radius=10,
        **kwargs,
    ):
        super().__init__(
            height=height,
            alignment=alignment.center,
            border_radius=border_radius,
            gradient=LinearGradient(
                colors=["#cacaca", "#f0f0f0"],
                end=alignment.top_left,
                begin=alignment.center_right,
            ),
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(elevation, shadow1_color),
                    offset=Offset(-1, -1),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=10,
                    color=colors.with_opacity(elevation / 2, shadow2_color),
                    offset=Offset(1, 1),
                ),
            ],
            **kwargs,
        )


class FloatingContainer(Container):
    def __init__(
        self,
        height: int,
        border_radius=10,
        bgcolor: str = colors.GREY_200,
        shadow1_color: str = colors.WHITE,
        shadow2_color: str = colors.BLACK,
        shadow_position: ShadowPosition = ShadowPosition.BOTTOM_RIGHT,
        **kwargs,
    ):
        super().__init__(
            bgcolor=bgcolor,
            height=height,
            alignment=alignment.center,
            border_radius=border_radius,
            shadow=[
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, shadow1_color),
                    offset=Offset(-shadow_position[0], -shadow_position[1]),
                ),
                BoxShadow(
                    spread_radius=1,
                    blur_radius=6,
                    color=colors.with_opacity(0.2, shadow2_color),
                    offset=Offset(*shadow_position),
                ),
            ],
            **kwargs,
        )


def Neumorphic_content(page):
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
                            ResponsiveRow(
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
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
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
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "FloatingContainer",
                                                weight=FontWeight.BOLD,
                                            ),
                                            FloatingContainer(100, width=100),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                ],
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
