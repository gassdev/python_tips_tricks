# def square_numbers(nums):
#     for i in nums:
#         yield (i*i)

# my_nums = square_numbers([1,2,3,4,5])
my_nums = (x*x for x in [1,2,3,4,5]) # returns a generator


# for num in my_nums:
#     print(num)

print(next(my_nums))
print(next(my_nums))
print(next(my_nums))