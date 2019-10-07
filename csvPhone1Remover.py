import tkinter
import pandas as pd
import numpy as np

fileName = 'export.csv'


def removeDupe():

    # loads CSV into file
    data = pd.read_csv(fileName, delimiter=",", encoding="utf-8", dtype=object)
    print(data, '\n -------------------Unprocessed data above---------------------')

    # See output of program
    # In 'subset' write all the fields you want to dedup with
    # print(data.drop_duplicates(subset='Phone 1.1', keep="last"))

    # data.drop_duplicates(subset='Phone 1.1', keep="last").to_csv('unDuped-by-Phone.csv')

    # Prints specific column values
    print(data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last'))
    # [data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last').to_csv('SpecificColumns.csv')


    # to_csv by itself just gets rid of quotations in empty columns
    # data.to_csv('unDuped.csv')
    print("CSV generated.")


removeDupe()
