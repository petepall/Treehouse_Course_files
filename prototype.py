# favorite_things = ['raindrops on roses', 'whiskers on kittens',
#                    'bright copper kettles', 'warm woolen mittens',
#                    'bright paper packages tied up with string',
#                    'cream colored ponies', 'crisp apple strudels']

# slice1 = favorite_things[1:4]
# slice2 = favorite_things[-2:]
# sorted_things = favorite_things[:]
# sorted_things.sort()

# print(sorted_things)

# number = list(range(20))
# print(number)
# print(number[::2])
# print(number[2::2])
# print(number[-2::])
# print(number[::-1])


# def first_4(data):
#     return data[0:4]


# print(first_4([1, 2, 3, 4, 5]))


# def first_and_last_4(data):
#     value = data[:4] + data[-4:]
#     print(value)
#     return value


# # def first_and_last_4(firstlast):
# #     first = firstlast[:4]
# #     last = firstlast[-4:]
# #     first_and_last = first + last
# #     return(first_and_last)


# print(first_and_last_4([1, 2, 3, 4, 5, 6, 7, 8, 9]))


# def odds(data):
#     return data[1::2]


# print(odds([1, 2, 3, 4, 5, 6, 7, 8, 9]))

# def reverse_evens(data):
#     value = data[::2]
#     return value[::-1]


# print(reverse_evens([1, 2, 3, 4, 5, 6]))

# """I need you to create a new function for me.
# This one will be named sillycase and it'll take a single string as an argument.

# sillycase should return the same string but the first half should be lowercased 
# and the second half should be uppercased. For example, with the string 
# \"Treehouse\", sillycase would return \"treeHOUSE\".

# Don't worry about rounding your halves, but remember that indexes should be 
# integers. You'll want to use the int() function or integer division, //."
# """


# def sillycase(data):
#     first_half = data[: (len(data) // 2)].lower()
#     second_half = data[(len(data) // 2):].upper()
#     return first_half + second_half


# print(sillycase("Treehouse"))

