import tkinter
from h2geometry import *
from tools import mod2pi

class Canvas:  
    def __init__(self, top):
        self.size_math = 2*1.2
        self.size_px = 0.8*min(top.winfo_screenwidth(), top.winfo_screenheight())
        self.origin_X = self.size_px/2
        self.origin_Y = self.size_px/2
        self.scale = self.size_px/self.size_math
        self.next = "red"
    
        self.cv = tkinter.Canvas(top, width=self.size_px, height=self.size_px, bg="white")
        self.cv.focus_set()
        self.cv.pack()
        self.draw_circle(0, 1, "black")

        N = 5
        angles = [2*k*np.pi/N for k in range(N)]
        self.draw_broken_line([0.5 + 0.3*np.exp(1j*theta) for theta in angles], "green")

    def mouse_click(self, event):
        X, Y = event.x, event.y
        x, y = self.px_to_math(X, Y)
        z = x + y*1j
        if normsq(z)<1:
            self.draw_point(z, color="blue")
        else:
            self.draw_point(z, color="red")
        
    def px_to_math(self, X, Y):
        x = (X - self.origin_X)/self.scale
        y = -(Y - self.origin_Y)/self.scale
        return x, y
        
    def math_to_px(self, x, y):
        X = np.rint(x*self.scale + self.origin_X)
        Y = np.rint(-(y*self.scale) + self.origin_Y)
        return X, Y

    def draw_point(self, z, color="black"):
        ''' Here z is a point in the plane given by a complex coordinate '''
        X, Y = self.math_to_px(z.real, z.imag)
        self.cv.create_oval(X-1, Y-1, X+2, Y+2, fill=color, outline=color, width=3)
        
    def draw_segment(self, z1, z2, color):
        self.draw_broken_line([z1, z2], color)

    def draw_broken_line(self, z, color):
        ''' Here z is a list of points given by their complex coordinates '''
        X, Y = self.math_to_px(np.real(z), np.imag(z))
        points = [[X[i], Y[i]] for i in range(len(X))]
        self.cv.create_line(points, fill=color, width=2)
        
    def draw_circle(self, c, r, color):
        X, Y = self.math_to_px(c.real, c.imag)
        R = np.rint(self.scale*r)
        self.cv.create_oval(X-R, Y-R, X+R+1, Y+R+1, outline=color, width=2)
        
    def draw_circle_arc(self, c, r, z1, z2, color):
        angle1 = mod2pi(np.angle(z1 - c))
        angle2 = mod2pi(np.angle(z2 - c))
        if ((z2-c)*((z1-c).conjugate())).imag < 0:
            angle1, angle2 = angle2, angle1
        X, Y = self.math_to_px(c.real,c.imag)
        R = self.scale*r
        self.cv.create_arc(X-R, Y-R, X+R+1, Y+R+1, start=angle1*180/np.pi, extent=mod2pi(angle2-angle1)*180/np.pi, outline=color, style=tkinter.ARC, width=1)


    def draw_H2_segment(self, z1, z2, color):
        ''' Draws the hyperbolic segment between two points '''
        # to complete


    def draw_H2_triangle(self, z1, z2, z3, color, fill=False):
        ''' Draws a hyperbolic triangle given by its vertices '''
        # to complete

    def draw_H2_polygon(self, z, color, fill=False):
        ''' Draws a hyperbolic triangle given by its list of vertices (z is a list)'''
        # to complete
