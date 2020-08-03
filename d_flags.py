from math import *
import numpy as np
'''
vertices = np.array([
[1, 1, -1],  #v1 - top front right
[1, -1, -1], #v2 - bottom front right
[-1, -1, -1],#v3 - bottom front left
[-1, 1, -1], #v4 - top front left

[1, 1, 1],  #v5 - top back right
[1, -1, 1], #v6 - bottom back right
[-1, -1, 1],#v7 - bottom back left
[-1, 1, 1]  #v8 - top back left
])'''

#function for getting the flags to define the visibility of the surface
def get_flags(vertices):
    #defining the flags
    flags = np.zeros(8)

    #performing the transpose to get the x, y and z coordinates separately
    transpose_mat = vertices.T
    x_max = max(transpose_mat[0])
    x_min = min(transpose_mat[0])
    y_max = max(transpose_mat[1])
    y_min = min(transpose_mat[1])
    z_max = max(transpose_mat[2])
    z_min = min(transpose_mat[2])

    #print(x_max, y_max, z_max)
    #print(x_min, y_min, z_min)

    for i in range(8):
        #get the coordinate to be tested
        coor = vertices[i]
        #if the x or y or z part is max or min then it is visible except for z min
        if coor[0] == x_min or coor[0] == x_max:
            flags[i] = 1
        elif coor[1] == y_max or coor[1] == y_min:
            flags[i] = 1
        elif coor[2] == z_max:
            flags[i] = 1
        else:
            #if the coordinate if visible but its x y z are not max or min
            vertice_op = np.array([])
            for j in range(8):
                #get the matrix without the coor row
                if ~(vertices[j]==coor).all():
                    vertice_op = np.append(vertice_op, vertices[j], axis = 0)
            #reshape the result into row and column as before
            vertice_op = np.reshape(vertice_op, (7,3))
            print("The vertice_op is : " , vertice_op)
            #perform max and min for tested coordinate and other four coordinate representing the surface
            #if coordinate lies within the surface then it doesn't have max x and y and min x and y
            #among the given five coordinate
            #create list for the x part of the five coordinates
            lst_x = np.array(coor[0])
            lst_y = np.array(coor[1])
            for j in range(4):
                for k in range(j+1,4):
                    #add the first coordinate of the surface
                    lst_x = np.append(lst_x,vertice_op[j][0])
                    #add the remaining three coordinate of the surface
                    lst_x = np.append(lst_x,vertice_op[k:k+3, 0])
                    lst_y = np.append(lst_y,vertice_op[j][1])
                    lst_y = np.append(lst_y,vertice_op[k:k+3, 1])
                    #print(lst_x, lst_y)
                    if (max(lst_x)==coor[0] or min(lst_x)==coor[0]) and flags[i]!=1:
                        flags[i] = 1
                    elif (max(lst_y)==coor[1] or min(lst_y)==coor[1]) and flags[i]!=1:
                        flags[i] = 1
                    else:
                        break
    print(flags)
    return flags


