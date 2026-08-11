# User se total cart value lena
cart_value = float(input("Enter total cart value (PKR): "))

# Check karna ke cart value 5000 PKR se zyada hai ya nahi
if cart_value > 5000:
    # 10% discount calculate karna
    discount = cart_value * 0.10

    # Discount minus karke final bill calculate karna
    discounted_total = cart_value - discount

    # Discounted total print karna
    print("Discounted Total:", discounted_total, "PKR")

else:
    # Agar cart value 5000 ya us se kam ho
    print("No discount applicable")