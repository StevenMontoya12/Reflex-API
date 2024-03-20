# chatapp.py

import reflex as rx


def index() -> rx.Component:
    return rx.container(
        rx.box(
            "What is Reflex?",
            # The user's question is on the right.
            text_align="right",
        ),
        rx.box(
            "A way to build web apps in pure Python!",
            # The answer is on the left.
            text_align="left",
        ),
    )


# Add state and page to the app.
app = rx.App()
app.add_page(index)