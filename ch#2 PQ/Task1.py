# User se traffic light ka current color input lena
light = input("Enter traffic light color (Red, Yellow, Green): ")

# Agar light Red ho to vehicle stop karna hai
if light == "Red":
    print("Stop your vehicle")

# Agar light Yellow ho to speed slow karni hai
elif light == "Yellow":
    print("Slow Down")

# Agar light Green ho to vehicle chalana hai
elif light == "Green":
    print("Go")

# Agar user ne koi invalid color enter kiya ho
else:
    print("Invalid traffic light color") 