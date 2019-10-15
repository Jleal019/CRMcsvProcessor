import pandas, os, csv

'''
Written on Python 3.7.3
using Pandas 0.25.1, Numpy 1.17.2 

Description: This script fixes issues with international codes in front of
values in the Phone 1.1 field from Infusionsoft. This script will also rename
any duplicate contacts it detects based on the value in the Phone 1.1 field

NOTE: Deleting whole columns is faster in Excel/Calc
'''
fileName = 'export.csv'

# creates CSV dataframe using pandas
data = pandas.read_csv(fileName, delimiter=',', encoding='utf-8', dtype=object)

# removes hello@gmail.com use from the Email column
data = data.replace(to_replace='hello@gmail.com', value='')

# removes leading 1's from phone numbers
data['Phone 1.1'] = data['Phone 1.1'].str.lstrip('+1')

# print(data[['Id', 'Name', 'Phone 1.1']])


def removeDupe():

    # loads CSV into file

    # --- See output of program without changes ---
    print('-------Data with duplicates -------')
    print(data[['Id', 'Name', 'Phone 1.1']])

    # In 'subset', write all the fields you want to deduplicate with
    # A new file will be created called 'unDuped-by-Phone.csv'
    # This is the file without duplicates
    # print('------- All Data without duplicates -------')
    # print(data.drop_duplicates(subset='Phone 1.1', keep='first'))
    # data.drop_duplicates(subset='Phone 1.1', keep='first').to_csv('unDuped-by-Phone.csv', index=False)

    # Change Name field value based on duplicate row values in Phone 1.1 field
    print('------- Renamed rows -------')
    # Must pass keep as 'last' since that is the value to be kept
    dup = data.duplicated(subset='Phone 1.1', keep='first')
    # create Duplicate column filled with True value
    data['Duplicate'] = True
    # Needed for some reason.
    data.duplicated(subset='Phone 1.1', keep='first')
    # Sets the newest (last) record to False if duplicate
    data.loc[data['Phone 1.1'].duplicated(keep='first'), 'Duplicate'] = False
    # Renames the records marked for deletion
    data.loc[data['Duplicate'] == False, 'First Name'] = 'MarkDelete360'
    nuData = data.drop('Duplicate', axis=1)

    nuData[['Id', 'Name', 'First Name', 'Last Name', 'Phone 1.1', 'Email']].to_csv('PhoneFixColumns.csv', index=False)

    # print('TESTING', data[['Id', 'First Name', 'Phone 1.1', 'Duplicate']])

    print(data[['Id', 'Name', 'Phone 1.1']])

    # Prints specific column values
    # print('------- Data with specific columns without duplicates -------')
    # print(data[['Id', 'Name', 'Phone 1.1']].drop_duplicates(subset='Phone 1.1', keep='first'))
    # data[['Id', 'Name', 'Phone 1.1']].drop_duplicates(subset='Phone 1.1', keep='first').to_csv('Specific-Columns.csv', index=False)

    # to_csv by itself just gets rid of quotations in empty columns
    # data.to_csv('unQuoted.csv', index=False)
    print('CSV generated.')

    # findDiff(fileName, 'test.csv')


def findDiff(ref, diff):
    print('---------------- Diff Data ---------------------------')

    data1 = pandas.read_csv(fileName, delimiter=',', encoding='utf-8', dtype=object)
    data2 = pandas.read_csv(diff, delimiter=',', encoding='utf-8', dtype=object)

    catData = pandas.concat([data1, data2], axis=1)

    print(catData.drop_duplicates(subset='Phone 1.1'))

    print(catData[['Name', 'Phone 1.1']])


removeDupe()
