# Starting batch number
num = 1

# 1 se 50 tak batch numbers check karna
while num <= 50:

    # Check karna ke batch number 2 se completely divisible hai
    if num % 2 == 0:

        # Agar number even hai to usay display karna
        print(f"Even Batch Processed: {num}")

    # Next batch number par move karna
    num += 1