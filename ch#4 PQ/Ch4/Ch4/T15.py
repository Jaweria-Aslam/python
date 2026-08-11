# Python ka standard time module import karna
import time

# Loop ko 5 sensor nodes ke liye run karna
for node in range(1, 6):

    # Current sensor node ka tracker value print karna
    print("Checking Sensor Node:", node)

    # Har sensor check ke baad 1 second ka delay
    time.sleep(1)

# Monitoring complete hone ka message
print("All sensor nodes checked successfully.")