#Definition of a list
my_list =[1,2,3,"Python",3.14]
print(my_list)

#Accessing list elements
first_item = my_list[0] #Gets the first item, 1
print("First item of the list is:",first_item)

#Adding element to the list
my_list.append("new item")
print(my_list)

#Removing elements from a list
my_list.remove("Python")
print(my_list)


#Using a for loop
for item in my_list:
    print(item)

#Using the enumerate() function
for index, item in enumerate(my_list):
    print(index+1,"element of list is:",item)

#List Comprehensions
squared_numbers = [x**2 for x in range(10)]
print(squared_numbers)

#Fibonacci Numbers
f_id=0
f_idx=1
fib_num = [f_id,f_idx]

for n in range(10):
    next_num=f_id + f_idx
  
    f_id=f_idx
    f_idx=next_num
    
    fib_num.append(next_num)
    print(fib_num)
