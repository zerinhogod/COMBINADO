from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▶️", callback_data="resume_cb"),
            InlineKeyboardButton(text="⏸️", callback_data="pause_cb"),
            InlineKeyboardButton(text="⏩️", callback_data="skip_cb"),
            InlineKeyboardButton(text="⏹️", callback_data="end_cb"),
        ]
    ]
)

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="FECHAR", callback_data="close")]]
)
