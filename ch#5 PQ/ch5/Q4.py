# Function definition
def calculate_fare(base_fare, distance):
    fare = base_fare + (distance * 20)
    print("Total Fare:", fare)


# Sirf ek argument pass kiya gaya hai
# distance argument missing hai
calculate_fare(150)