#Defining a tuple
device = ('Router','192.168.1.1','Cisco')
print(device)


#Tuple without parentheses
interface = "GigabitEthernet0","up",1000 #Interface name, status, speed
print(interface)


#Attempting to modify a tuple
try:    
    device[1] = "192.168.2.1" #Attempt to change the IP address
except TypeError as e:
    print(e)


#Unpacking a tuple
name,ip,brand = device
print(f"Name: {name}, IP: {ip}, Brand: {brand}")


#TUPLES IN NETWORKING
#Storing device configuration
device_info=("Router1","172.168.0.1","Juniper",22) #Hostname, IP, Model, SSH port

#Endpoint addressing
endpoint = ("10.10.10.1",443) #IP address and port
