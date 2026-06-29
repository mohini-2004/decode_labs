import random
import string

# Get password length from the user
length = int(input("Enter the password length: "))

# Characters to use in the password
characters = string.ascii_letters + string.digits

# Generate the password
password = ""

for i in range(length):
    password += random.choice(characters)

# Display the generated password
print("Generated Password:", password)