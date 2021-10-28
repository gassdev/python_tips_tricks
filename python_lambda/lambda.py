# def double(x): return x*2

# def add(x, y): return x+y

# def product(x, y, z): return x*y*z

from functools import reduce

double = lambda x: x*2
add = lambda x, y: x+y
product = lambda x, y, z: x*y*z

print(double(10))
print(add(10, 5))
print(product(3,4,5))

# filter, reduce, map
my_list = [2, 5, 8, 10, 9, 3]
my_list2 = [1, 4, 7, 8, 5, 1]

a = map(lambda x: x*2, my_list)
print(list(a))
b = map(lambda x, y: x+y, my_list, my_list2)
print(list(b))

c = filter(lambda x: x%2 == 0, my_list)
print(list(c))

d = filter(lambda x: True if x>5 else False, my_list)
print(list(d))

e = reduce(lambda x, y : x+y, my_list)
print(e)