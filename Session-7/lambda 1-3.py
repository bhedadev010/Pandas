#1) Given a list of integers, use a lambda function to filter out all the even numbers

a = [1,2,3,4,5,6,7,8,9]

b = list(filter(lambda x:x%2==0,a))
print(b)


#2) Write a lambda function to sort a list of strings based on their length.

b = ['wsd','dvvc','de','devvv']

c = sorted(b,key=lambda x:len(x))
print(c)


#3) Use a lambda function to create a new list where each number in the original list is doubled.

b = [1,2,3,4,5,5,7,8,9]
c = list(map(lambda x:x+x,b))
print(c)