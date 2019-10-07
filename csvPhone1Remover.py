import tkinter
import pandas as pd
import numpy as np

fileName = 'export.csv'


def removeDupe():

    # loads CSV into file
    data = pd.read_csv(fileName, encoding="utf-8", dtype=object)

    # See output of program
    # print(data.drop_duplicates(subset='Phone 1.1', keep="last"))
    # data.drop_duplicates(subset='Phone 1.1', keep="last").to_csv('unDuped-by-Phone.csv')

    # In 'subset' write all the fields you want to dedup with
    # data[['Name', 'Phone 1.1s']].duplicated(subset='Phone 1.1', keep='last').to_csv('DupForManualRemoval.csv')

    # to_csv by itself just gets rid of apostrophes in empty columns
    # data.to_csv('unDuped.csv')
    print("CSV generated.")


removeDupe()
