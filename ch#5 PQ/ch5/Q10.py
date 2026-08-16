# Global variable
API_KEY = "GLOBAL_X"


# Function definition
def security_check():
    # Local variable
    API_KEY = "LOCAL_Y"

    # Local variable ko print karega
    print("Inside function:", API_KEY)


# Function call
security_check()

# Global variable ko print karega
print("Outside function:", API_KEY)