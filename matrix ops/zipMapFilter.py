def even(number):
    if (number % 2) == 0:
        return  True
    return  False

def square(number):
    return number*number

numbers = [1,2,3,4,5]
even_numbers = filter(even, numbers)
even_numbers_squared = map(square, even_numbers)

print(list(even_numbers))
print(list(even_numbers_squared))

even_numbers = [2,4]
even_numbers_squared = [4, 8]
zipped_result = zip(even_numbers, even_numbers_squared)
print(list(zipped_result))