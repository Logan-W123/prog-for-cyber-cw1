#Logan Ward | ID: B01886641
#Data Structures and Modules
#Task 3
#4/11/2026

#update the risk level of the incident
def update_risk_level(incident: dict, new_risk_level: str) -> dict:
    incident["risk_level"] = new_risk_level
    return incident

def main() -> None:
    
    #create a dictionary containing the username, ip address, event type and risk level
    incident = {
        "username": "admin",
        "ip_address": "192.168.1.25",
        "event_type": "Failed login",
        "risk_level": "Medium"
    }
 
    #display the username and ip address
    print("SECURITY INCIDENT MANAGER")
    print("=========================")
    print(f"Username: {incident['username']}")
    print(f"IP Address: {incident['ip_address']}")
 
    #add a new field called status
    incident["status"] = "Under investigation"
    print(f"\nNew field added - status: {incident['status']}")
 
    #ask the user for the new risk level
    new_risk_level = input("\nPlease enter the new risk level (Low/Medium/High): ")
    incident = update_risk_level(incident, new_risk_level)
    print(f"Risk level updated to: {incident['risk_level']}")
 
    #remove the event type field from the dictionary
    del incident["event_type"]
    print("\nThe event_type field has been removed.")
 
    #display all remaining keys and values
    print("\nRemaining keys and values:")
    for key, value in incident.items():
        print(f"{key}: {value}")
 
    #display the total number of key-value pairs
    print(f"\nTotal number of key-value pairs: {len(incident)}")
    

if __name__ == "__main__":
    main()