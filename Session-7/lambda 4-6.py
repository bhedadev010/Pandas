#4) Create a lambda function that returns another lambda function which adds a specified number to its argument.

#no


#5) Given a list of integers, use a lambda function to filter out all numbers greater than 10

a = [12,14,52,120,9,8,7]

b = list(filter(lambda x:x>10,a))
print(b)


#6) Write a lambda function to find the maximum value in a list of numbers.

b = lambda x:max(x)
print(b(a))