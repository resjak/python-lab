#Basic dictionary comprehension
numbers = [1,2,3,4,5]
squares = {n:n**2 for n in numbers}
print(squares)

print("\n")


#Conditional dictionary comprehension
even_squres = {n:n**2 for n in numbers if n%2 == 0}
print(even_squres)

print("\n")


#Mapping IP address to devices
devices = ["Router1", "Switch1","Router2"]
ips = ["192.168.1.1", "192.168.1.2", "192.168.1.3"]
ip_device_map = {ips[i]:devices[i] for i in range(len(devices))}
print(ip_device_map)

print("\n")


#Interface speed mapping
interfaces = ["Gig0/0", "Gig0/1", "Fa0/0"]
speeds = ["1Gbps", "1Gbps", "100Mbps"]
interface_speed = {interfaces[i]: speeds[i] for i in range(len(interfaces)) }
print(interface_speed)

print("\n")


#Filtering dictionary entries
devices_types = {"Router1":"Router","Switch1":"Switch","Router2":"Router"}
routers_only = {device: type for device, type in devices_types.items()if type=="Router"}
print(routers_only)

print("\n")