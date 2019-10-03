import csv

fileName = 'export.csv'


with open(input_file, newline='') as file:
    csvReader = csv.reader(file, delimiter=',')
    for row in csvReader:
        print(row)
