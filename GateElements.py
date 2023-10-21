import cairo
import math 
from math import pi
import Wire

# !TODO: Should be removed
def buffer_gate(cr):
    cr.set_source_rgb(0, 0, 0)         
    cr.move_to(0,0)
    cr.rel_line_to(1,0.5)
    cr.rel_line_to(-1,0.5)
    cr.close_path()
    cr.set_line_join (cairo.LINE_JOIN_ROUND)
    cr.set_line_width(0.015)             
    cr.stroke()
    cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
    cr.fill()   

def buffer_gate_mod(cr,x, y,width, height, element_size = 1/25):
    cr.set_source_rgb(0, 0, 0)         
    cr.move_to(x/width,y/height)
    cr.rel_line_to(0.5*(element_size),0.5*(element_size))
    cr.rel_line_to(-0.5*(element_size),0.5*(element_size))
    cr.close_path()
    cr.set_line_join (cairo.LINE_JOIN_ROUND)
    cr.set_line_width(0.15*(element_size))             
    cr.stroke()
    cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
    cr.fill()
    # Wire.ioWire(cr,,width, height)
    # Wire.ioWire(cr,420,140,250,80,width, height)

# !TODO: Should be removed
def and_gate(cr):
    cr.set_source_rgb(0, 0, 0)         
    cr.move_to(0,0)
    cr.rel_move_to(0.5,0)
    cr.rel_line_to(-0.5,0)
    cr.rel_line_to(0,1)
    cr.rel_line_to(0.5,0)
    cr.arc(0.5,0.5,0.5 ,(-1*(pi/2)), (pi/2))
    cr.set_line_join (cairo.LINE_JOIN_ROUND)
    cr.set_line_width(0.015)             
    cr.stroke()
    cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
    cr.fill() 

def and_gate_mod(cr,x, y,width, height, element_size = 1/25):
    cr.set_source_rgb(0, 0, 0)         
    cr.move_to(x/width,y/height)
    cr.rel_move_to(0.5*(element_size),0*(element_size))
    cr.rel_line_to(-0.5*(element_size),0*(element_size))
    cr.rel_line_to(0*(element_size),1*(element_size))
    cr.rel_line_to(0.5*(element_size),0*(element_size))
    cr.arc((x/width)+0.5*(element_size),(y/height)+0.5*(element_size),0.5*(element_size) ,(-1*(pi/2)), (pi/2))
    cr.set_line_join (cairo.LINE_JOIN_ROUND)
    cr.set_line_width(0.15*(element_size))             
    cr.stroke()
    cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
    cr.fill() 

# !TODO: Should be removed
# the original method works fine , but it is scalled up a lot
def or_gate(cr):
    cr.set_source_rgb(0, 0, 0)         
    cr.move_to(0,0)
    cr.rel_move_to(0.5,0)
    cr.rel_line_to(-0.5,0)
    cr.rel_line_to(0,1)
    cr.rel_line_to(0.5,0)
    cr.move_to(0.5,0) # IDK why it should be 0.5, 0 instead of 0,0 for now , Cuz I am so exhusted
    cr.curve_to(0.5, 0, 1.6, 0.5, 0.5, 1)
    cr.set_line_join (cairo.LINE_JOIN_ROUND)
    cr.set_line_width(0.015)             
    cr.stroke()
    cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
    cr.fill() 
 
# ! it has wierd behaviors to for its curve
def or_gate_mod(cr,x, y,width, height, element_size = 1/25):
   cr.set_source_rgb(0, 0, 0)         
   cr.move_to(x/width,y/height)
   cr.rel_move_to(0.5*(element_size),0*(element_size))
   cr.rel_line_to(-0.5*(element_size),0*(element_size))
   cr.rel_line_to(0*(element_size),1*(element_size))
   cr.rel_line_to(0.5*(element_size),0*(element_size))
   cr.rel_move_to(0.5*(element_size),0*(element_size)) # IDK why it should be 0.5, 0 instead of 0,0 for now , Cuz I am so exhusted
   cr.curve_to(0.5*(element_size),0*(element_size), (x/width)+1.6*(element_size), (y/height)+0.5*(element_size), (x/width)+0.5*(element_size), (y/height)+1*(element_size))
   cr.set_line_join (cairo.LINE_JOIN_ROUND)
   cr.set_line_width(0.15*(element_size))             
   cr.stroke()
   cr.set_source_rgba(0, 1, 0, 0.60)  #rgba
   cr.fill() 