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

    line = re.search(r'''
        ^(?P<name>[-\w ]*,\s[-\w ]+)\t  # Last and first names
        (?P<email>[-\w\d.+]+@[-\w\d.]+)\t  # Email
        (?P<phone>\(?\d{3}\)?-?\s?\d{3}-\d{4})?\t  # Phone number
        (?P<job>[\w\s]+,\s[\w\s.]+)?\t  # Job and company
        (?P<twitter>@[\w\d]+)?$  # Twitter
    ''', data, re.X | re.M)

    print(line)
    print(line.groupdict())
