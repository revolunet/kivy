__all__ = ('WindowFake')

from . import WindowBase
from kivy.base import EventLoop

class WindowFake(WindowBase):
    def mainloop(self):
        while not EventLoop.quit and EventLoop.status == 'started':
            EventLoop.idle()
