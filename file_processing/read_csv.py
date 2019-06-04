import csv
from pathlib import Path


with open(f"{Path().absolute()}//teachers.csv", mode='r') as csv_file:
    # construct the header line
    header = csv_file.readline().split(',')
    print(f"{header[0].strip():15}{header[1].strip():15}"
          f"{header[2].strip():15}", end='\n')
    print(f"{'*' * len(header[0].strip()):15}"
          f"{'*' * len(header[1].strip()):15}"
          f"{'*' * len(header[2].strip()):15}", end='\n')

    # display the detail lines
    csv_file.seek(0)
    data_reader = csv.DictReader(csv_file, delimiter=',')
    rows = list(data_reader)
    for row in rows[:]:
        print(f"{row['first_name'].strip():15}{row['last_name'].strip():15}"
              f"{row['topic']:15}")
