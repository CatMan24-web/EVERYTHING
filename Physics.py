from vpython import 

# Create the canvas
scene = canvas(height=800, width=400, )

# Create the box
box_object = box(pos=vector(-5, 0, 0), size=vector(1, 1, 1), color=color.red)

# Set the velocity of the box
velocity = vector(0.1, 0, 0)

while :
     
    box_object.pos += velocity  # Move the box

    # Reverse the direction if the box reaches the edges of the canvas
    if box_object.pos.x > 5 or box_object.pos.x < -5:
        velocity.x = -velocity.x
