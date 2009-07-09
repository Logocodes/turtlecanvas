from PIL import Image
from PIL.ImageColor import colormap


class Renderer(object):

    def __init__(self, width=320, height=240, background=colormap['white']):
        self.width = width
        self.height = height
        self.image = Image.new('RGB', (width, height), background)
