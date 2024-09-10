
list_of_cars = ["Chevy", "Mustang", "C8"]

# variable car has the name of each car
for car in list_of_cars:
    print(car)

# variable index has only the current index as we are looping
for index in range(len(list_of_cars)):
    print(list_of_cars[index])

numbers = [10, 9, 8, 11, 12, 2]

# list comprehension example
small_numbers = [item for item in numbers if item < 10]
print(small_numbers)