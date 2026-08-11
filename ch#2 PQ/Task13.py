# Server connectivity details ko tuple mein store karna
server_config = ("192.168.1.1", 8080)

try:
    # Port number (index 1) ko update karne ki koshish
    server_config[1] = 9090

except TypeError as e:
    # Tuple ko modify nahi kiya ja sakta, is liye TypeError handle hoga
    print("TypeError:", e)
    print("Security Check: Server configuration edit nahi ho sakti.")

# Original configuration check karna
print("Original Server Configuration:", server_config)