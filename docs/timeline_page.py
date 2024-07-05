from flet import *
from fletura import Timeline


events = [
    {
        "title": "Event 1",
        "description": "This is the description for event 1.",
        "timestamp": "2023-01-01 10:00 AM",
        "dot_props": {
            "border": border.all(2, color="black"),
        },
        "content_position": 0,
        "separator_props": {
            "color": colors.BLACK,
            # "width": 3,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 25,
    },
    {
        "title": "Event 2",
        "description": "This is the description for event 2.",
        "timestamp": "2023-02-01 12:00 PM",
        "dot_props": {
            "border": border.all(2, color="black"),
        },
        "content_position": 0,
        "separator_props": {
            "color": colors.BLACK,
            # "width": 3,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 25,
    },
    {
        "title": "Event 3",
        "description": "This is the description for event 3.",
        "timestamp": "2023-03-01 02:00 PM",
        "dot_props": {
            "border": border.all(2, color="black"),
        },
        "content_position": 0,
        "separator_props": {
            "color": colors.BLACK,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 20,
    },
]

travel_events = [
    {
        "title": "Trip to Japan",
        "description": "Visited Tokyo and Kyoto.",
        "timestamp": "2023-04-05 08:00 AM",
        "dot_props": {
            "icon": icons.FLIGHT,
            "icon_size": 20,
            "icon_color": colors.ORANGE,
            "border": border.all(2, color="orange"),
        },
        "separator_props": {
            "color": colors.GREEN_200,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 20,
    },
    {
        "title": "Hiking Trip",
        "description": "Hiked in the Swiss Alps.",
        "timestamp": "2023-07-20 07:00 AM",
        "dot_props": {
            "icon": icons.TERRAIN,
            "icon_size": 20,
            "icon_color": colors.BROWN,
            "border": border.all(2, color="brown"),
        },
        "separator_props": {
            "color": colors.YELLOW_200,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 20,
    },
]

project_events = [
    {
        "title": "Project Kickoff",
        "description": "Initial meeting with the team.",
        "timestamp": "2023-01-01 10:00 AM",
        "dot_props": {
            "icon": icons.MEETING_ROOM,
            "icon_size": 20,
            "icon_color": colors.BLUE,
            "border": border.all(2, color="blue"),
        },
        "on_click": lambda _: ...,
        "separator_props": {
            "color": colors.GREEN_500,
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 25,
    },
    {
        "title": "Design Phase",
        "description": "Work on initial designs and wireframes.",
        "timestamp": "2023-02-01 12:00 PM",
        "dot_props": {
            "icon": icons.DESIGN_SERVICES,
            "icon_size": 20,
            "icon_color": colors.RED,
            "border": border.all(2, color="red"),
        },
        "separator_props": {
            "height": 70,
            "margin": margin.only(top=5),
        },
        "content_position": 25,
    },
]

timeline1 = Timeline(events)
timeline2 = Timeline(travel_events)
timeline3 = Timeline(project_events)


def Timeline_content(page):
    cont = Container(
        content=Column(
            [
                Container(
                    Text(
                        "Timeline Component",
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
                                "The Timeline component is a structured UI element designed to display a sequence of events or activities in a chronological order.",
                                size=18,
                                color="black",
                            ),
                            ResponsiveRow(
                                [
                                    Column(
                                        [
                                            Text(
                                                "Simple Timeline component",
                                                weight=FontWeight.BOLD,
                                            ),
                                            timeline1,
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Customized Timeline",
                                                weight=FontWeight.BOLD,
                                            ),
                                            timeline2,
                                        ],
                                        col={"sm": 6, "md": 4, "xl": 4},
                                    ),
                                    Column(
                                        [
                                            Text(
                                                "Timeline component with on_click event",
                                                weight=FontWeight.BOLD,
                                            ),
                                            timeline3,
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
