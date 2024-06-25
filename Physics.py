from vpython import *

# Create the scene
scene = canvas(title="Box_Of_Physics", width=800, height=600, background=color.black)

# Create the floor and the box
floor = box(size=vector(10, 0.1, 10), color=color.white)
moving_box = box(size=vector(1, 1, 1), color=color.white)


x = -4.5
velocity = 0.1
direction = 1

# Update the x position of the box
 x += velocity * direction
    
# Update the box position
 moving_box.size = vector(1, 1, 1)  # We need to keep setting size, as per requirement of not using pos or vec
 moving_box.axis = vector(x, 0, 0)  # Using axis instead to set position
    
 # Check for collisions with the edges of the floor
if x >= 4.5 or x <= -4.5:
    direction *= -1
    