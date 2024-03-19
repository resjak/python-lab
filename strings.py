#Creating a String
single_quoted_string = 'Hello, Python!'
double_quoted_string = "Hello, Python!"
print ('\nSingle quoted string is:',single_quoted_string)
print ('\nDouble quoted string is:',double_quoted_string)


#String concatenation
greeting = '\nHello'
target = "World"
message = greeting+", "+target+"!"
print(message)


#Basic usage of f-strings
name = "Python"
version = 3.8
message=f"\nWelcome to {name} version {version}!"
print(message)


#Expressions in f-strings
a=5
b=10
result_message = f"\nThe sum of {a} and {b} is {a+b}."
print(result_message)


#String lenght
lenght = len(message)
print("\nLenght of the message is:",lenght,'\n')


#Extracting the IP address
cidr_notation = "172.168.1.1/24"
ip_address = cidr_notation.split('/')[0]
print('IP address is:',ip_address)


#Extracting each octed
first_octet = ip_address[:ip_address.index('.')]
print('\nFirst octet:',first_octet)

second_octet_start = ip_address.index('.')+1
second_octet_end = ip_address.index('.',second_octet_start)
second_octet = ip_address[second_octet_start:second_octet_end]
print('\nSecond octet:',second_octet)

subnet_mask = cidr_notation.split('/')[1]
print('\nSubnet mask:',subnet_mask)

