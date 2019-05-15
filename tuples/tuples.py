# def multiply(*args):
#     product = 0
#     for nums in args:
#         if product == 0:
#             product = nums
#         else:
#             product *= nums

#     return product


# print(multiply(5, 4, 3))


# def stringcases(data):
#     return (data.upper(), data.lower(), data.title(), data[::-1])


# print(stringcases("hello"))


# combo([1, 2, 3], 'abc')
# Output:
# [(1, 'a'), (2, 'b'), (3, 'c')]
def combo(data1, data2):
    return [(data1[i], data2[i]) for i in range(0, len(data1))]


print(combo([1, 2, 3], 'abc'))
