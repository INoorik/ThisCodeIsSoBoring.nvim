from PIL import Image
from PIL import ImageOps
import cv2
from .image_render import ImageRenderer
from time import sleep

class Player:
    def __init__(self, nvim, window, video):
        self.nvim = nvim
        self.window = window
        self.video = video
        self.renderer = ImageRenderer()
    def play(self):
        self.nvim.funcs.nvim_set_option_value('number', False, {'scope': 'local', 'win': self.window})  
        self.nvim.funcs.nvim_set_option_value('relativenumber', False, {'scope': 'local', 'win': self.window})  
        success, image = self.video.read()
        image = Image.fromarray(image)
        while success and self.window.valid:
            self.window.buffer[:] = self.renderer.render(self._resize_image_to_fit_window(image))
            success, image = self.video.read()
            image = Image.fromarray(image)
            sampling_period = 1/self.video.get(cv2.CAP_PROP_FPS)
            sleep(sampling_period)
    def _resize_image_to_fit_window(self, image):
        graphic_size = (self.window.width-1, self.window.height*2)
        symbol_size = (self.window.width-1, self.window.height)
        return ImageOps.pad(image, graphic_size).resize(symbol_size)
