# Function definition
def analyze_text(user_input):
    vowels = "aeiouAEIOU"
    vowel_count = 0
    consonant_count = 0

    # String ke har character ko check karna
    for char in user_input:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    # Multiple values return karna
    return vowel_count, consonant_count


# Tuple unpacking
v_cnt, c_cnt = analyze_text("Saumya")

# Results display karna
print("Vowels =", v_cnt)
print("Consonants =", c_cnt)