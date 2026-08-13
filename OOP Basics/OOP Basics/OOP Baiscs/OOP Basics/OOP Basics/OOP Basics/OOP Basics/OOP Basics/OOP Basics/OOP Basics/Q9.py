# HotelRoom class
class HotelRoom:

    # Constructor
    def __init__(self):
        # Room is initially occupied
        self.is_occupied = True

    # Method to checkout
    def checkout(self):
        # Change room status to False
        self.is_occupied = False


# Creating HotelRoom object
room1 = HotelRoom()

# Printing initial status
print("Before Checkout:", room1.is_occupied)

# Calling checkout method
room1.checkout()

# Printing updated status
print("After Checkout:", room1.is_occupied)