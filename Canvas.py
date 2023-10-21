import cairo
from math import pi, sqrt
import GateElement

class Canvas(object):

    def __init__(self, filename, width, height):
        self.surface = cairo.SVGSurface(filename + '.svg', width, height)
        cr = self.cr = cairo.Context(self.surface)
        cr.scale(width, height)
        cr.set_line_width(0.1)

        cr.rectangle(0, 0, 1, 1)
        cr.set_source_rgb(1, 1, 1)
        cr.fill()
        # cr.translate(0.5,0.5)

        GateElement.or_gate(cr)

        self.surface.write_to_png(filename + '.png')
        cr.show_page()
        self.surface.finish()

dia = Canvas('myDrawing1',720,720)