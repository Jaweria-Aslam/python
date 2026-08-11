# User ke text editor operations ki list
actions = ["Type 'Hello'", "Make Bold", "Insert Table"]

# Undo button dabane par last action ko remove karna
removed_action = actions.pop()

# Jo action remove hua hai usay print karna
print("Undo kiya gaya action:", removed_action)

# Updated action list display karna
print("Updated Actions:", actions)