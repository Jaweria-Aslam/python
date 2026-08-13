# DatabaseConfig class
class DatabaseConfig:

    # Constructor
    def __init__(self):
        # Tuple is used because it is immutable
        self.credentials = ("localhost", 3306)


# Creating DatabaseConfig object
db = DatabaseConfig()

# Printing database credentials
print("Host:", db.credentials[0])
print("Port:", db.credentials[1])