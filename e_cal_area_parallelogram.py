import numpy as np
import math
#defining a cube for sample
k = np.array([[-0.5, 1.5, -0.70710678],
              [-0.20710678, -0.20710678, -1.70710678],
              [-1.20710678, -1.20710678, -0.29289322],
              [-1.5,         0.5,         0.70710678],
              [ 1.20710678,  1.20710678,  0.29289322],
              [ 1.5,        -0.5,        -0.70710678],
              [ 0.5,        -1.5,         0.70710678],
              [ 0.20710678,  0.20710678,  1.70710678]])

#flags for visibility and invisibility
flags = np.array([1, 0, 1, 1, 1, 1, 1, 1])

#function for calculating the area of parallelogram
def parm_area(f_ver, s_ver, t_ver, fo_ver):
    #getting the coefficient in the equations as Ax+By+C = 0
    A = fo_ver[1] - t_ver[1]
    B = t_ver[0] - fo_ver[0]
    C = t_ver[1]*fo_ver[0] - t_ver[0]*fo_ver[1]
    #getting the perpendicular distance/length of parallelogram
    per_dist = abs(A*f_ver[0]+B*f_ver[0]+C)/math.sqrt(A**2+B**2)
    #getting the base length of parallelogram
    base = math.sqrt((fo_ver[0]-t_ver[0])**2+(fo_ver[1]-t_ver[1])**2)
    #returning the area of parm using b*h
    return per_dist*base

#calculating the curved surface area of cube using each face
def calculate_area(vertices, flags):
    area = 0
    #for the front face if visible
    first_f = vertices[0]
    second_f = vertices[1]
    third_f = vertices[2]
    fourth_f = vertices[3]
    if flags[0]!=0 and flags[1]!=0 and flags[2]!=0 and flags[3]!=0:
        area += parm_area(first_f, second_f, third_f, fourth_f)

    #for the back face if visible
    first_b = vertices[4]
    second_b = vertices[5]
    third_b = vertices[6]
    fourth_b = vertices[7]

    if flags[4]!=0 and flags[5]!=0 and flags[6]!=0 and flags[7]!=0:
        area += parm_area(first_b, second_b, third_b, fourth_b)

    #for the top face if visible
    first_t = vertices[0]
    second_t = vertices[3]
    third_t = vertices[4]
    fourth_t = vertices[7]

    if flags[0]!=0 and flags[3]!=0 and flags[4]!=0 and flags[7]!=0:
        area += parm_area(first_t, second_t, third_t, fourth_t)

    #for the bottom face if visible 
    first_bo = vertices[1]
    second_bo = vertices[2]
    third_bo = vertices[5]
    fourth_bo = vertices[6]

    if flags[1]!=0 and flags[2]!=0 and flags[5]!=0 and flags[6]!=0:
        area += parm_area(first_bo, second_bo, third_bo, fourth_bo)

    #for the left face if visible
    first_l = vertices[2]
    second_l = vertices[3]
    third_l = vertices[6]
    fourth_l = vertices[7]

    if flags[2]!=0 and flags[3]!=0 and flags[6]!=0 and flags[7]!=0:
        area += parm_area(first_l, second_l, third_l, fourth_l)

    #for the right face if visible
    first_r = vertices[0]
    second_r = vertices[1]
    third_r = vertices[4]
    fourth_r = vertices[5]

    if flags[1]!=0 and flags[0]!=0 and flags[5]!=0 and flags[4]!=0:
        area += parm_area(first_r, second_r, third_r, fourth_r)

    #return the area
    return area

#area = calculate_area(k, flags)
#print(area)
        
    
    
