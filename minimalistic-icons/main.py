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
@click.option('-o',
              '--output',
              type=click.STRING,
              default='output.png',
              show_default=True,
              help='Output file path.')
@click.option('-c',
              '--circle',
              type=click.BOOL,
              default=False,
              show_default=True,
              is_flag=True,
              help='Crop image in a circle.')
# pylint: disable=too-many-arguments
def main(color, emoji, size, width, height, output, circle):
    """Create a minimalistic icon"""

    if size:
        width = size
        height = size

    if circle and width != height:
        raise click.UsageError(
            'Cropping image in a circle is only supported if width and height is equal.'
        )

    background_color = ImageColor.getrgb(color)

    background = Image.new('RGBA', (width, height),
                           background_color if not circle else None)
    background_draw = ImageDraw.Draw(background)

    if circle:
        background_draw.ellipse((0, 0, width, height), background_color)

    foreground = Image.new('RGBA', background.size)

    emoji_image = twemoji.get_emoji_image(emoji, int(min(width, height) / 4))

    foreground.paste(
        emoji_image,
        tuple(
            int(background_dim / 2 - emoji_dim / 2) for background_dim,
            emoji_dim in zip(foreground.size, emoji_image.size)))

    image = Image.alpha_composite(background, foreground)

    image.save(output)

    click.echo('Image created')


if __name__ == '__main__':
    main()  # pylint: disable=no-value-for-parameter
