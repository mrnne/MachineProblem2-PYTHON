# MACHINE PROBLEM 2 
# Python Program for solving the center, radius and vector DEF from 3 input points (x,y)
# Center-radius form/ General form (x-h)^2 + (y-k)^2 = r^2
# x^2 + y^2 + Dx + Ey + F= 0

# import numpy and math
import numpy as np
import math

# Obtaining 3 input points (x,y)
def circle2d(x1,y1,x2,y2,x3,y3):

    # Creating an array with columns of x^2  + y^2, x1, y1, 1 
    M= np.array([[(x1**2  + y1**2), x1, y1, 1], [(x2**2  + y2**2), x2, y2, 1], [(x3**2  + y3**2), x3, y3, 1]])

    # M1 is a minor of M without column 1
    M1= M[:,[1,2,3]]
    # M12 is a minor of M without column 2
    M12= M[:,[0,2,3]]
    # M13 is a minor of M without column 3
    M13= M[:,[0,1,3]]

    # Obtaining the center (x value) 
    x= round((np.linalg.det(M12) / np.linalg.det(M1) )*(1/2))

    # Obtaining the center (x value) 
    y= round((np.linalg.det(M13) / np.linalg.det(M1) )*(-1/2))

    # We will be using the 1st Point (x1,y1) to substitute

    # Radius is from  r^2= (x-h)^2 + (y-k)^2 
    r= round(math.sqrt(((x1-x)**2) + ((y1-y)**2)),5)
   
    # Constant F is derived from x^2 + y^2 + Dx + Ey + F= 0
    F = ( - x1**2  - y1**2 - (2 * -x  *x1) - (2 * -y *y1))

    # Combining the constants into a horizontal vector
    DEF= [2*(-x), 2*(-y), F];

    # Displaying the Center (x,y)
    print('Center: (',x,', ',y,')')

    # Displaying the Radius (r)
    print('Radius: ',r)

    # Displaying the Vector (DEF)
    print('vector[D,E,F]: ', DEF)