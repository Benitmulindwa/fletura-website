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
                                            "Rating Type:",
                                            size=18,
                                            color="black",
                                        ),
                                        margin=margin.only(top=20),
                                    ),
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
                # ________________ratingsize________________________
                Container(
                    content=Column(
                        [
                            Container(
                                Text(
                                    "Rating size:",
                                    size=18,
                                    color="black",
                                ),
                                margin=margin.only(top=20),
                            ),
                            Column(
                                [
                                    Container(
                                        Text(
                                            "Small",
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
                                        size="small",
                                    ),
                                ]
                            ),
                            Column(
                                [
                                    Text(
                                        "Medium",
                                        weight=FontWeight.BOLD,
                                    ),
                                    Rating(
                                        color="#223631",
                                        max_value=5,
                                        selection_icon=icons.STAR,
                                        rating_value=2.5,
                                        rating_type=RatingType.READONLY,
                                        size="medium",
                                    ),
                                ]
                            ),
                            Column(
                                [
                                    Text(
                                        "Large",
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
                                        "Extralarge",
                                        weight=FontWeight.BOLD,
                                    ),
                                    Rating(
                                        color="#223631",
                                        max_value=5,
                                        rating_value=1.5,
                                        rating_type=RatingType.DISABLED,
                                        size="extralarge",
                                    ),
                                ],
                            ),
                        ],
                    ),
                    padding=padding.only(30, right=30, bottom=30),
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
