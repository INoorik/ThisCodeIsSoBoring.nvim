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
        success, image = self.video.read()
        image = Image.fromarray(image)
        while success and self.window.valid:
            self.window.buffer[:] = self.renderer.render(self._resize_image_to_fit_window(image))
            sampling_period = 1/self.video.get(cv2.CAP_PROP_FPS)
            sleep(sampling_period)
    def _resize_image_to_fit_window(self, image):
        size = (self.window.width, self.window.height//2)
        return ImageOps.pad(image, size)
