import cairo
from math import pi, sqrt

def ioWire(cr,xZero,yZero,xOne,yOne,width, height, element_size = 1/25):         
    cr.set_source_rgba(0, 0, 0, 0.90)  #rgba
    cr.move_to(xZero/width,yZero/height)
    cr.line_to(xOne/width,yOne/height)
    cr.set_line_width(0.15*(element_size))             
    cr.stroke()
    cr.fill() 