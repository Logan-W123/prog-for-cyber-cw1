#Logan Ward | ID: B01886641
#Task 2: Security Event Logger

import random
import socket
from datetime import datetime


    #get the local IP address of the machine
def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(("8.8.8.8", 80))
    ip_address = s.getsockname()[0]
    s.close()
    return ip_address


    #generate a random 4-digit event ID
def get_event_id():
    return random.randint(1000, 9999)


    #get the current timestamp in a readable format
def get_timestamp():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    

def check_login(correct_username, correct_password):
    while True:
        
        event_id = get_event_id()
        ip_address = get_ip_address()
        timestamp = get_timestamp()
        
        username = input("\nEnter username: ")
        password = input("Enter password: ")
        
        if username == correct_username and password == correct_password:
            print("Login successful!")
            event_log(event_id, username, ip_address, "Successful login", timestamp)
            return True
        
        else:
            print("Login failed! Please try again.")
            event_log(event_id, username, ip_address, "Failed login", timestamp)


def event_log(event_id, username, ip_address, event, timestamp):
    
    
    #display event log
    print("EVENT LOG")
    print("==========")
   
    print(f"Event ID: {event_id}")
    print(f"Username: {username}")
    print(f"IP Address: {ip_address}")
    print(f"Event: {event}")
    print(f"Timestamp: {timestamp}")


def main ()-> None:
    
    correct_username = "admin"
    correct_password = "P@ssw0rd123"

    
    check_login(correct_username, correct_password)
    
    
if __name__ == "__main__":
    main()

