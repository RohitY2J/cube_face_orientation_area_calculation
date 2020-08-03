import numpy as np
from b_cube_diagram import plot_cube
from c_3d_transformation import rotate_matrix
from d_flags import get_flags
from math import *
from e_cal_area_parallelogram import calculate_area

#define the coordinates of cube
vertices = np.array([
[1, 1, -1],  #v1 - top front right
[1, -1, -1], #v2 - bottom front right
[-1, -1, -1],#v3 - bottom front left
[-1, 1, -1], #v4 - top front left

[1, 1, 1],  #v5 - top back right
[1, -1, 1], #v6 - bottom back right
[-1, -1, 1],#v7 - bottom back left
[-1, 1, 1]  #v8 - top back left
])

#plotting the cube
plot_cube(vertices)

#define roll pitch yaw
roll, pitch, yaw = pi/2, 0, 0

#get the rotated matrix
new_vertices = rotate_matrix(vertices, roll, pitch, yaw)

#plotting the new cube
plot_cube(new_vertices)

#get flags for new matrices
visible_flags = get_flags(new_vertices)

#calculate area
area = calculate_area(new_vertices, visible_flags)

print(area)



