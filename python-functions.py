# python3 python-functions.py

# 1. Write a function named `sum_to` that accepts a single integer, `n`, and returns the sum of the integers from 1 to `n`.

#For example:
# sum_to(6)  # returns 21
# sum_to(10) # returns 55

n = 6

def sum_to(n):
    return sum(range(n+1))

print(sum_to(n))

# 2. Write a function named `largest` that takes a list of numbers as an argument and returns the largest number in that list.
    
# For example:
# largest([1, 2, 3, 4, 0])  # returns 4
# largest([10, 4, 2, 231, 91, 54])  # returns 23

def largest(li):
  return max(li)

print(largest([1, 2, 3, 4, 0]))

# 3. Write a function named `occurrences` that takes two string arguments as input and counts the number of occurrences of the second string inside the first string.

# For example:

# occurrences('fleep floop', 'e')   # returns 2
# occurrences('fleep floop', 'p')   # returns 2
# occurrences('fleep floop', 'ee')  # returns 1
# occurrences('fleep floop', 'fe')  # returns 0