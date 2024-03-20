#Defining a dictionary
device={
    "hostname": "Router1",
    "ip": "192.168.1.1",
    "model": "Cisco 2901",
    "interfaces": ["GigabitEthernet0","GigabitEthernet1"]
}
print(device)


#Accessing dictionary values
ip_address = device["ip"]
print(f"\nDevice IP address: {ip_address}")


#Adding a new key-value pair
device["location"]="Data Center A"
print(device)


#Modyfying an existing value
device["ip"]="192.168.2.1"
print(device)


#Removing a key-value pair
del device["model"] #Using del
location = device.pop("location")#Using pop, also retrieves the value
print(device)


#Iterating through keys
for key in device.keys():
    print(key)


#Iterating through values
for value in device.values():
    print(value)

#Iterating through key-value pairs
for key, value in device.items():
    print(f"{key}: {value}")

#DICTIONARIES IN NETWORKING
#Storing routing information
routing_table = {
    "10.0.0.0/24": "192.168.1.1",
    "172.16.0.0/16": "192.168.2.1"
}
for network, next_hop in routing_table.items():
    print(f"Destination: {network}, Next Hop: {next_hop}")
