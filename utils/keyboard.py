from telegram import (
    ReplyKeyboardMarkup,
    Update,
)

REPLY_KEYBOARD = [
    ["đ° Balance", "âšī¸ Airdrop Info"],
    ["đ¸ Withdrawal", "đ Ref Link"],
    ["đž My Data", "Quit Airdrop"],
]


def create_markup(buttons):
    return ReplyKeyboardMarkup(buttons)


def get_reply_keyboard_markup():
    return ReplyKeyboardMarkup(REPLY_KEYBOARD)
