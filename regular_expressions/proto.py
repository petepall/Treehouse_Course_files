from os import path
import re

with open(path.join(path.dirname(__file__), 'names.txt'), mode='r',
          encoding="utf-8") as file:
    data = file.read()

    # print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
    # print(re.search(r'\w+, \w+', data))
    # print(re.findall(r'\(?\d{3}\)?-?\s?\d{3}-\d{4}', data))
    # print(re.findall(r'\w*, \w+', data))
    # print(re.findall(r'[-\w\d+.]+@[-\w\d.]+', data))
    # print(re.findall(r'\b[trehous]{9}\b', data, re.I))
    # print(re.findall(r'''
    #       \b@[-\w\d.]*  # first a word boundry and @, and then any # of char
    #       [^gov\t]+  # Ignore 1+ instances of the letters g o or v an a tab
    #       \b  # match another word boundry
    #     ''', data, re.VERBOSE | re.I))

    # print(re.findall(r"""
    #     \b[-\w]*,  # find a word boundary, 1+ hyphen or char, and a comma
    #     \s  # find 1 whitespace
    #     [-\w ]+  # 1+ hyphens and char and explicit spaces
    #     [^\t\n]  # Ignore tabs and newlines
    #  """, data, re.X))

    data_format = re.compile(r'''
        ^(?P<name>(?P<last>[-\w ]*),\s(?P<first>[-\w ]+))\t  # Last and first names
        (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
        (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone number
        (?P<job>[\w\s]+,\s[\w\s.]+)?\t  # Job and company
        (?P<twitter>@[\w\d]+)?$  # Twitter
    ''', re.X | re.M)

    # print(re.search(line, data).groupdict())
    # print(line.search(data).groupdict())

    # for match in line.finditer(data):
    #     print('{first} {last} <{email}>'.format(**match.groupdict()))


class Person:
    """Represents a persons data"""

    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def __str__(self):
        string = ''
        for key, value in self.__dict__.items():
            string += f"{key}: {value}\n"
        return string

    @classmethod
    def construct(cls, list, expr, data):
        for match in expr.finditer(data):
            list.append(cls(**match.groupdict()))


class AdressBook(list):
    """Represents the addressbook"""

    def search(self, term=None):
        if term:
            result = []
            for person in self:
                for key, value in person.__dict__.items():
                    try:
                        if term in value and person not in result:
                            result.append(person)
                    except (AttributeError, TypeError):
                        continue
            return result
        return self


if __name__ == "__main__":
    address_book = AdressBook()
    Person.construct(address_book, data_format, data)
    for item in address_book.search('kenneth'):
        print(item)
