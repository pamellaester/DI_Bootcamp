#  Exercise 1: Identifying Time Complexity

# for i in range(10):
#     print(i)

# O(N)


# for i in range(n):
    # for j in range(n):
    #     print(i, j)

# O(N^2)

# i = 1
# while i < n:
#     i *= 2
#     print(i)

# O(2^N)

# Exercise 2: Understanding Insertion Sort

# numbers = [5, 2, 9, 1, 5, 6]

# def insertion_sort(numbers: list) -> None:
#   def insertion_sort(numbers: list) -> None:
#    for i in range(1, len(numbers)):
#       value = numbers[i]
#       j = i - 1
#       while value < numbers[j] and j >= 0:
#          numbers[j + 1] = numbers[j]
#          j -= 1
#       numbers[j + 1] = value

# insertion_sort(numbers) # sorts the numbers list
# print(numbers) # check that the sorting is successfull

# Exercise 3: Understanding Binary Search

numbers = [1, 3, 5, 7, 9, 11]

def binary_search(numbers: list, value: int) -> int:
  low = 0
  high = len(numbers) -1
  while low <= high:

        mid = low + (high - low)//2

        if numbers[mid] == value:
            return mid 
        elif numbers[mid] < value:
            low = mid + 1
        else:
            high = mid - 1 

  return -1  
    
result = binary_search(numbers, 7)
 # returns 3
if result != -1:
    print("Element is present at index " + str(result))
else:
    print("Not found")
