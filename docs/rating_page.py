from flet import *
from fletura import Rating, RatingType


def Rating_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Rating",
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
                                "Ratings provide insight regarding others' opinions and experiences, and can allow the user to submit a rating of their own.",
                                size=18,
                                color="black",
                            ),
                            Column(
                                [
                                    Container(
                                        Text(
                                            "Controlled",
                                            weight=FontWeight.BOLD,
                                        ),
                                        padding=padding.only(top=20),
                                    ),
                                    Rating(
                                        color="#223631",
                                        rating_icon=icons.STAR_OUTLINE_OUTLINED,
                                        selection_icon=icons.STAR,
                                        max_value=5,
                                        rating_type=RatingType.CONTROLLED,
                                    ),
                                ]
                            ),
                            Column(
                                [
                                    Text(
                                        "Read Only",
                                        weight=FontWeight.BOLD,
                                    ),
                                    Rating(
                                        color="#223631",
                                        max_value=5,
                                        selection_icon=icons.STAR,
                                        rating_value=2.5,
                                        rating_type=RatingType.READONLY,
                                        size="large",
                                    ),
                                ]
                            ),
                            Column(
                                [
                                    Text(
                                        "Disabled",
                                        weight=FontWeight.BOLD,
                                    ),
                                    Rating(
                                        color="#223631",
                                        max_value=5,
                                        rating_value=1.5,
                                        rating_type=RatingType.DISABLED,
                                    ),
                                ],
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
