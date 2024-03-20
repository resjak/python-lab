#Creating a set
vlans = {10,20,30,40,50}
protocols = set(['OSPF','BGP','EIGRP'])
print(vlans)
print(protocols)

print("\n")


#Adding elements to a set
vlans.add(60)
print(vlans)

print("\n")


#Removing elements from a list
vlans.remove(10)
protocols.discard('EIGRP')
print(vlans)
print(protocols)


#SET OPERATIONS
#Union
a = {1,2,3}
b = {3,4,5}
union_set = a.union(b)
print("Union set:",union_set)

#Intersection
intersection_set = a.intersection(b)
print("Intersection set:",intersection_set)

#Difference
difference_set = a.difference(b)
print("Difference set:",difference_set)

#Unique IP address
ips = set()
ips.add('192.168.1.1')
ips.add('192.168.0.1')
ips.add('192.168.1.1')
print("IPs: ",ips)

#Comparing VLAN configs
switch1_vlans = {10,20,30}
switch2_vlans = {20,30,40}
missing_vlans = switch1_vlans.difference(switch2_vlans)
print("Missig VLANS: ",missing_vlans)