"""
    Minimalistic Icons
"""

import click
from PIL import Image, ImageColor, ImageDraw
import twemoji


@click.command()
@click.argument('color', type=click.STRING, required=True)
@click.argument('emoji', type=click.STRING)
@click.option('-s',
              '--size',
              type=click.INT,
              default=512,
              show_default=True,
              help='The size of image. Overrides `width` and `height` options.'
              )
@click.option('-w',
              '--width',
              type=click.INT,
              default=512,
              show_default=True,
              help='The width of image.')
@click.option('-h',
              '--height',
              type=click.INT,
              default=512,
              show_default=True,
              help='The height of image.')
@click.option('-f',
              '--file',
              type=click.STRING,
              default='image.png',
              show_default=True,
              help='Output file')
@click.option('-c',
              '--circle',
              type=click.BOOL,
              default=False,
              show_default=True,
              is_flag=True,
              help='Crop image in a circle')
# pylint: disable=too-many-arguments
def main(color, emoji, size, width, height, file, circle):
    """Create a minimalistic icon"""

    if size:
        width = size
        height = size

    if circle and width != height:
        raise click.UsageError(
            'Cropping image in a circle is only supported if width and height is equal.'
        )

    image_color = ImageColor.getrgb(color)

    image = Image.new('RGBA', (width, height),
                      image_color if not circle else None)
    draw = ImageDraw.Draw(image)

    if circle:
        draw.ellipse((0, 0, width, height), image_color)

    emoji_image_size = int(min(width, height) / 4)

    emoji_image = twemoji.get_emoji_image(emoji, emoji_image_size)

    image.paste(emoji_image, (int(width / 2 - emoji_image_size / 2),
                              int(height / 2 - emoji_image_size / 2)),
                mask=emoji_image.split()[3])

    image.save(file)

    click.echo('Image created')


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
