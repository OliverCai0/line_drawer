from display import *

def draw_line( x0, y0, x1, y1, screen, color ):
    m = (y1 - y0)/(x1 - x0)

    #Octant 1
    if (m < 1) and (m > 0):
        A = y1 - y0
        B = x0 - x1
        d = 2 * A + B
        while x0 <= x1:
            plot(x,y)
            if d >= 0:
                y0 = y1 + 1
                d = d + 2 * B
            x0 = x0 + 1
            d = d + 2 * A

    #Octant 2
    if m > 1:
        


