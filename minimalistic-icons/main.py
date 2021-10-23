"""
    Minimalistic Icons
"""

import click
from PIL import Image, ImageColor
import twemoji


@click.command()
@click.argument('color', type=click.STRING, required=True)
@click.argument('emoji', type=click.STRING)
@click.option('-s',
              '--size',
              type=click.INT,
              default=512,
              show_default=True,
              help='The size of image.')
@click.option('-f',
              '--file',
              type=click.STRING,
              default='image.png',
              show_default=True,
              help='Output file')
def main(color, emoji, size, file):
    """Create a minimalistic icon"""

    image_color = ImageColor.getrgb(color)

    image = Image.new('RGBA', (size, size), image_color)

    emoji_image_size = int(size / 4)

    emoji_image = twemoji.get_emoji_image(emoji).resize(
        (emoji_image_size, emoji_image_size))

    emoji_image_offset = int(size / 2 - emoji_image_size / 2)

    image.paste(emoji_image, (emoji_image_offset, emoji_image_offset),
                mask=emoji_image.split()[3])

    image.save(file)

    click.echo('Image created')


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
