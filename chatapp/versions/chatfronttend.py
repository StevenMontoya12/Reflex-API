# chatapp.py

import reflex as rx


def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(question, text_align="right"),
        rx.box(answer, text_align="left"),
        margin_y="1em",
    )


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


def chat() -> rx.Component:
    qa_pairs = [
        (
            "What is Reflex?",
            "A way to build web apps in pure Python!",
        ),
        (
            "What can I make with it?",
            "Anything from a simple website to a complex web app!",
        ),
              (
            "Que es Python?",
            "Python es un lenguaje de alto nivel de programación interpretado cuya filosofía hace hincapié en la legibilidad de su código",
        ),
    ]
    return rx.box(
        *[
            qa(question, answer)
            for question, answer in qa_pairs
        ]
    )


def index() -> rx.Component:
    return rx.container(chat())



# Add state and page to the app.
app = rx.App()
app.add_page(index)

