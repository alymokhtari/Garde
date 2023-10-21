import cairo
from math import pi, sqrt

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