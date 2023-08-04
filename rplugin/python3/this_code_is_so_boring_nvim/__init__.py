import pynvim
from .player import Player
import cv2

@pynvim.plugin
class Test:
    def __init__(self, nvim):
        self.default_video = "https://ia801901.us.archive.org/14/items/xbdv-9403/XBDV9403.mp4"
        self.nvim = nvim
    @pynvim.command('ThisCodeIsSoBoring', range='', nargs='?', sync=True)
    def play(self, args, range):
        if len(args) == 0:
            video = cv2.VideoCapture(self.default_video)
        else:
            video = cv2.VideoCapture(args[0])
        player = Player(self.nvim, self.nvim.current.window, video)
        self.nvim.async_call(player.play)
    @pynvim.command('SetThisCodeIsSoBoringVideo', range='', nargs=1, sync=True)
    def set_default(self, args, range):
        self.default_video = args[0]
