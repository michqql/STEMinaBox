# Import microbit
from microbit import *
import move_sensor

def moveForward(distance = 1):
    # TODO: Implement
    return 0

def moveBackwards(distance = 1):
    # TODO: Implement
    return 0

def chooseRandomDirection():
    # TODO: Implement
    return 0

# Main loop
while True:
    # Update the sensor
    move_sensor.update()

    # If moving, carry on!
    if move_sensor.isMoving():
        # Continue moving forward
        moveForward()
    else:
        # No longer able to move in this direction
        # Back up and choose new direction
        moveBackwards(10)
        chooseRandomDirection()
        # Wait before moving forward again, to wait for the move sensor to 
        # no longer detect the movement of going backwards and changing direction
        # TODO: Implement sleep

        moveForward(10) # start moving forward to satisfy moving_sensor.isMoving
        

# end mainloop