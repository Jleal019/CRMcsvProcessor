import tkinter
import csv
import pandas
import numpy

fileName = 'export.csv'

'''Fix last name issue
'''


def removeDupe():

    # loads CSV into file
    data = pandas.read_csv(fileName, delimiter=",", encoding="utf-8", dtype=object)
    print(data, '\n -------------------Unprocessed data above---------------------')

    # --- See output of program ---
    # In 'subset', write all the fields you want to dedup with
    # print(data.drop_duplicates(subset='Phone 1.1', keep="last"))

    # data.drop_duplicates(subset='Phone 1.1', keep="last").to_csv('unDuped-by-Phone.csv')

    # Prints specific column values
    print(data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last'))
    data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last').to_csv('Specific-Columns.csv')

    # to_csv by itself just gets rid of quotations in empty columns
    # data.to_csv('unDuped.csv')
    print("CSV generated.")

    findDiff(fileName, 'test.csv')


def findDiff(ref, diff):
    print("---------------- Diff Data ---------------------------")

    data = pandas.read_csv(ref, delimiter=',', encoding="utf-8", dtype=object)
    data2 = pandas.read_csv(diff, delimiter=',', encoding="utf-8", dtype=object)
    catData = pandas.concat([data, data2], axis=1)

    print(catData[["Name", "Phone 1.1"]])


removeDupe()
