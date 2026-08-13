# Profile class
class Profile:

    # Constructor
    def __init__(self):
        # User status is Active by default
        self.status = "Active"

    # Method to restrict user access
    def restrict_access(self):
        # Change status to Banned
        self.status = "Banned"


# Creating Profile object
user1 = Profile()

# Printing status before restriction
print("Before Restriction:", user1.status)

# Restricting user access
user1.restrict_access()

# Printing status after restriction
print("After Restriction:", user1.status)