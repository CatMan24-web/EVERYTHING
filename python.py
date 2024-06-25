from vpython import *

# Create the scene
scene = canvas(title="Box_Of_Physics", width=800, height=600, background=color.black)

# Create the floor and the box
floor = box(size=vector(10, 0.1, 10), color=color.white)
moving_box = box(size=vector(1, 1, 1), color=color.white)


x = -4.5
velocity = 0.1
direction = 1



    # Stop the box when it returns to the left edge
if x <= -4.5 and direction == -1:
    return True
        
