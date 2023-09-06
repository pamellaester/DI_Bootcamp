# square = lambda n : n*n
# num = square(5)
# print(num)

# myList = [10, 25, 17, 9, 30, -5]
# # Double the value of each element
# myList2 = map(lambda n : n*2, myList)
# print (list(myList2))

# Exercise
#  1. create a function that takes a number as an argument, and check if this number is even or odd
# 2. create a function that takes a list of numbers as an argument, and check if each number is even or odd

# def number(input('insert a number: \n')):
#    if (a % 2) == 0:
#       print ('the number {a} is even')
#    if (a % 2) != 0:
#       print ('the number {a} is odd')

# number()
# print ('the number {a} is even')
# print ('the number {a} is odd')


def highest_even (li):
   evens = []
   for item in li:
     item % 2 == 0 
     evens.append(item)
     # function to reach te hights amount in the list
    return max(evens)    
    

print(highest_even ([10,2,3,4,5,6,11]))
