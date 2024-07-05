from flet import *
from fletura import CardMedia


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
