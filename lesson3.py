import numpy as np

# using the range data type to create an array of numbers from 1-100
numbers = np.arange(1,101)

#checking my numbers
print(numbers)

# using the lcm function to help find the lowest common factor of the even numbers in my range
x = np.lcm.reduce(numbers[numbers%2==0])

# checking my answer
print(x) 