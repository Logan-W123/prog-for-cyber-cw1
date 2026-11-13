#Logan Ward | ID: B01886641
#Task 3: IP Address Validator


#check if the IP is valid
def Validate_IP(ip_address):
    
    
    ip_address = ip_address.strip()
    
    if "." not in ip_address:
        return False
    
    
    if ip_address.count(".") != 3:
        return False
    
    octet = ip_address.split(".")
    
    if len(octet) != 4:
        return False
    
    for i in octet:
        if not i.isdigit():
            return False
                
        number = int(i)
        
        if number <0 or number >255:
            return False
             
    return True

def main() -> None:
    
    #ask user for an ip address
    ip_address = input("Enter an IP address: ")
    
    
    #display the results
    if Validate_IP(ip_address):
        print("Valid IP address")
    else:
        print("Invalid IP address")
    
    
if __name__ == "__main__":
    main()
