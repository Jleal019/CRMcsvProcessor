import tkinter
import pandas as pd
import numpy as np

fileName = 'export.csv'


def removeDupe():
    try:
        # loads CSV into file
        data = pd.read_csv(fileName, encoding="utf-8", dtype=object)

        # In 'subset' write all the fields you want to dedup with

        data.drop_duplicates(subset='Phone 1.1', keep='last').to_csv('unDuped.csv')

        print("CSV generated.")

    except KeyError:
        print("It seems you have entered some values incorrectly. Please try again.")
        removeDupe()


removeDupe()
