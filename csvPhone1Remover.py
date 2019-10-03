import tkinter
import pandas as pd

fileName = 'export.csv'


def removeDupe():
    try:
        # loads CSV into file
        data = pd.read_csv(fileName, encoding="utf-8", dtype=object)

        # In 'subset' write all the fields you want to dedup with
        data.drop_duplicates(subset=['Phone 1'], keep='first')

        print(data.drop_duplicates(subset=['Phone 1'], keep='first'))

        # saves new CSV with removed dupes
        # data.to_csv(r'unDuped.csv')

        print("CSV generated.")

    except KeyError:
        print("It seems you have entered some values incorrectly. Please try again.")
        removeDupe()


removeDupe()
