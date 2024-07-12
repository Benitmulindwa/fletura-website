from flet import *


class Switch(Container):
    def __init__(
        self,
        track_width: int = 60,
        track_height: int = 25,
        track_style: dict = {},
        active_track_content: Control = None,
        inactive_track_content: Control = None,
        thumb_width: int = 40,
        thumb_height: int = 40,
        active_thumb_content: Control = None,
        inactive_thumb_content: Control = None,
        default_thumb_content: Control = None,
        thumb_style: dict = None,
        active_color: str = "green",
        inactive_color: str = "grey",
        label: str = None,
        label_style: TextStyle = None,
        value: bool = False,
        on_hover: HoverEvent = None,
        on_change: ControlEvent = None,
    ):
        super().__init__(on_hover=on_hover)

        self.track_width = track_width
        self.track_height = track_height
        self.track_style = track_style
        self.active_track_content = active_track_content
        self.inactive_track_content = inactive_track_content
        self.thumb_width = thumb_width
        self.thumb_height = thumb_height
        self.active_thumb_content = active_thumb_content
        self.inactive_thumb_content = inactive_thumb_content
        self.default_thumb_content = (
            inactive_thumb_content
            if default_thumb_content == None
            else default_thumb_content
        )
        self.thumb_style = thumb_style or {
            "bgcolor": "white",
            "border_radius": 20,
        }
        self.active_color = active_color
        self.inactive_color = inactive_color
        self.label = label
        self.label_style = label_style
        self.on_change = on_change

        self.value = value  # initial state
        self.create_switch()

    def create_switch(self):
        # Create the switch components and layout.

        x_offset, y_offset = self.calculate_offsets()

        self.switch_thumb = Container(
            self.default_thumb_content,
            width=self.thumb_width,
            height=self.thumb_height,
            offset=transform.Offset(0 if self.value == False else -x_offset, -y_offset),
            animate_offset=animation.Animation(200, AnimationCurve.DECELERATE),
            **self.thumb_style,
        )

        self.switch_track = Container(
            self.inactive_track_content,
            width=self.track_width,
            height=self.track_height,
            bgcolor=self.inactive_color,
            border_radius=self.track_height / 2,
            **self.track_style,
        )
        self.switch_track.alignment = (
            alignment.center_left if self.value else alignment.center_right
        )

        self.switch_container = Container(
            content=Stack([self.switch_track, self.switch_thumb]),
            on_click=self.switch_changed,
            alignment=alignment.center,
        )
        self.label_text = Text(self.label, style=self.label_style)

        self.content = Row(
            [self.switch_container, self.label_text],
            alignment="center",
            vertical_alignment="center",
        )

        self.padding = padding.only(bottom=0, top=0)

    def calculate_offsets(self):
        # Calculate the offsets for centering the thumb.
        x_offset = (self.thumb_width - self.track_width) / (
            self.track_width / (self.track_width / self.thumb_width)
        )
        y_offset = (self.thumb_height - self.track_height) / (
            self.thumb_height / (self.track_height * 0.4) * self.track_height
        )
        return x_offset, y_offset

    def update_switch_state(self):

        x_offset, y_offset = self.calculate_offsets()

        self.switch_thumb.offset = (
            transform.Offset(-x_offset, -y_offset)
            if self.value
            else transform.Offset(0, -y_offset)
        )
        self.switch_thumb.content = (
            self.active_thumb_content if self.value else self.inactive_thumb_content
        )
        self.switch_track.bgcolor = (
            self.active_color if self.value else self.inactive_color
        )
        self.switch_track.content = (
            self.active_track_content if self.value else self.inactive_track_content
        )
        self.switch_track.alignment = (
            alignment.center_left if self.value else alignment.center_right
        )
        self.switch_thumb.update()
        self.switch_track.update()

    def switch_changed(self, e):
        self.value = not self.value
        self.update_switch_state()
        if self.on_change:
            self.on_change(self)


def Switch_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Switch Component",
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
                                "The Switch component  is a customizable switch control for toggling between two states. It provides various customization options for its appearance and behavior, including track and thumb styling, content, colors, and events.\n Examples:",
                                size=18,
                                color="black",
                            ),
                            ResponsiveRow(
                                [
                                    Column(
                                        [
                                            Text(
                                                "Basic Switch component",
                                                weight=FontWeight.BOLD,
                                            ),
                                            Switch(),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Switch with a small thumb",
                                                weight=FontWeight.BOLD,
                                            ),
                                            # Small thumb
                                            Switch(
                                                label="Small thumb",
                                                thumb_height=20,
                                                thumb_width=20,
                                                active_color="blue",
                                                inactive_color="red",
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Switch",
                                                weight=FontWeight.BOLD,
                                            ),
                                            # Switch with all customizations
                                            Switch(
                                                label="Fully Customized",
                                                track_width=120,
                                                track_height=60,
                                                thumb_width=70,
                                                thumb_height=70,
                                                active_thumb_content=Icon(
                                                    icons.POWER, color="white"
                                                ),
                                                inactive_thumb_content=Icon(
                                                    icons.POWER_OFF, color="white"
                                                ),
                                                active_color="green",
                                                inactive_color="red",
                                                track_style={
                                                    "gradient": RadialGradient(
                                                        colors=["purple", "blue"]
                                                    )
                                                },
                                                thumb_style={
                                                    "gradient": LinearGradient(
                                                        colors=["yellow", "orange"]
                                                    ),
                                                    "border_radius": 40,
                                                },
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Switch With background images",
                                                weight=FontWeight.BOLD,
                                            ),
                                            Switch(  # Large Thumb and Track
                                                label="Track with background Images",
                                                track_width=100,
                                                active_track_content=Image(
                                                    src="https://picsum.photos/200/200?3",
                                                    fit=ImageFit.FIT_WIDTH,
                                                    width=100,
                                                ),
                                                inactive_track_content=Image(
                                                    src="https://picsum.photos/200/200?0",
                                                    fit=ImageFit.FIT_WIDTH,
                                                    width=100,
                                                ),
                                                track_height=50,
                                                thumb_width=60,
                                                thumb_height=60,
                                                value=True,
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Switch with a square thumb",
                                                weight=FontWeight.BOLD,
                                            ),
                                            # Custom Track Gradient & squared thumb
                                            Switch(
                                                label="Gradient Track",
                                                track_width=100,
                                                track_style={
                                                    "gradient": LinearGradient(
                                                        colors=[
                                                            "red",
                                                            "orange",
                                                            "blue",
                                                            "yellow",
                                                            "#f5f5f5",
                                                        ]
                                                    )
                                                },
                                                thumb_style={
                                                    "gradient": RadialGradient(
                                                        colors=[
                                                            "blue",
                                                            "yellow",
                                                            "orange",
                                                        ]
                                                    )
                                                },
                                            ),
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Switch with track contents ",
                                                weight=FontWeight.BOLD,
                                            ),
                                            # Switch with track contents
                                            Switch(
                                                track_width=100,
                                                thumb_height=40,
                                                thumb_width=40,
                                                active_color="green",
                                                inactive_color="grey",
                                                inactive_thumb_content=Icon(
                                                    icons.LIGHT_MODE
                                                ),
                                                active_thumb_content=Icon(
                                                    icons.DARK_MODE
                                                ),
                                                active_track_content=Icon(
                                                    icons.LIGHT_MODE
                                                ),
                                                inactive_track_content=Icon(
                                                    icons.DARK_MODE
                                                ),
                                                track_style={
                                                    "border": border.all(1, "white100"),
                                                },
                                            ),
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
