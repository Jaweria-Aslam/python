# Product class
class Product:
    # Constructor with default attributes
    def __init__(self, name="Unknown Product", price=0):
        self.name = name
        self.price = price

    # Method to print product details
    def display(self):
        print("Product Name:", self.name)
        print("Product Price: Rs.", self.price)


# Creating two objects
laptop = Product("Laptop", 80000)
smartphone = Product("Smartphone", 50000)

# Printing details
print("Laptop Details:")
laptop.display()

print("\nSmartphone Details:")
smartphone.display()