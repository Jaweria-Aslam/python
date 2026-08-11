# Basic customer information
basic_info = {
    "name": "Hamza"
}

# Professional customer information
professional_info = {
    "role": "AI Specialist"
}

# Professional information ko basic information mein merge karna
basic_info.update(professional_info)

# Merged dictionary print karna
print("Merged Customer Profile:", basic_info)