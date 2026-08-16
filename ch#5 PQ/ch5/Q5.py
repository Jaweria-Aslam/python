# Function with default parameter
def set_ac_temp(temp=24):
    print("AC set to", temp)


# Scenario 1: Without custom argument
# Default value 24 use hogi
set_ac_temp()

# Scenario 2: With custom argument
# 18 default value 24 ko override karega
set_ac_temp(18)