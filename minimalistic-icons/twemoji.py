"""
    Parse and get twemojis
"""

from io import BytesIO
import requests
from PIL import Image
# from svglib.svglib import svg2png


def get_emoji_image(char):
    """Get twemoji image"""

    request = requests.get(
        f'https://twemoji.maxcdn.com/v/latest/72x72/{ord(char[0]):x}.png')

    return Image.open(BytesIO(request.content)).convert('RGBA')
