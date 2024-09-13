#7) Create a lambda function to reverse a given string.

a = 'dev'

b = lambda x:x[::-1]

print(b(a))


#8) Write a lambda function to concatenate two strings with a space between them.

concat_strings = lambda s1, s2: s1 + ' ' + s2

string1 = "Hello"
string2 = "World"
result = concat_strings(string1, string2)
print(result)


#9) Use a lambda function to filter a list of strings, keeping only those that contain the letter 'a'.

#no


#10) Given a list of tuples where each tuple contains a person's name and age (e.g., [('Alice', 30),
# ('Bob', 25), ('Charlie', 35)]), use a lambda function to sort the list by age in descending order.

people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]
sorted_people = sorted(people, key=lambda x: x[1], reverse=True)
print(sorted_people)