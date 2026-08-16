# Global variable
API_KEY = "GLOBAL_X"

# Function
def security_check():
    # Local variable
    API_KEY = "LOCAL_Y"

    print("Inside function:", API_KEY)


# Function call
security_check()

# Global variable print
print("Outside function:", API_KEY)