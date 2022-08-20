# creating my integer list between 5.5 to 20.5

numbers = list(range(6,21))

print(numbers)

# write a python program with the lambda function to count the even numbers on my list
even_num = filter(lambda x: x%2==0, numbers)

print(len(list(even_num)))

# write a python program with the lambda function to count the odd numbers on my list
odd_num = filter(lambda x: x%2==1, numbers)

print(len(list(odd_num)))

# write a python program with the lambda function to give ne the square of my numbers
square_num = list(map(lambda x: x**2, numbers))

print(square_num)

# write a python program with the lambda function to give me the cube of my numbers
cube_num = list(map(lambda x: x**3, numbers))

print(cube_num)
