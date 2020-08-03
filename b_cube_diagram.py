from mpl_toolkits.mplot3d import axes3d
import matplotlib.pyplot as plt
import numpy as np

def plot_cube(vertices):
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')

    ax.scatter([0],[0],[5])
    #top front face
    for i in range(4):
        if i != 3:
            #get the x and y values of consecutive two vertices as list
            X, Y = [vertices[i][0], vertices[i+1][0]], [vertices[i][1], vertices[i+1][1]] 
            #get the z coordinate
            Z = np.array([[vertices[i][2],vertices[i+1][2]],[vertices[i][2],vertices[i+1][2]]])
            #plot the particular length
            ax.plot_wireframe(X, Y, Z)
            X, Y = [vertices[i+4][0], vertices[i+5][0]], [vertices[i+4][1], vertices[i+5][1]] 
            Z = np.array([[vertices[i+4][2],vertices[i+5][2]],[vertices[i+4][2],vertices[i+5][2]]])
            ax.plot_wireframe(X, Y, Z)
            X, Y = [vertices[i][0], vertices[i+4][0]], [vertices[i][1], vertices[i+4][1]] 
            Z = np.array([[vertices[i][2],vertices[i+4][2]],[vertices[i][2],vertices[i+3][2]]])
            ax.plot_wireframe(X, Y, Z)
        else:
            X, Y = [vertices[i][0], vertices[0][0]], [vertices[i][1], vertices[0][1]] 
            Z = np.array([[vertices[i][2],vertices[0][2]],[vertices[i][2],vertices[0][2]]])
            ax.plot_wireframe(X, Y, Z)
            X, Y = [vertices[i+4][0], vertices[i+1][0]], [vertices[i+4][1], vertices[i+1][1]] 
            Z = np.array([[vertices[i+4][2],vertices[i+1][2]],[vertices[i+4][2],vertices[i+1][2]]])
            ax.plot_wireframe(X, Y, Z)
            X, Y = [vertices[i][0], vertices[i+4][0]], [vertices[i][1], vertices[i+4][1]] 
            Z = np.array([[vertices[i][2],vertices[i+4][2]],[vertices[i][2],vertices[i+4][2]]])
            ax.plot_wireframe(X, Y, Z)

    plt.show() 
