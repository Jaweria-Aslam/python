# 15 is an integer, while "Active connections: " is a string.
# Python cannot directly join a string and an integer using +.
# So, we convert 15 into a string using str().

connections = 15

print("Active connections: " + str(connections))