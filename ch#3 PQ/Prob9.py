# Website par aane wali IP requests ki list
traffic = ["IP-1", "IP-2", "IP-1", "IP-3", "IP-2"]

# List ko set mein convert karna
# Set automatically duplicate IP addresses remove kar deta hai
unique_ips = set(traffic)

# Unique IPs print karna
print("Unique IPs:", unique_ips)