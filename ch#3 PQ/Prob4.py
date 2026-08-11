# Employee ki information dictionary mein store karna
employee = {
    "name": "Sarah",
    "role": "Designer",
    "salary": 95000
}

# .pop() method se salary key-value pair remove karna
removed_salary = employee.pop("salary")

# Updated employee dictionary print karna
print("Updated Employee Record:", employee)

# Remove ki gayi salary bhi check karna
print("Removed Salary:", removed_salary)