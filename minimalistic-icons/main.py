"""
    Minimalistic Icons
"""

import click
from PIL import Image, ImageColor

@click.command()
@click.argument('color', type=click.STRING, required=True)
@click.option('-s', '--size', type=click.INT, default=512, show_default=True,
              help='The size of image.')
@click.option('-f', '--file', type=click.STRING, default='image.png', show_default=True,
              help='Output file')
def main(color, size, file):
    """Create a minimalistic icon"""

    image_color = ImageColor.getrgb(color)
    image = Image.new('RGB', (size, size), image_color)

    image.save(file)

    click.echo('Image created')

if __name__ == '__main__':
    main() # pylint: disable=no-value-for-parameter
