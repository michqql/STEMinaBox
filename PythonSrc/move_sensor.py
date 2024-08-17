# Import accelerometer from microbit
from microbit import accelerometer

# Constant which is the number of samples we want to average over.
# Higher values will create a smoother increase/decrease in average
CONST_AVERAGE_SAMPLE_N = 50

# Constant which is the significance threshold of movement
CONST_MOVEMENT_SIGNIFICANCE = 100.0

# Accelerometer average - a rolling average
move_average = 0

def calculateRollingAverage(average, new_sample):
    average -= average / CONST_AVERAGE_SAMPLE_N
    average += new_sample / CONST_AVERAGE_SAMPLE_N

    return average
# end calculateRollingAverage

# Function that should be called by calling application 
# to allow this library to update its sensors
def update():
    # Strengths of movement from the accelerometer
    strength = accelerometer.get_strength()

    # Update the average
    move_average = calculateRollingAverage(move_average, strength)
# end update()

# Returns true if the movement of the microbit is currently significant
# False will indicate that the device is not moving, True indicates movement
def isMoving():
    return move_average >= CONST_MOVEMENT_SIGNIFICANCE
# end isMoving