import csv

csvfile = open('data-text.csv', 'r', encoding='utf-8')
reader = csv.DictReader(csvfile)

for row in reader:
    print(row)
