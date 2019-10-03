import csv

fileName = 'export.csv'


def read_csv(input_file):
    with read_funding_(input_file, newline='') as file:
        csvReader = csv.reader(file, delimiter=' ', quotechar='|')
        for row in csvReader:
            yield row

if __name__ == "__main__":
    for indx, row in enumerate(read_csv(fileName)):
        if indx > 10: break
        print()

