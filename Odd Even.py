# Function to check if a number is odd or even
def check_odd_even(number):
    if number % 2 == 0:
        return f"{number} is Even"
    else:
        return f"{number} is Odd"

# Input from the user
num = int(input("Enter a number: "))

# Check if the number is odd or even
result = check_odd_even(num)
print(result)
