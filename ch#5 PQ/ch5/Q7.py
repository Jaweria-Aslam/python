# Function definition
def book_flight(origin, destination, passenger_class):
    print(f"Booking Flight from {origin} to {destination} in {passenger_class} class.")


# Keyword arguments
# Order change kiya gaya hai, lekin names explicitly diye gaye hain
book_flight(
    destination="London",
    passenger_class="Business",
    origin="Karachi"
)