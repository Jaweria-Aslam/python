# Starting value set karna
counter = 1

# Infinite loop ka example
while counter <= 5:

    # Current value display karna
    print("Checkpoint - Counter:", counter)

    # BUG:
    # Yahan counter ko increase nahi kiya gaya,
    # isliye counter hamesha 1 rahega
    # aur condition counter <= 5 hamesha True rahegi.

    # counter += 1  # Ye line missing hai