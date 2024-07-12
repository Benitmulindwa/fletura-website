from flet import *


class CardMedia(Container):
    def __init__(
        self,
        image_src: str,
        image_height: int = 140,
        can_expand: bool = False,
        actions: list = [],
        title: str = "Lizard",
        title_style: TextStyle = None,
        description: str = "",
        long_description: str = None,
        description_style: TextStyle = None,
        action_area: bool = False,
        on_click_action_area: ControlEvent = None,
        width=300,
        **kwargs,
    ):
        super().__init__(**kwargs)

        self.bgcolor = "black"
        self.width = width
        self.border_radius = 10
        self.padding = padding.only(bottom=10)

        self.expanded = False

        self.expanded_container = Container(
            ListView([Text(long_description, style=description_style)], auto_scroll=1),
            visible=False,
            padding=padding.only(10, right=10),
            margin=margin.only(bottom=10),
            # height=200,
        )
        self.image_container = Container(
            Image(
                src=image_src,
                fit="cover",
                height=image_height,
                width=self.width,
            ),
            alignment=alignment.center,
            margin=margin.all(0),
            width=400,
        )
        # A container to contain all the actions
        self.actions_row = Container(
            Row(
                [
                    *(action for action in actions),
                    Row(expand=True),
                    Container(
                        IconButton(icons.ARROW_DROP_DOWN, on_click=self.toggle_expand)
                        if can_expand == True
                        else None
                    ),
                ],
                spacing=0,
                alignment="start",
            ),
            margin=margin.only(top=5, right=10),
        )

        self.content = Column(
            [
                self.image_container,
                Container(
                    Column(
                        [
                            Container(
                                Text(
                                    f"{title}",
                                    size=20,
                                    weight=FontWeight.BOLD,
                                    style=title_style,
                                )
                            ),
                            Text(description, style=description_style),
                        ],
                        spacing=5,
                    ),
                    padding=padding.only(left=10, top=10, right=10),
                ),
                self.actions_row,
                self.expanded_container,
            ],
            spacing=0,
        )
        self.shadow = [
            BoxShadow(
                spread_radius=6,
                blur_radius=10,
                color=colors.with_opacity(0.3, "black"),
                offset=Offset(0, 8),
            )
        ]
        # These events are trigged only if the action_area property True
        self.on_click = on_click_action_area
        self.on_hover = self.action_area if action_area else None

    # when the dropdown iconbutton is clicked
    def toggle_expand(self, e):
        self.expanded = not self.expanded
        self.expanded_container.visible = self.expanded
        e.control.icon = icons.ARROW_DROP_UP if self.expanded else icons.ARROW_DROP_DOWN
        self.update()

    # trigged when the action_area is set to True & the Card is hovered by a cursor
    def action_area(self, e):
        e.control.opacity = 0.7 if e.data == "true" else 1.0
        e.control.update()


def Card_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text("CardMedia", size=24, weight=FontWeight.BOLD, color="#223631"),
                    padding=padding.only(30, top=15, bottom=10),
                ),
                Container(
                    content=Column(
                        [
                            Text(
                                "CardMedia is surface that displays content and actions related to a single topic.",
                                size=18,
                                color="black",
                            ),
                            ResponsiveRow(
                                [
                                    Column(
                                        [
                                            Text(
                                                "Card with a long-description:",
                                                weight=FontWeight.BOLD,
                                            ),
                                            CardMedia(
                                                image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
                                                description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
                                                description_style=TextStyle(
                                                    color="white"
                                                ),
                                                actions=[
                                                    TextButton("SHARE"),
                                                    TextButton("LEARN MORE"),
                                                ],
                                                can_expand=True,
                                                long_description="""
Ils partagent le fait d'avoir quatre pattes (hormis les orvets), des oreilles à tympan apparent sans conduit auditif externe, le corps recouvert d'écailles et la mue. Certaines familles emblématiques du terme générique de "lézard", comme les Lacertidae, peuvent perdre volontairement leur queue (autotomie) en cas d'agression et ont des paupières mobiles.
""",
                                                title_style=TextStyle(color="white"),
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Card without a long-description:",
                                                weight=FontWeight.BOLD,
                                            ),
                                            CardMedia(
                                                image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
                                                description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
                                                actions=[
                                                    TextButton("SHARE"),
                                                    TextButton("LEARN MORE"),
                                                ],
                                                description_style=TextStyle(
                                                    color="white"
                                                ),
                                                title_style=TextStyle(color="white"),
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Card with an action area",
                                                weight=FontWeight.BOLD,
                                            ),
                                            CardMedia(
                                                image_src="https://th.bing.com/th/id/R.5e510c21c45cefceb127a2280c789b72?rik=2ddR7LkLmjAIFA&pid=ImgRaw&r=0",
                                                description="Lizards are a widespread group of squamate reptiles, with over 6,000 species, ranging across all continents except Antarctica",
                                                action_area=True,
                                                actions=[],
                                                description_style=TextStyle(
                                                    color="white"
                                                ),
                                                title_style=TextStyle(color="white"),
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                ],
                                # scroll="always",
                            ),
                        ],
                        # scroll="always",
                    ),
                    # width=page.width // 1.5,
                    padding=padding.only(30, right=30),
                ),
            ],
            scroll="always",
            alignment="start",
            horizontal_alignment="start",
        ),
        visible=True,
        expand=True,
        width=page.width // 1.1,
    )
    cont.alignment = alignment.center_left

    return cont
