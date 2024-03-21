class NetworkDevice:

    def __init__(self,hostname,ip_address):
        self.hostname=hostname
        self.ip_address=ip_address

    def display_config(self):
        print(f"Hostname: {self.hostname}, IP Address:{self.ip_address}")


class Router(NetworkDevice):
    def __init__(self, hostname, ip_address, routing_protocol):
        super().__init__(hostname,ip_address)
        self.routing_protocol = routing_protocol
        
#polymorphism
    def display_config(self):
        super().display_config()
        print(f"Routing protocol: {self.routing_protocol}")
#####




router = NetworkDevice("Router1","192.168.1.1")
#router.display_config()
#print(f"Device: {router.hostname}, IP:{router.ip_address}")

router = Router("Router1", "192.168.1.1", "OSPF")
#print(f"Routing protocol: {router.routing_protocol}")

router.display_config()
    
