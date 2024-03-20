#Basic if statement
port_status = "up"
if port_status == "up":
    print("The port is operational.")

print("\n")


#Adding else
if port_status=="up":
    print("The port is operational.")
else:
    print("The port is down.")

print("\n")


#Using elif for multiple conditions
port_speed = 1000
if port_speed == 100:
    print("FastEthernet port.")
elif port_speed == 1000:
    print ("GigabitEthernet port.")
else:
    print("Speed unrecognized.")

#EXERCISE - VLAN configuration check
interface_configs = {
    "GigabitEthernet0/1":{"Status": "up","vlan": "10"},
    "GigabitEthernet0/2":{"Status": "down","vlan": "20"},
    "GigabitEthernet0/3":{"Status": "up","vlan": "10"},
}

#status = {interface:portstat for interface, portstat in interface_configs.items()}
#print(status)