# Function definition
def apply_discount(bill_amount, discount_percentage):
    discount = bill_amount * discount_percentage / 100
    final_payable = bill_amount - discount
    print("Final Payable:", float(final_payable))


# Function call
apply_discount(5000, 10)