# Natural numbers ki limit define karna
N = 5

# Total balance ko 0 se initialize karna
total = 0

# Counter ko 1 se start karna
i = 1

# Jab tak counter N se chhota ya barabar hai, loop chalega
while i <= N:

    # Current number ko total balance mein add karna
    total = total + i

    # Counter ko next number par le jana
    i += 1

# Final invoice balance print karna
print("Total Invoice Balance:", total)