from display import *

def draw_line( x0, y0, x1, y1, screen, color ):


    #Draw from left to right
    if x1 < x0:
        temp = x0
        x0 = x1
        x1 = temp
        temp = y0
        y0 = y1
        y1 = temp

    if y1 == y0:
        while x0 < x1:
            plot(screen, color, int(x0), int(y0))
            x0 = x0 + 1
        return
    
    if x1 == x0:
        while y0 < y1:
            plot(screen, color, int(x0), int(y0))
            y0 = y0 + 1
        return

    m = (y1 - y0)/(x1 - x0)

    #Octant 1 and 5
    if (m <= 1) and (m >= 0):
        #print('Hello')
        A = y1 - y0
        B = x0 - x1
        d = 2 * A + B
        while x0 <= x1:
            #print(x0)
            #print(y0)
            plot(screen, color, int(x0), int(y0))
            if d >= 0:
                #print('No')
                y0 = y0 + 1
                d = d + 2 * B
            x0 = x0 + 1
            d = d + 2 * A

    #Octant 8 and 4
    if (-1 <= m) and (m <= 0):
        A = y1 - y0
        B = x0 - x1
        d = 2 * A - B
        while x0 <= x1:
            plot(screen, color, int(x0), int(y0))
            if d <= 0:
                y0 = y0 - 1
                d = d - 2 * B
            x0 = x0 + 1
            d = d + 2 * A

    #Octant 2 and 6
    if m > 1:
        A = y1 - y0
        B = x0 - x1
        d = 2 * B + A
        while y0 <= y1:
            plot(screen, color, int(x0), int(y0))
            #print(x0)
            if d <= 0:
                x0 = x0 + 1
                d = d + 2 * A
            y0 = y0 + 1
            d = d + 2 * B

    #Octant 2 and 6
    if m < 1:
        A = y1 - y0
        B = x0 - x1
        d = -(2 * B) - A
        while y0 >= y1:
            plot(screen, color, int(x0), int(y0))
            #print(x0)
            if d >= 0:
                x0 = x0 + 1
                d = d + 2 * A
            y0 = y0 - 1
            d = d - 2 * B