# User ka current account balance set karna
balance = 15000

# User se withdrawal amount input lena
withdraw_amount = float(input("Enter withdrawal amount (PKR): "))

# Check karna ke withdrawal amount balance ke barabar ya kam hai
if withdraw_amount <= balance:
    # Withdrawal amount ko balance se deduct karna
    balance = balance - withdraw_amount

    # Updated balance display karna
    print("Withdrawal Successful!")
    print("Updated Balance:", balance, "PKR")

else:
    # Agar withdrawal amount balance se zyada ho
    print("Insufficient Funds")