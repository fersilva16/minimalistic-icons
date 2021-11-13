"""
    Parse and get twemojis
"""

from io import BytesIO
import cairosvg
from PIL import Image
import requests


def get_emoji_image(char, size):
    """Get twemoji image"""

    request = requests.get(
        f'https://twemoji.maxcdn.com/v/latest/svg/{ord(char[0]):x}.svg')

    out = BytesIO()

    cairosvg.svg2png(
        bytestring=request.content,
        write_to=out,
        output_width=size,
        output_height=size,
    )

    return Image.open(out).convert('RGBA')
