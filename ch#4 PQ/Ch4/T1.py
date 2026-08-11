# Song ka naam define karna
song_name = "Soul Light"

# Song ko kitni dafa repeat karna hai
N = 3

# Repeat counter ko 1 se start karna
count = 1

# Jab tak count N se chhota ya barabar hai, loop chalega
while count <= N:

    # Song name aur current repeat count print karna
    print(f"Playing: {song_name} (Repeat Count: {count})")

    # Counter ko 1 se increase karna
    # Is se infinite loop prevent hota hai
    count += 1