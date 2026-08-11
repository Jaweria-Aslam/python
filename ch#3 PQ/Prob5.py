# Server configuration ki dictionary
config = {
    "host": "localhost",
    "port": 8080
}

# .get() method se port number safely access karna
port = config.get("port")

# Port number print karna
print("Port:", port)

# Aisi key search karna jo dictionary mein mojood nahi
username = config.get("username")

# Missing key ki wajah se program crash nahi hoga
print("Username:", username)