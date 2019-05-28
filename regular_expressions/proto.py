from os import path
import re

with open(path.join(path.dirname(__file__), 'names.txt'), mode='r',
          encoding="utf-8") as file:
    data = file.read()

    print(re.search(r'\(\d\d\d\) \d\d\d-\d\d\d\d', data))
