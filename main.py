from flet import *


def main(page: Page):
    # Set up the page
    page.title = "Flet Components Documentation"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    # page.bgcolor = colors.GREY_100

    def hovered(e):
        e.control.opacity = 0.5 if e.control.opacity == 1.0 else 1.0
        e.control.update()

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

    indicator = Container(
        width=4,
        height=30,
        alignment=alignment.center_right,
        bgcolor="orange",
        offset=transform.Offset(0, 0),
        animate=animation.Animation(500, AnimationCurve.DECELERATE),
    )

    # sidebarmenu
    sidebar = Container(
        Column(
            [
                Container(
                    Column(
                        [
                            Container(
                                Image(
                                    src="light_logo.jpg",
                                    width=100,
                                    height=100,
                                ),
                                width=100,
                                height=100,
                                border_radius=50,
                                alignment=alignment.center,
                                margin=margin.only(top=15, bottom=0),
                            ),
                            Container(
                                Text(
                                    "PhoenixBusiness",
                                    size=15,
                                    weight=FontWeight.W_500,
                                ),
                                margin=margin.only(top=0),
                                padding=padding.only(top=0),
                                alignment=alignment.center,
                            ),
                        ],
                        horizontal_alignment=CrossAxisAlignment.CENTER,
                    ),
                    margin=margin.only(top=15, bottom=15),
                ),
                Divider(height=5, color=colors.with_opacity(0.5, "transparent")),
                Column(
                    [
                        Container(
                            Row(
                                [
                                    Icon(icons.DASHBOARD),
                                    Text("Home"),
                                    Row(expand=True),
                                    indicator,
                                ]
                            ),
                            padding=padding.only(10),
                            bgcolor=colors.with_opacity(0.2, "white"),
                            height=30,
                            opacity=1.0,
                            data=0,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "home"),
                        ),
                        Container(
                            Row(
                                [
                                    Icon(icons.PRODUCTION_QUANTITY_LIMITS_SHARP),
                                    Text("Neumorphic"),
                                ]
                            ),
                            padding=padding.only(10),
                            height=30,
                            opacity=1.0,
                            data=1,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "neumorphic_card"),
                        ),
                        Container(
                            Row([Icon(icons.FILE_COPY), Text("Ventes")]),
                            padding=padding.only(10),
                            opacity=1.0,
                            height=30,
                            data=2,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "progress_indicator"),
                        ),
                        Container(
                            Row([Icon(icons.ANALYTICS), Text("Analyses")]),
                            padding=padding.only(10),
                            opacity=1.0,
                            height=30,
                            data=3,
                            on_hover=hovered,
                            on_click=lambda e: ...,
                        ),
                    ],
                    spacing=0,
                ),
            ]
        ),
        width=200,
        height=700,
        bgcolor="#101415",
        alignment=alignment.center,
    )

    # Create a sidebar for navigation
    # sidebar = Container(
    #     width=200,
    #     bgcolor=colors.BLUE_700,
    #     padding=10,
    #     content=Column(
    #         [
    #             Text(
    #                 "Documentation", size=20, weight=FontWeight.BOLD, color=colors.WHITE
    #             ),
    #             Divider(color=colors.WHITE),
    #             TextButton(
    #                 "Home", icon=icons.HOME, on_click=lambda e: show_content("home")
    #             ),
    #             TextButton(
    #                 "Neumorphic Card",
    #                 on_click=lambda e: show_content("neumorphic_card"),
    #             ),
    #             TextButton("Timeline", on_click=lambda e: show_content("timeline")),
    #             TextButton(
    #                 "Progress Indicator",
    #                 on_click=lambda e: show_content("progress_indicator"),
    #             ),
    #         ],
    #         spacing=10,
    #     ),
    # )

    # # Function to show the selected content and hide the others
    menu_items: list = []

    def show_content(e, content_name):
        home_content.visible = content_name == "home"
        neumorphic_card_content.visible = content_name == "neumorphic_card"
        timeline_content.visible = content_name == "timeline"
        progress_indicator_content.visible = content_name == "progress_indicator"
        _removed = None
        menu_items.append(int(e.control.data))

        if len(menu_items) >= 2:
            _removed = menu_items.pop(0)

        if _removed != e.control.data:
            sidebar.content.controls[2].controls[_removed].bgcolor = (
                colors.with_opacity(0.0, "transparent")
            )
            sidebar.update()

        indicator.offset.y = e.control.data
        indicator.update()

        sidebar.content.controls[2].controls[int(e.control.data)].bgcolor = (
            colors.with_opacity(0.2, "white")
        )

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
