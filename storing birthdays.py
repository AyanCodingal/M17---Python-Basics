# Function to display all stored birthdays
def display_birthdays(birthday_dict):
    for name, birthday in birthday_dict.items():
        print(f"{name}'s birthday is on {birthday}")

# Main Program
birthdays = {}

# Collecting birthdays of 5 friends
for i in range(5):
    name = input(f"Enter the name of friend {i+1}: ")
    birthday = input(f"Enter {name}'s birthday (dd/mm/yyyy): ")
    birthdays[name] = birthday

# Display the stored birthdays
print("\nStored Birthdays:")
display_birthdays(birthdays)
