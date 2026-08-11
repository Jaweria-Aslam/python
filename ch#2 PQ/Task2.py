# Student ke exam marks input lena
marks = int(input("Enter your exam marks (0-100): "))

# Agar marks 90 ya us se zyada hon to Grade A
if marks >= 90:
    print("Grade A")

# Agar marks 80 se 89 ke darmiyan hon to Grade B
elif marks >= 80:
    print("Grade B")

# Baqi tamam marks ke liye Grade C
else:
    print("Grade C")