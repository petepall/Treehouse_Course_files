import sys
from pathlib import Path


def rememberer(thing):
    with open(f"{Path().absolute()}//notes.txt", mode='a') as notes_file:
        notes_file.writelines(f"{thing}\n")


def show():
    with open(f"{Path().absolute()}//notes.txt", newline='', mode='r')\
            as notes_file:
        for line in notes_file:
            print(line)


if __name__ == "__main__":
    if sys.argv[1].lower() == '--list':
        show()
    else:
        rememberer(' '.join(sys.argv[1:]))
