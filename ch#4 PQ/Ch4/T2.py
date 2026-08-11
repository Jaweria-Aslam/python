# Maximum allowed login attempts
max_attempts = 3

# Attempt counter ko 1 se start karna
attempts = 1

# Wrong login attempts ko simulate karna
while attempts <= max_attempts:

    # Wrong login attempt ki warning display karna
    print(f"Login Attempt {attempts} failed.")

    # Attempt counter ko 1 se increase karna
    # Is se infinite loop prevent hota hai
    attempts += 1

# Maximum attempts complete hone ke baad system lock karna
print("System locked.")