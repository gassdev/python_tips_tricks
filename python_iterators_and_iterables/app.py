nums = [1, 2, 3]

i_nums = iter(nums)

# print(dir(i_nums))

# for num in nums:
#     print(num)

# print(next(i_nums))
# print(next(i_nums))
# print(next(i_nums))

while True:
    try:
        item = next(i_nums)
        print(item)
    except StopIteration:
        break