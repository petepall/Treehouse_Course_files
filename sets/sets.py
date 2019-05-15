# songs = set({
#     "Leef",
#     "I drove all night",
#     "Suzanne"
# })

# songs.add("Treehouse Hula")

# songs.update({"Python Two-Step", "Ruby Rhumba"}, {"My PDF Files"})

# print(songs)


# set1 = set(range(10))
# set2 = set({1, 2, 3, 5, 7, 11, 13, 17, 19, 23})

# print(set1.union(set2))
# print(set1 | set2)
# print(set1.difference(set2))
# print(set1 - set2)
# print(set2.difference(set1))
# print(set2 - set1)
# print(set2.symmetric_difference(set1))
# print(set1 ^ set2)
# print(set1.intersection(set2))
# print(set1 & set2)


COURSES = {
    "Python Basics": {"Python", "functions", "variables",
                      "booleans", "integers", "floats",
                      "arrays", "strings", "exceptions",
                      "conditions", "input", "loops"},
    "Java Basics": {"Java", "strings", "variables",
                    "input", "exceptions", "integers",
                    "booleans", "loops"},
    "PHP Basics": {"PHP", "variables", "conditions",
                   "integers", "floats", "strings",
                   "booleans", "HTML"},
    "Ruby Basics": {"Ruby", "strings", "floats",
                    "integers", "conditions",
                    "functions", "input"}
}


def covers(data):
    output = []
    for key in COURSES.keys():
        if data.intersection(COURSES[key]):
            output.append(key)
    return output


def covers_all(data):
    output = []
    for key in COURSES.keys():
        if data.issubset(COURSES[key]):
            output.append(key)
    return output


print(covers({"Python"}))
print(covers_all({"conditions", "input"}))
