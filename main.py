from flet import *
from docs import *
from time import sleep

PRIMARYCOLOR = "#223631"


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


def main(page: Page):

    def close_sidebar(e):
        state = e.control.data
        e.control.icon = icons.ARROW_FORWARD if state == False else icons.ARROW_BACK
        e.control.parent.parent.controls[0].width = 0 if state == False else 200
        e.control.data = not state
        e.control.parent.parent.update()

    def respo_page():
        if page.width <= 500:
            page.controls[0].controls[1].controls[-1].visible = True

        else:
            page.controls[0].controls[1].controls[-1].visible = False
        page.update()

    # On resize event
    def on_resized_event(e):
        respo_page()

    page.bgcolor = colors.GREY_300
    page.title = "Flet Components Documentation"
    page.horizontal_alignment = "center"
    page.vertical_alignment = "start"
    page.padding = 0
    page.theme_mode = "light"
    page.on_resized = on_resized_event

    def hovered(e):
        e.control.opacity = 0.5 if e.control.opacity == 1.0 else 1.0
        e.control.update()

    def change_scale(e):
        e.control.scale = 1.3 if e.data == "true" else 1
        e.control.update()

    def fletura_source_code(e):
        page.launch_url("https://github.com/Benitmulindwa/fletura")

    def open_searchbar(e):
        state = e.control.data
        (
            e.control.parent.parent.controls.insert(
                0,
                Container(
                    TextField(
                        # border=None,
                        height=30,
                        width=page.width // 6,
                        bgcolor="#f0f0f0",
                        content_padding=8,
                        border_color=PRIMARYCOLOR,
                        cursor_color="#4b4b4b",
                        hint_text="Search",
                        text_style=TextStyle(weight=FontWeight.W_600),
                    ),
                    offset=transform.Offset(-1, 0),
                    animate_offset=animation.Animation(400, AnimationCurve.DECELERATE),
                ),
            )
            if state == False
            else e.control.parent.parent.controls.pop(0)
        )
        page.update()
        sleep(0.05)
        e.control.parent.parent.controls[0].offset = transform.Offset(0, 0)
        e.control.icon = icons.CLOSE if state == False else icons.SEARCH
        e.control.data = not state
        page.update()

    # Create the main content containers for each section
    card_content = Card_content(page)
    dock_content = Dock_content(page)
    paper_content = Paper_content(page)
    neumorphic_card_content = Neumorphic_content(page)
    timeline_content = Timeline_content(page)
    rating_content = Rating_content(page)
    switch_content = Switch_content(page)

    # ___________________________________________________________________________________________________________________________#
    # Indicator
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
                                border_radius=50,
                                alignment=alignment.center,
                                margin=margin.only(top=15, bottom=0),
                            ),
                            Container(
                                Text(
                                    "FLETURA",
                                    size=25,
                                    weight=FontWeight.W_500,
                                    color=colors.GREY_300,
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
                                    Text(
                                        "Card",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    ),
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
                                    Text(
                                        "Neumorphic",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    ),
                                ]
                            ),
                            padding=padding.only(10),
                            height=30,
                            opacity=1.0,
                            data=1,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "neumorphic"),
                        ),
                        Container(
                            Row(
                                [
                                    Text(
                                        "Rating",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    )
                                ]
                            ),
                            padding=padding.only(10),
                            opacity=1.0,
                            height=30,
                            data=2,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "rating"),
                        ),
                        Container(
                            Row(
                                [
                                    Text(
                                        "Timeline",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    )
                                ]
                            ),
                            padding=padding.only(10),
                            opacity=1.0,
                            height=30,
                            data=3,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "timeline"),
                        ),
                        Container(
                            Row(
                                [
                                    Text(
                                        "Dock",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    ),
                                    Row(expand=True),
                                ]
                            ),
                            padding=padding.only(10),
                            height=30,
                            opacity=1.0,
                            data=4,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "dock"),
                        ),
                        Container(
                            Row(
                                [
                                    Text(
                                        "Paper",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    ),
                                    Row(expand=True),
                                ]
                            ),
                            padding=padding.only(10),
                            height=30,
                            opacity=1.0,
                            data=5,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "paper"),
                        ),
                        Container(
                            Row(
                                [
                                    Text(
                                        "Switch",
                                        weight=FontWeight.W_500,
                                        size=17,
                                        color=colors.GREY_100,
                                    ),
                                    Row(expand=True),
                                ]
                            ),
                            padding=padding.only(10),
                            height=30,
                            opacity=1.0,
                            data=6,
                            on_hover=hovered,
                            on_click=lambda e: show_content(e, "switch"),
                        ),
                    ],
                    spacing=0,
                ),
                Column(expand=True),
                Text("Built with 💕", size=12, color="orange"),
            ]
        ),
        width=200,
        height=700,
        bgcolor=PRIMARYCOLOR,
        alignment=alignment.center,
    )

    def hovered(e):
        e.control.opacity = 0.5 if e.control.opacity == 1.0 else 1.0
        e.control.update()

    # # Function to show the selected content and hide the others
    menu_items: list = []

    def show_content(e, content_name):
        card_content.visible = content_name == "home"
        neumorphic_card_content.visible = content_name == "neumorphic"
        timeline_content.visible = content_name == "timeline"
        rating_content.visible = content_name == "rating"
        dock_content.visible = content_name == "dock"
        paper_content.visible = content_name == "paper"
        switch_content.visible = content_name == "switch"
        _removed = 0
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
                Stack(
                    [
                        sidebar,
                    ]
                ),
                Column(
                    [
                        FlatContainer(
                            content=Row(
                                [
                                    Container(
                                        IconButton(
                                            icons.SEARCH,
                                            icon_color="#223631",
                                            padding=padding.all(-100),
                                            data=False,
                                            on_click=open_searchbar,
                                        ),
                                        on_hover=change_scale,
                                    ),
                                    Container(
                                        Image(
                                            src="github_icon.png",
                                            height=40,
                                            width=40,
                                        ),
                                        margin=margin.only(-10),
                                        on_hover=change_scale,
                                        on_click=fletura_source_code,
                                    ),
                                ],
                                alignment="end",
                            ),
                            width=page.width // 1.1,
                            height=50,
                            margin=margin.only(0, 15, 10),
                        ),
                        Divider(
                            height=5,
                            color=colors.with_opacity(0.5, "orange"),
                        ),
                        Stack(
                            [
                                card_content,
                                neumorphic_card_content,
                                timeline_content,
                                rating_content,
                                dock_content,
                                paper_content,
                                switch_content,
                            ],
                            expand=True,
                        ),
                        IconButton(
                            icons.ARROW_BACK,
                            icon_color="orange",
                            on_click=close_sidebar,
                            data=False,
                            # visible=False,
                            icon_size=40,
                        ),
                    ],
                    expand=True,
                ),
            ],
            expand=True,
        )
    )
    respo_page()
    page.update()


if __name__ == "__main__":
    app(target=main, assets_dir="assets")
