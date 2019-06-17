import csv
from pathlib import Path


with open(f"{Path().absolute()}\\file_processing\\teachers.csv",
          mode='r') as csv_file:

    # construct the header line
    data_reader = csv.DictReader(csv_file, delimiter=',')
    print(f"{data_reader.fieldnames[0].capitalize():15}"
          f"{data_reader.fieldnames[1].capitalize():15}"
          f"{data_reader.fieldnames[2].capitalize():15}")

    print(f"{'*' * len(data_reader.fieldnames[0].strip()):15}"
          f"{'*' * len(data_reader.fieldnames[1].strip()):15}"
          f"{'*' * len(data_reader.fieldnames[2].strip()):15}", end='\n')

    # display the detail lines
    rows = list(data_reader)
    for row in rows[:]:
        print(f"{row['first_name'].strip():15}{row['last_name'].strip():15}"
              f"{row['topic']:15}")
