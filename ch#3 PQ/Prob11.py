# Firewall mein blocked IP addresses ka set
blocked_ips = {"192.168.1.1", "10.0.0.1"}

# Safe declare ki gayi IP ko set se remove karna
blocked_ips.remove("192.168.1.1")

# Updated blocked IPs print karna
print("Updated Blocked IPs:", blocked_ips)