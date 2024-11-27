import os
from datetime import datetime

# Made by itstermoh

class Colors:
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN = (0, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (0, 0, 255)
    PINK = (255, 192, 203)
    PURPLE = (160, 32, 240)

    WHITE = (255, 255, 255)
    GRAY = (128, 128, 128)
    BLACK = (0, 0, 0)

class Styles:
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    ITALIC = '\033[3m'
    STRIKETHROUGH = '\033[9m'
    RESET = '\033[0m'

def interpolate_color(start, end, factor):
    return int(start + (end - start) * factor)

def hex2rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 3:
        hex_color = ''.join([c*2 for c in hex_color])
    return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))

def _print(text, start_color, end_color, style=None):
    os.system('')

    gradient_text = ""
    for i, char in enumerate(text):
        factor = i / (len(text) - 1)
        r = interpolate_color(start_color[0], end_color[0], factor)
        g = interpolate_color(start_color[1], end_color[1], factor)
        b = interpolate_color(start_color[2], end_color[2], factor)

        color_code = f"\033[38;2;{r};{g};{b}m"
        gradient_text += color_code + char

    if style:
        gradient_text = style + gradient_text

    gradient_text += Styles.RESET
    print(datetime.utcnow().strftime("%H:%M:%S") + "  ➤    " + gradient_text)

def banner(text, start_color, end_color, steps=10, style=None):
    os.system('')

    parts = text.split("\n")

    for i, line in enumerate(parts):
        factor = i / (steps - 1)
        r = interpolate_color(start_color[0], end_color[0], factor)
        g = interpolate_color(start_color[1], end_color[1], factor)
        b = interpolate_color(start_color[2], end_color[2], factor)

        color_code = f"\033[38;2;{r};{g};{b}m"
        styled_line = (style if style else "") + color_code + line
        print(styled_line)

    print(Styles.RESET)