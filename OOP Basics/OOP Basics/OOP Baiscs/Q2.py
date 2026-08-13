# SmartBulb class
class SmartBulb:

    # Constructor with default state
    def __init__(self):
        self.state = "OFF"

    # Method to turn the bulb ON
    def turn_on(self):
        self.state = "ON"


# Creating SmartBulb object
bulb = SmartBulb()

# Printing initial state
print("Initial State:", bulb.state)

# Turning the bulb ON
bulb.turn_on()

# Printing new state
print("After turn_on():", bulb.state)