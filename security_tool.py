#Logan Ward | ID: B01886641
#Task 1: Security Tool

#authenticate user funciton
def user_authentication(correct_username, correct_password):
    Failed_attempts = 0
    
    while Failed_attempts < 3:
        username = input("Please enter your username: ")
        password = input("Please enter your password: ")
        
        if username == correct_username and password == correct_password:
            print("Login successful! Welcome, " + username + ".")
            return True
        else:
            Failed_attempts += 1
            print(f"Incorrect username or password. You have {3 - Failed_attempts} attempts left.")

    print("Login failed. Maximum attempts reached, the account is now frozen for 24 hours.")
    return False

    #display the menu options to the user
def display_menu():
    print("\n----- Security Program Menu -----")
    print("1. Security Event Counter")
    print("2. Brute Force Attack Simulation")
    print("3. Exit")
    return input("Please select an option (1-3): ")



#ask the user for a password 10 times and count the number of correct and incorrect attempts
def security_event_counter(event_counter_password):
    correct_count = 0
    incorrect_count = 0
    
    for i in range(1,11):
        password = input(f"Attempt {i}: Please enter the password: ")
        if password == event_counter_password:
            correct_count += 1
        else:
            incorrect_count += 1

    Incorrect_percentage = (incorrect_count / 10) * 100
    
    print(f"\nTotal correct attempts: {correct_count}")
    print(f"Total incorrect attempts: {incorrect_count}")
    print(f"Percentage of incorrect attempts: {Incorrect_percentage}%")
    
    if Incorrect_percentage > 50:
        print("Warning: More than 50 percent of the attempts were incorrect.")
        

        #Simulate a brute force attack
def brute_force_attack_simulation(bruteforce_password, bruteforce_max_attempts):
    current_attempts = 0
    guess = ""
    
    #if the user guesses the password correctly, display a success message and the number of attempts taken. If the user fails to guess the password within the maximum attempts, display a failure message.
    while guess != bruteforce_password and current_attempts < bruteforce_max_attempts:
        guess = input("Please enter your guess for the password: ")
        current_attempts += 1
        
        if guess != bruteforce_password:
            print(f"Password entered incorrectly. Attempt {current_attempts} of {bruteforce_max_attempts}")
        
    if guess == bruteforce_password:
        print(f"Password found after {current_attempts} attempts!")
    else:
        print("Password not found. Maximum attempts reached. Brute force attack simulation failed.")
            


def main() -> None:
    
    #set the correct username and password
    correct_username = "123"
    correct_password = "123"
    event_counter_password = "1234"
    bruteforce_password = "test123"
    bruteforce_max_attempts = 5

    if user_authentication(correct_username, correct_password) == False:
        return  # Exit the program if authentication fails 
    
    # function calls and keep the menu running until the user chooses to exit
    menu_choice = ""
    while menu_choice != "3":
        menu_choice = display_menu()
        
        if menu_choice == "1":
            print("Security Event Counter selected.")
            security_event_counter(event_counter_password)
            
        elif menu_choice == "2":
            print("Brute Force Attack Simulation selected.")
            brute_force_attack_simulation(bruteforce_password, bruteforce_max_attempts)

        elif menu_choice == "3":
            print("Exiting the program. Thank you for using my Security tool!")
            
        else:
            print("Invalid option. Please select a valid option (1-3).")
    
if __name__ == "__main__":
    main()