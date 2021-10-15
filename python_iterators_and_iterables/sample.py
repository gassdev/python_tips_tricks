def my_range(start, end):
    current = start
    while current <= end:
        yield current
        current += 1

nums = my_range(1, 10) # my_range(1, 10) return a generator
# print(dir(nums))

# for num in nums:
#     print(num)

while True:
    try:
        print(next(nums))
    except StopIteration:
        break