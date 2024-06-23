from flet import *
import os
import markdown2


def main(page: Page):
    page.title = "Fletura Documentation"
    page.vertical_alignment = MainAxisAlignment.CENTER
    page.horizontal_alignment = CrossAxisAlignment.CENTER
    page.padding = 0

    page.add(
        Container(
            Stack(
                [
                    Container(
                        Text("Fletura Documentations", color="black"),
                        margin=margin.only(left=10, right=10),
                        height=50,
                        width=page.width,
                        bgcolor=colors.GREY_400,
                        padding=padding.only(10, right=10),
                    )
                ]
            ),
            expand=True,
            gradient=LinearGradient(
                colors=["#1a1a2e", "#16213e", "#0f3460", "#0b132b"]
            ),
        )
    )


app(target=main)
