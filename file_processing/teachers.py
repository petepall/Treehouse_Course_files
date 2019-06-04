import csv
from pathlib import Path


with open(f'{Path().absolute()}//teachers.csv', mode='a') as csv_file:
    fieldnames = ['first_name', 'last_name', 'topic']
    data_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)

    data_writer.writeheader()
    data_writer.writerow({
        'first_name': 'Kenneth',
        'last_name': 'Love',
        'topic': 'Python'
    })
    data_writer.writerow({
        'first_name': 'Alena',
        'last_name': 'Holligan',
        'topic': 'PHP'
    })
