# Countdown ki starting value
count = 5

# Negative step (-1) ke saath countdown loop
# range(count, 0, -1) values ko 5 se 1 tak decrease karega
for i in range(count, 0, -1):

    # Current countdown value print karna
    print(f"T-minus {i}")

# Countdown complete hone ke baad final message
print("Blast Off!")