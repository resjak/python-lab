#Defining a simple functions
def greet():
    print("Hello, Network Engineer!")

#Function with positional arguments
def configure_interface(interface_name, ip_address):
    print(f"Configuring {interface_name} with IP {ip_address}")


#Calling a function
greet()
configure_interface("GigabitEthernet0/1","192.168.1.1")
configure_interface(ip_address="192.168.1.1",interface_name="GigabitEthernet0/1")


#Return multiple values
def calculate_metrics(bytes_transmitted, bytes_received):
    tx_rate = bytes_transmitted / 60   #Assuming bytes per minute for simplicity
    rx_rate = bytes_received / 60
    return tx_rate, rx_rate

tx, rx = calculate_metrics(3000, 5000)
print(f"Transmit rate: {int(tx)} Bps, Receive rate: {int(rx)} Bps")


#Function with default argument values
def ping (host = "8.8.8.8", count=4):
    print(f"Pinging {host} {count} times...")
    return "Ping successful"

print (ping()) #uses default values
print(ping("192.168.1.1")) #Overrides only the host
print(ping(count=8)) #Overrides only the count


