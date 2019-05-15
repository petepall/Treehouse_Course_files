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

# course_minutes = {
#     "Python basics": 232,
#     "Django basics": 237,
#     "Flask basics": 189,
#     "Java basics": 133,
# }

# for course, time in course_minutes.items():
#     print(f"{course:20}: {time:5}")


# E.g. word_count("I do not like it Sam I Am") gets back a dictionary like:
# {'i': 2, 'do': 1, 'it': 1, 'sam': 1, 'like': 1, 'not': 1, 'am': 1}
# Lowercase the string to make it easier.
# def word_count(data):
#     word_counter = {}
#     for word in data.lower().split():
#         word_counter[word] = data.lower().split().count(word)

#     return word_counter


# print(word_count("I do not like it Sam I Am"))


# The dictionary will look something like:
# {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#  'Kenneth Love': ['Python Basics', 'Python Collections']}
#
# Each key will be a Teacher and the value will be a list of courses.

# def num_teachers(data):
#     return len(data)


# def num_courses(data):
#     return sum(map(len, data.values()))


# def courses(data):
#     courses_list = [item for course in data.values() for item in course]
#     return courses_list


# def most_courses(data):
#     courses_count = 0
#     teacher_with_most_courses = ''

#     for teacher, courses in data.items():
#         if len(courses) > courses_count:
#             teacher_with_most_courses = teacher
#             courses_count = len(courses)

#     return teacher_with_most_courses


# def stats(data):
#     statistics = []
#     for teacher, courses in data.items():
#         statistics.append([teacher, len(courses)])
#     return statistics


# data = {'Andrew Chalkley': ['jQuery Basics', 'Node.js Basics'],
#         'Kenneth Love': ['Python Basics', 'Python Collections', 'test']}

# print(num_teachers(data))
# print(num_courses(data))
# print(courses(data))
# print(most_courses(data))
# print(stats(data))


# import random


# def get_location(cells):
#     return random.sample(cells, 3)


# print(get_location((1, 2, 3, 4, 5, 2, 4, 6)))

# def move(player, direction):
#     x, y, hp = player
#     dirx, diry = direction

#     if x + dirx < 0 or x + dirx > 9 or y + diry < 0 or y + diry > 9:
#         hp -= 5
#     else:
#         x += dirx
#         y += diry

#     return x, y, hp


# print(move((1, 1, 10), (-1, 0)))
# print(move((0, 1, 10), (-1, 0)))
# print(move((0, 9, 5), (0, 1)))

