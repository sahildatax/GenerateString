from pyrogram.types import InlineKeyboardButton


class Data:
    # Start Message
    START = """
Halo {}

Welcome To {}

Session Generator Bot
    """

    # Home Button
    home_buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton(text="🏠 Return 🏠", callback_data="home")]
    ]

    generate_button = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")]
    ]

    # Rest Buttons
    buttons = [
        [InlineKeyboardButton("🔥 Start Generating Session 🔥", callback_data="generate")],
        [InlineKeyboardButton("✨ Maintaned By Sahil✨", url="https://t.me/sahil_nolia")],
        [
            InlineKeyboardButton("Help ❔", callback_data="help"),
            InlineKeyboardButton("🎪 About 🎪", callback_data="about")
        ],
        [InlineKeyboardButton("♥ Bot Info ♥", url="https://t.me/rioprojects")],
    ]

    # Help Message
    HELP = """
✨ **Available Commands** ✨

/help - This Message
/start - Check Dead or Alive
/generate - Generate Session
/cancel - Cancel process
/restart - Restart process
"""

    # About Message
    ABOUT = """
This is a Session Generator Bot


    """
