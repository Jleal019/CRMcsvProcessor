import pandas, numpy, csv, tkinter, re, phonenumbers

'''
Written on Python 3.7.3
using Pandas 0.25.1, Numpy 1.17.2 

-Fix last name issue

-Deleting whole columns is faster in Excel/Calc
'''
fileName = 'export.csv'

# creates CSV dataframe using pandas
data = pandas.read_csv(fileName, delimiter=",", encoding="utf-8", dtype=object)


# removes hello@gmail.com use from the Email column
data = data.replace(to_replace='hello@gmail.com', value='')

# removes leading 1's from phone numbers
data['Phone 1.1'] = data['Phone 1.1'].str.lstrip('+1')


def removeDupe():

    # loads CSV into file

    # --- See output of program without changes ---
    # print(data.drop_duplicates(subset='Phone 1.1', keep="last"))

    # --- Remove trailing 1's ---

    # In 'subset', write all the fields you want to deduplicate with
    # A new file will be created called 'unDuped-by-Phone.csv'
    # This is the file without duplicates
    # data.drop_duplicates(subset='Phone 1.1', keep="last").to_csv('unDuped-by-Phone.csv')

    # Prints specific column values
    print(data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last'))
    data[["Name", "Phone 1.1"]].drop_duplicates(subset='Phone 1.1', keep='last').to_csv('Specific-Columns.csv')

    # to_csv by itself just gets rid of quotations in empty columns
    # data.to_csv('unQuoted.csv')
    print("CSV generated.")

    # findDiff(fileName, 'test.csv')


def findDiff(ref, diff):
    print("---------------- Diff Data ---------------------------")

    data1 = pandas.read_csv(fileName, delimiter=',', encoding="utf-8", dtype=object)
    data2 = pandas.read_csv(diff, delimiter=',', encoding="utf-8", dtype=object)

    catData = pandas.concat([data1, data2], axis=1)

    print(catData.drop_duplicates(subset='Phone 1.1'))

    print(catData[["Name", "Phone 1.1"]])

removeDupe()
