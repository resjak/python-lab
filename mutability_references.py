#Strings are immutable
my_string = "Hello, Python!"

try:
    my_string[7] = 'W' #Trying to replace 'P' with 'W'
except TypeError as e:
    print('\n',e) 



#Lists are Mutable
my_list = [1,2,3,4]
my_list[2] = 30 #Changing the third element from 3 to 30
print('\n',my_list)



#Copying References
original_list = [1,2,3]
new_list = original_list #This copies the reference, not the list
new_list[1] = 200 #Modifies the original list as well
print("\nOriginal list values:",original_list)



#Independent copies
independent_copy = original_list[:]
independent_copy[1] = 20
print('\nOriginal list:',original_list)
print('\nIndependent copy:',independent_copy)



#Integers are immutable
a=10
b=a
b=5
print('\n"a" value is:',a,'and "b" value is:',b)

lst1=[1,2,3]
lst2 = lst1
lst2.append(4)
print('\n',lst1)