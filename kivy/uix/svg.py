
'''
SVG widget
'''

__all__ = ('SVG', )

from kivy.uix.widget import Widget
from kivy.properties import StringProperty
from kivy.graphics.svg import SVGData


class SVG(Widget):
    """
    SVG Widget:  basic widget that reads an svg file and draws the contents
    """
    #: Filename of the svg graphic
    source = StringProperty(None)

    #: SVG data element
    def on_source(self, instance, value):
        print "laoding", value
        self.svg_data = SVGData(value)


if __name__ == '__main__':
    from kivy.app import App
    from sys import argv
    class SVGApp(App):
        def build(self):
            return SVG(source=argv[1])
    SVGApp().run()
