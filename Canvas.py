import cairo
from math import pi, sqrt
import GateElements, Wire

class Canvas(object):

    def __init__(self, filename, width, height):
        self.surface = cairo.SVGSurface(filename + '.svg', width, height)
        cr = self.cr = cairo.Context(self.surface)
        cr.scale(width, height)
        cr.set_line_width(0.1)

        cr.rectangle(0, 0, 1, 1)
        cr.set_source_rgb(1, 1, 1)
        cr.fill()
        # cr.scale(0.124,0.124)
        # cr.translate(0.5,0.5)

        GateElements.buffer_gate_mod(cr, 900, 520, width, height)
        GateElements.buffer_gate_mod(cr, 870, 120, width, height)

        GateElements.and_gate_mod(cr, 400, 120, width, height)

        GateElements.or_gate_mod(cr, 20, 420, width, height)
        Wire.ioWire(cr,420,140,250,80,width, height)

        self.surface.write_to_png(filename + '.png')
        cr.show_page()
        self.surface.finish()

dia = Canvas('myDrawing1',4096,2048)