from vpython import *

# Create a box
box_object = box(pos=vector(0, 0, 0), size=vector(1, 1, 1), color=color.red)

# Set up the scene
scene = canvas()

# Display the box
scene.append_to_caption('\nA red box has been created at the origin with size 1x1x1\n')
