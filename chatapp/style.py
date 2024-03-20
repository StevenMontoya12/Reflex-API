# style.py

# Common styles for questions and answers.
shadow = "rgba(0, 0, 0, 0.18) 0px 2px 8px"
chat_margin = "20%"
message_style = dict(
    padding="1em",
    border_radius="5px",
    margin_y="0.5em",
    box_shadow=shadow,
)

# Set specific styles for questions and answers.
question_style = message_style | dict(
    bg="#F5EFFE", margin_left=chat_margin
)
answer_style = message_style | dict(
    bg="#DEEAFD", margin_right=chat_margin
)

# Styles for the action bar.
input_style = dict(
    border_width="1px", padding="1em", box_shadow=shadow
)
button_style = dict(
    background_color="purple", box_shadow=shadow , margin_top="1.5em"
)


background_style = dict(
    background_color="grey",
    flex=1
)

