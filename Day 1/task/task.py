# Create a greeting for your program with ASCII art.
print("=" * 50)
print("     Welcome to the Band Name Generator")
print("=" * 50)

# Ask the user for the city that they grew up in and store it in a variable.
print("\nLet's get started!")
CityName = input("1. What's the name of the city you grew up in?\n> ")

# Draw a line separator for better readability.
print("-" * 50)

# Ask the user for the name of a pet and store it in a variable.
PetName = input("2. What is the name of your pet?\n> ")

# Draw another line separator for better readability.
print("-" * 50)

# Combine the name of their city and pet and show them their band name.
print(f"\nYour band name could be: *** {CityName} {PetName} ***")
print("=" * 50)
