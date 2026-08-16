# Tax calculation function
def calc_tax(bill):
    tax_rate = 10
    tax = bill * tax_rate / 100
    return bill + tax


# Checkout processing function
def process_checkout(bill):
    # calc_tax() ka returned result receive karna
    total = calc_tax(bill)

    print("Final Checkout Total:", total)


# Function call
process_checkout(1000)