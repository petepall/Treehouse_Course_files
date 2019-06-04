import json


with open('file_processing\\148.json') as art_file:
    art = json.load(art_file)
    print(art)
    for key, value in art.items():
        if value is None:
            value = ""
        elif type(value) == str and ("\n" in value or "\r" in value):
            value = value.replace("\n", " - ").replace("\r", "")

        print(f"{key:25} -> {value}")
