# Function to check if two numbers are not equal
def check_not_equal(num1, num2):
    if num1 != num2:
        return f"{num1} is not equal to {num2}"
    else:
        return f"{num1} is equal to {num2}"

# Input two numbers from the user
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Check if the numbers are not equal
result = check_not_equal(num1, num2)
print(result)
