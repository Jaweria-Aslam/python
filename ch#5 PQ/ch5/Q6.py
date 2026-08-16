# Function definition
def convert_usd_to_pkr(amount):
    rate = 280
    return amount * rate


# Function call aur returned value ko variable mein save karna
result = convert_usd_to_pkr(50)

# Result display karna
print("Converted Amount:", result)