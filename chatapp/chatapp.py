# chatapp.py
import reflex as rx

from chatapp import style
from chatapp.state import State

def qa(question: str, answer: str) -> rx.Component:
    return rx.box(
        rx.box(
            rx.text(question, text_align="right"),
            style=style.question_style,
        ),
        rx.box(
            rx.text(answer, text_align="left"),
            style=style.answer_style,
        ),
        margin_y="1em",
    )


def chat() -> rx.Component:
    return rx.box(
        rx.foreach(
            State.chat_history,
            lambda messages: qa(messages[0], messages[1]),
        )
    )


def action_bar() -> rx.Component:
    return rx.hstack(
        rx.chakra.input(
            value=State.question,
            placeholder="Has una pregunta..",
            on_change=State.set_question,
            style=style.input_style,
        ),
        rx.button(
            "Aceptar",
            on_click=State.answer,
            style=style.button_style,
        ),
    )


def index() -> rx.Component:
    return rx.container(
        rx.box(
            rx.text("Hola soy ChatGPT\nTe ayudaré a resolver tus dudas", text_align="center"),
            style={"margin-top": "20px", "color": " #a351ca", "font-size": "18px", "font-weight": "700"}  # Estilos del cuadro de texto
        ),
        chat(),
        action_bar(),
       
        )






app = rx.App()
app.add_page(index)

