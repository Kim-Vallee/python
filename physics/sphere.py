from visual import *
from numpy import *
# L = 1
# R = 0.3
# for i in range(-L,L+1):
#     if i % 2 == 0:
#         for j in range(-L,L+1):
#             if j % 2 == 0:
#                 for k in range(-L,L+1):
#                     if k % 2 == 0:
#                         sphere(pos=[i,j,k],radius=R,color=color.red)
#                     else:
#                         sphere(pos=[i,j,k],radius=R,color=color.blue)
#             else:
#                 for k in range(-L,L+1):
#                     if k % 2 == 0:
#                         sphere(pos=[i,j,k],radius=R,color=color.blue)
#                     else:
#                         sphere(pos=[i,j,k],radius=R,color=color.red)
#     else:
#         for j in range(-L,L+1):
#             if j % 2 == 0:
#                 for k in range(-L,L+1):
#                     if k % 2 == 0:
#                         sphere(pos=[i,j,k],radius=R,color=color.blue)
#                     else:
#                         sphere(pos=[i,j,k],radius=R,color=color.red)
#             else:
#                 for k in range(-L,L+1):
#                     if k % 2 == 0:
#                         sphere(pos=[i,j,k],radius=R,color=color.red)
#                     else:
#                         sphere(pos=[i,j,k],radius=R,color=color.blue)
# ----------------------------------------------
# s = sphere()
# s.radius = 0.5
# s.color = color.blue
# ----------------------------------------------
# s = empty(10,sphere)
# for n in range(10):
#     s[n] = sphere()
# ----------------------------------------------
# box(pos=[x,y,z], axis=[a,b,c], \
# length=L, height=H, width=W, up=[q,r,s]) # Creates a cube
#
# cone(pos=[x,y,z], axis=[a,b,c], radius=R)
#
# cylinder(pos=[x,y,z], axis=[a,b,c], radius=R)
#
# pyramid(pos=[x,y,z], size=[z,b,c])
#
# arrow(pos=[x,y,z], axis=[a,b,c], \
# headwidth=H, headlength=L, shaftwidth=W)

display(x=100,y=100,width=600,height=600, \
center=[5,0,0],forward=[0,0,-1], \
background=color.blue,foreground=color.yellow)
