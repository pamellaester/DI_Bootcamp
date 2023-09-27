import itertools

def subsetsum(numbers: list, target: int) -> bool:
    for numbers in itertools.combinations(numbers,2):
     if sum(numbers) == target:
        print([numbers.index(number) for number in numbers])
            
numbers = [12, -7, 20, 1, 4, -10, -1]

subsetsum(numbers, 1) # False
subsetsum(numbers, 2) # True: 12,  -10
subsetsum(numbers, 3) # True: 4,  -1
subsetsum(numbers, 4) # False