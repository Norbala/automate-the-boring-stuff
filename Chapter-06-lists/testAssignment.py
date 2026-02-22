def eggs(some_parameter):
    some_parameter.append('Hello')

spam = [1, 2, 3]
test = eggs(spam)
print(spam)  # Prints [1, 2, 3, 'Hello']

print(test)