# Server ki temperature readings ki list
temperatures = [40, 60, 92, 70]

# Temperature readings ko one by one check karna
for temperature in temperatures:

    # Check karna ke temperature safe limit se zyada hai
    if temperature > 90:

        # Danger message print karna
        print(f"Danger: {temperature} C detected! Shutting down system.")

        # Loop ko immediately terminate karna
        break

    # Safe temperature ko print karna
    print(f"Current Temperature: {temperature} C")

# Loop ke baad program continue karega
print("System monitoring stopped.")