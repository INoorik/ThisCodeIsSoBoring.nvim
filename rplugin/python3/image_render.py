from PIL import Image

class ImageRenderer:
    def __init__(self, characters = \
                 '¶@ØÆMåBNÊßÔR#8Q&mÃ0À$GXZA5ñk2S%±3Fz¢yÝCJf1t7ªLc¿+?(r/¤²!*;"^:,\'.` '):
        self.characters = characters
    def _get_character_by_pixel(self, pixel):
        blackwhite_pixel = sum(pixel[:3])//min(len(pixel), 3)
        character_index = blackwhite_pixel*len(self.characters)//257;
        return self.characters[::-1][character_index];
    def render(self, image):
        result = []
        for y in range(image.height):
            line = ''
            for x in range(image.width):
                line += self._get_character_by_pixel(image.getpixel((x, y)))
            result.append(line)
        return result

