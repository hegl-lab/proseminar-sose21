#!/usr/bin/env python
# -*- coding: utf-8 -*-

from schwarztriangle import SchwarzTriangle
from canvas import Canvas
import tkinter
from h2geometry import *

def test_barycenter(window):
    z1  = 0.4 + 0.5j
    z2 = 0.3 + 0.1j
    z3 = -0.2 - 0.7j
    m = 0 + 0 * 1j
    b = get_barycenter(z1, z2, z3)
    window.canvas.draw_point(z1, "blue")
    window.canvas.draw_point(z2, "blue")
    window.canvas.draw_point(z3, "blue")
    window.canvas.draw_point(b, "orange")
    window.canvas.draw_point(m, "red")
    

def check_conditions_and_start(p2,q2,r2,first_window):
    """Checks that the necessary conditions are being met before opening the main window."""
    if not ((float(p2) == 2 and float(q2) == 2) or (float(p2) == 2 and float(r2) == 2) or (float(q2) == 2 and float(r2) == 2)):
            if float(p2) > 1 and float(q2) > 1 and float(r2) > 1:
                if (1/float(p2) + 1/float(q2) + 1/float(r2) < 1):
                    first_window.destroy()
                    run_main_window_tessellation(float(p2), float(q2), float(r2))
                else:
                    label = tkinter.Label(first_window,text= "1/p + 1/q + 1/r = " 
                                                            + str(1/float(p2) + 1/float(q2) + 1/float(r2)) 
                                                            + ", but should be < 1.", fg = "red")
                    label.pack(side="left")  
            else:
                label = tkinter.Label(first_window,text= "All values must be > 1.", fg = "red")
                label.pack(side="left") 
    else:
        label = tkinter.Label(first_window,text= "Only one value can be 2.", fg = "red")
        label.pack(side="left")

def run_tessellation_program():
    """Opens a window where you can write values for p, q and r."""
    first_window = tkinter.Tk()
    first_window.title("Schwarz triangle tessellation")
    
    #Make boxes for writing p, q and r.
    p = enter_pqr(first_window, "p")
    q = enter_pqr(first_window, "q")
    r = enter_pqr(first_window, "r")

    def f():
        p2 = p.get()
        q2 = q.get()
        r2 = r.get()
        check_conditions_and_start(p2,q2,r2,first_window)

    def g(e):
        p2 = p.get()
        q2 = q.get()
        r2 = r.get()
        check_conditions_and_start(p2,q2,r2,first_window)
            
    printButton = tkinter.Button(first_window,text = "Enter", command = f)
    printButton.pack()

    first_window.bind('<Return>', g)

    first_window.mainloop()

def run_main_window_tessellation(p,q,r):
    """Opens a window with a Schwarz triangle tessellation given p,q and r."""
    main_window = Window()
    schwarz = SchwarzTriangle(p,q,r)
    vertices = schwarz.vertices
    z1,z2,z3 = vertices[0],vertices[1],vertices[2]
    s12 = H2_segment(z1, z2)
    s13 = H2_segment(z1, z3)
    s23 = H2_segment(z2, z3)
    main_window.canvas.initiate_sides(s12, s23, s13)
    startTriangle = [H2_reflection(s12), H2_reflection(s13), H2_reflection(s23)]
    main_window.canvas.make_tessellation(z1, z2, z3, startTriangle)
    main_window.run()

def enter_pqr(window, name):
    frame = tkinter.Frame(window)
    frame.pack()
    label = tkinter.Label(frame, text="Please write " + name + ": ")
    label.pack(side="left")
    var = tkinter.StringVar()
    pqr = tkinter.Entry(frame, textvariable=var, exportselection=0)
    pqr.pack(side="left")
    return pqr

class Window:
    def __init__(self):
        self.top = tkinter.Tk()
        self.top.title("Hyperbolic tilings")
        self.canvas = Canvas(self.top)
        self.top.bind("<Button-1>", self.mouse_click)
    
    def mouse_click(self, event):
        self.canvas.mouse_click(event)
        
    def run(self):
        self.top.mainloop()

if __name__ == "__main__":
    #run_tessellation_program()
    #----------uncomment the following lines to test the barycenter function
    #window = Window()
    ##test_barycenter(window)
    #window.run()



