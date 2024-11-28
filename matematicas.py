import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

vertices = np.array([
    [0,0,0],
    [1,0,0],
    [0,1,0],
    [0,0,1]
])

faces= [
    [vertices[0], vertices[1],vertices[2]],
    [vertices[0], vertices[1],vertices[3]],
    [vertices[0], vertices[2],vertices[3]],
    [vertices[1], vertices[2],vertices[3]]
]

fig = plt.figure(figsize=(8,6))
ax = fig.add_subplot(111, projection = "3d")

poly3d = [[list(face) for face in faces]]
ax.add_collection3d(Poly3DCollection(faces, facecolors='cyan', edgecolor='black',alpha=0.5))

ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')
ax.set_zlabel('Z-axis')
ax.set_xlim(0,1)
ax.set_ylim(0,1)
ax.set_zlim(0,1)
ax.view_init(30,30)

plt.title("solido delimitado porx+y+z=1 y los platos coordenados")
plt.show()