#Extracting substrings
greeting = "Hello, Python!"
sub_greeting = greeting[0:5] #Extracts 'Hello'
print(sub_greeting)


#Omitting Indices
language = greeting[7:] #Extracts 'Python'
print(language)


#Skipping characters
skip_chars = greeting[::2] #Extracts 'Hlo yhn
print(skip_chars)


#Reversing a string
reversed_greeting = greeting[::-1]  #Reverses the string
print(reversed_greeting)

#Negative start or end indices
last_chars = greeting[-7:] #Extracts Python!
print(last_chars)

#Combining positive and negative indices
middle_chars=greeting[2:-1]
print(middle_chars)

#Step with start and end
nth_chars = greeting[1:10:3]
print(nth_chars)