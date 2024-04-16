# Num 5 Dictionary
# Dictionary containing usernames as keys and passwords as values
user_credentials = {
    "user1": "password1",
    "user2": "password2",
    "user3": "password3",
    "user4": "password4",
    "user5": "password5",
    "user6": "password6",
    "user7": "password7",
    "user8": "password8",
    "user9": "password9",
    "user10": "password10"
}

def login():
    while True:  # Loop until the correct username and password are entered
        username = input("Enter your username: ")
        password = input("Enter your password: ")

        # Check if username exists in the dictionary
        if username in user_credentials:
            # Check if the entered password matches the password associated with the username
            if user_credentials[username] == password:
                print("Login successful! Welcome, {}.".format(username))
                break  # Exit the loop after successful login
            else:
                print("Invalid password. Please try again.")
        else:
            print("User '{}' not found. You are not a valid user of the system.".format(username))

# Call the login function to start the authentication process
login()
