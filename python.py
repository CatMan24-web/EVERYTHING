from vpython import *

# Create the scene
scene = canvas(title="Moving Box", width=800, height=600, center=vector(0, 0, 0), background=color.white)

# Create the floor and the box
floor = box(pos=vector(0, -0.5, 0), size=vector(10, 0.1, 10), color=color.gray(0.5))
moving_box = box(pos=vector(-4.5, 0, 0), size=vector(1, 1, 1), color=color.blue)

# Set the initial velocity and direction
velocity = vector(2, 0, 0)
direction = 1

# Run the simulation
while True:
    rate(60)
    # Update the position of the box
    moving_box.pos += velocity * direction * 0.1
    # Check for collisions with the edges of the floor
    if moving_box.pos.x >= 4.5 or moving_box.pos.x <= -4.5:
        direction *= -1
    # Stop the box when it returns to the left edge
    if moving_box.pos.x <= -4.5 and direction == -1:
        break
