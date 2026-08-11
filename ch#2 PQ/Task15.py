# Server security log mein stored User IDs
access_logs = (101, 105, 101, 102, 101, 108, 105)

# User ID 101 ne kitni dafa database access kiya
count_101 = access_logs.count(101)

# User ID 102 pehli dafa kis index position par logged hai
index_102 = access_logs.index(102)

# Results display karna
print("User ID 101 ne database ko", count_101, "daafa access kiya.")
print("User ID 102 pehli dafa index position", index_102, "par logged hai.")