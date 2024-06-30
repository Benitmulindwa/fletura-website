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
                            Row(
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
                                                long_description="""To make the container expand when the drop-down icon is clicked, you can add a callback function that toggles the expansion of the description. This involves updating the visibility and possibly the size of the container when the icon is clicked. Here's how you can implement this:
Ils partagent le fait d'avoir quatre pattes (hormis les orvets), des oreilles à tympan apparent sans conduit auditif externe, le corps recouvert d'écailles et la mue. Certaines familles emblématiques du terme générique de "lézard", comme les Lacertidae, peuvent perdre volontairement leur queue (autotomie) en cas d'agression et ont des paupières mobiles.
""",
                                                title_style=TextStyle(color="white"),
                                            ),
                                        ]
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
                                        ]
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
                                    ),
                                ],
                                scroll="always",
                            ),
                            Text("CardMedia properties:"),
                            Text("image_src", weight=FontWeight.BOLD),
                            Text("title", weight=FontWeight.BOLD),
                            Text("image_src", weight=FontWeight.BOLD),
                            Text("description", weight=FontWeight.BOLD),
                            Text("long-description", weight=FontWeight.BOLD),
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
        # height=500,
        width=page.width // 1.1,
        # alignment=alignment.top_left,
    )
    cont.alignment = alignment.center_left

    return cont
