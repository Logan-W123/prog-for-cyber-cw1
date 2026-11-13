import security_tools
 
 
def main() -> None:
 
    print("CYBER SECURITY UTILITIES")
    print("========================")
 
    #ask the user for a password and an ip address
    password = input("Please enter a password: ")
    ip_address = input("Please enter an IP address: ")
 
    #check if the password is strong and display the result
    if security_tools.validate_password(password):
        print("\nPassword: Valid - your password is strong.")
    else:
        print("\nPassword: Invalid - your password is not strong.")
        print("It must be at least 8 characters and contain a letter, a digit and a symbol.")
        print(f"Suggested strong password: {security_tools.generate_password()}")
 
    #check if the ip address is valid and display the result
    if security_tools.validate_ip(ip_address):
        print(f"\nIP Address: {ip_address} is valid.")
    else:
        print(f"\nIP Address: {ip_address} is invalid.")
        print("It must have four numbers between 0 and 255 separated by three dots.")
 
if __name__ == "__main__":
    main()