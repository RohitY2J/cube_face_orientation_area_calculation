from math import *
import numpy as np

def rotate_matrix(vertices, roll, pitch, yaw):
    #defining the matrix for performing rotation
    rotation_matrix = np.array([[cos(yaw)*cos(pitch), cos(yaw)*sin(pitch)*sin(roll)-sin(yaw)*cos(roll), cos(yaw)*sin(pitch)*cos(roll)+sin(yaw)*sin(roll)],
                               [sin(yaw)*cos(pitch), sin(yaw)*sin(pitch)*sin(roll)+cos(yaw)*cos(roll), sin(yaw)*sin(pitch)*cos(roll)-cos(yaw)*sin(roll)],
                               [-sin(pitch), cos(pitch)*sin(roll), cos(pitch)*cos(roll)]])

    result = []
    print("Here the rotation matrix is : \n",rotation_matrix)
    #performing the matrix multiplication for each row in the matrix
    for i in range(8):
        result.append(list(np.matmul(rotation_matrix,vertices[i])))

    #convert the result back to array
    ans = np.array(result)
    print("The matrix after rotation is : \n", ans)
    return ans
