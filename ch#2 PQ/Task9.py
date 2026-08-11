# Database queries ki latency milliseconds mein
latencies = [120, 85, 200, 45, 150, 95]

# Sab se fast query ka execution time find karna
fastest = min(latencies)

# Sab se slow query ka execution time find karna
slowest = max(latencies)

# Results print karna
print("Fastest Query Time:", fastest, "ms")
print("Slowest Query Time:", slowest, "ms")