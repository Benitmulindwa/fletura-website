from flet import *


def main(page: Page):
    # Set up the page
    page.title = "Flet Components Documentation"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    # page.bgcolor = colors.GREY_100

    # Create the main content containers for each section
    home_content = Container(
        Column(
            [
                Text(
                    "Welcome to Flet Components Documentation",
                    size=24,
                    weight=FontWeight.BOLD,
                )
            ],
            alignment="center",
            horizontal_alignment="center",
        ),
        visible=True,
        expand=True,
    )

    neumorphic_card_content = Container(
        Column(
            [
                Text("Neumorphic Card", size=24, weight=FontWeight.BOLD),
                Text("Description:", size=18, weight=FontWeight.BOLD),
                Text(
                    "The Neumorphic Card component is a customizable card with neumorphism and blur effects."
                ),
                Text("Usage:", size=18, weight=FontWeight.BOLD),
                Text("Example:", size=18, weight=FontWeight.BOLD),
            ],
            spacing=10,
        ),
        visible=False,
        expand=True,
    )

    timeline_content = Container(
        Column(
            [Text("Timeline", size=24, weight=FontWeight.BOLD)],
            alignment="center",
            horizontal_alignment="center",
        ),
        visible=False,
        expand=True,
    )

    progress_indicator_content = Container(
        Column(
            [Text("Progress Indicator", size=24, weight=FontWeight.BOLD)],
            alignment="center",
            horizontal_alignment="center",
        ),
        visible=False,
        expand=True,
    )

    # Create a sidebar for navigation
    sidebar = Container(
        width=200,
        bgcolor=colors.BLUE_700,
        padding=10,
        content=Column(
            [
                Text(
                    "Documentation", size=20, weight=FontWeight.BOLD, color=colors.WHITE
                ),
                Divider(color=colors.WHITE),
                TextButton("Home", on_click=lambda e: show_content("home")),
                TextButton(
                    "Neumorphic Card",
                    on_click=lambda e: show_content("neumorphic_card"),
                ),
                TextButton("Timeline", on_click=lambda e: show_content("timeline")),
                TextButton(
                    "Progress Indicator",
                    on_click=lambda e: show_content("progress_indicator"),
                ),
            ],
            spacing=10,
        ),
    )

    # Function to show the selected content and hide the others
    def show_content(content_name):
        home_content.visible = content_name == "home"
        neumorphic_card_content.visible = content_name == "neumorphic_card"
        timeline_content.visible = content_name == "timeline"
        progress_indicator_content.visible = content_name == "progress_indicator"
        page.update()

    # Add everything to the page
    page.add(
        Row(
            [
                sidebar,
                Stack(
                    [
                        home_content,
                        neumorphic_card_content,
                        timeline_content,
                        progress_indicator_content,
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )


if __name__ == "__main__":
    app(target=main)
