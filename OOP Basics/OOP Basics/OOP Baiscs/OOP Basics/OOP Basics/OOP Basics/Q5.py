# Server class
class Server:

    # Class attribute
    provider_name = "AWS"

    # Constructor
    def __init__(self, ip_address):
        # Instance attribute
        self.ip_address = ip_address


# Creating a Server object
server1 = Server("192.168.1.10")

# Printing details
print("Cloud Provider:", server1.provider_name)
print("IP Address:", server1.ip_address)