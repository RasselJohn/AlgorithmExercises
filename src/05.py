# Change 2 variables without third

# one way
a = 3
b = 2
print("a = {0}, b = {1}".format(a, b))

a, b = b, a
print("a = {0}, b = {1}".format(a, b))

# second way
a = 3
b = 2
print("a = {0}, b = {1}".format(a, b))

a = a + b
b = a - b
a = a - b
print("a = {0}, b = {1}".format(a, b))
