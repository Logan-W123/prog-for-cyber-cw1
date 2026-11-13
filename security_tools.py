import random
import string
 
#check if the password is strong (minimum length, a character, a digit and a symbol)
def validate_password(password: str) -> bool:
    has_letter = False
    has_digit = False
    has_symbol = False
 
    for char in password:
        if char.isalpha():
            has_letter = True
        elif char.isdigit():
            has_digit = True
        elif char in string.punctuation:
            has_symbol = True
 
    return len(password) >= 8 and has_letter and has_digit and has_symbol
 
#check if the ip address is valid (three dots, four numbers, each between 0 and 255)
def validate_ip(ip_address: str) -> bool:
    if ip_address.count(".") != 3:
        return False
 
    octets = ip_address.split(".")
    for i in octets:
        if not i.isdigit():
            return False
        if int(i) < 0 or int(i) > 255:
            return False
 
    return True
 
#generate a strong random password between 10 and 16 characters long
def generate_password() -> str:
    length = random.randint(10, 16)
 
    #make sure there is at least one of each type of character
    password_chars = [
        random.choice(string.ascii_uppercase),
        random.choice(string.ascii_lowercase),
        random.choice(string.digits),
        random.choice(string.punctuation)
    ]
 
    #fill the rest of the password with random characters from all types
    all_chars = string.ascii_letters + string.digits + string.punctuation
    for i in range(length - 4):
        password_chars.append(random.choice(all_chars))
 
    #shuffle so the guaranteed characters are not always at the start
    random.shuffle(password_chars)
    return "".join(password_chars)