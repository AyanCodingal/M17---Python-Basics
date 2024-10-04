# Function to display a congratulations message
def congratulations_message(name, achievement):
    print(f"Congratulations, {name}!")
    print(f"You have achieved {achievement}!")
    print("Wishing you more success and happiness in the future!")

# Input from the user
name = input("Enter the person's name: ")
achievement = input("Enter the achievement: ")

# Show the congratulations message
congratulations_message(name, achievement)
