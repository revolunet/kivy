__all__ = ('WindowFake')

from . import WindowBase
from kivy.base import EventLoop

class WindowFake(WindowBase):
    def mainloop(self):
        while not EventLoop.quit and EventLoop.status == 'started':
            EventLoop.idle()

    def create_window(self):
        from kivy.core.gl import glGetIntegerv, GL_VIEWPORT
        viewport = glGetIntegerv(GL_VIEWPORT)
        print 'VIEWPORT===>', viewport
        self._size = viewport[2:]
        super(WindowFake, self).create_window()
        self.dispatch('on_resize', *self._size)

    def flip(self):
        from kivy.core.gl import glEnable
        # act as a frame flip trigger for hijacking lib.
        glEnable(0x9999)
