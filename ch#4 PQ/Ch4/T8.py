# Nodes ko 1 se 5 tak scan karna
for i in range(1, 6):

    # Check karna ke current node maintenance par hai
    if i == 3:

        # Maintenance Node 3 ko skip karna
        print("Skipping Maintenance Node 3")

        # Current iteration ko skip karke next iteration par jana
        continue

    # Baqi nodes ko scan karna
    print(f"Scanning Node: {i}")