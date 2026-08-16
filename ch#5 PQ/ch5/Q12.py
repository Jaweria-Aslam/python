# Default parameter ko non-default parameter se pehle rakha gaya hai
def setup(env="Prod", port):
    print("Environment:", env)
    print("Port:", port)


# Function call
setup("Production", 8080)