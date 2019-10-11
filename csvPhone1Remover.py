import pandas, numpy, csv, tkinter, re

'''
Written on Python 3.7.3
using Pandas 0.25.1, Numpy 1.17.2 

-Fix last name issue

-Deleting whole columns is faster in Excel/Calc
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
    # data.drop_duplicates(subset='Phone 1.1', keep='first').to_csv('unDuped-by-Phone.csv')

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

    nuData[['Id', 'Name', 'First Name', 'Last Name', 'Phone 1.1', 'Email']].to_csv('PhoneFixColumns.csv')

    # print('TESTING', data[['Id', 'First Name', 'Phone 1.1', 'Duplicate']])

    print(data[['Id', 'Name', 'Phone 1.1']])

    # Prints specific column values
    # print('------- Data with specific columns without duplicates -------')
    # print(data[['Id', 'Name', 'Phone 1.1']].drop_duplicates(subset='Phone 1.1', keep='first'))
    # data[['Id', 'Name', 'Phone 1.1']].drop_duplicates(subset='Phone 1.1', keep='first').to_csv('Specific-Columns.csv')

    # to_csv by itself just gets rid of quotations in empty columns
    # data.to_csv('unQuoted.csv')
    print('CSV generated.')

    # findDiff(fileName, 'test.csv')


def nameFix():

    csvFile = open('RenamedColumns.csv', encoding='utf-8')
    colNames = ['Id', 'Name', 'First Name', 'Last Name', 'Phone 1.1', 'Email']

    try:
        with csvFile:
            csvReader = csv.reader(csvFile, delimiter=',')
            # fields = csvReader.next()
            # csvWriter = csv.writer('NamesFixed.csv', sep=',')

            # error may occur here if amount of columns is less than 6
            for row in csvReader:
                ID = row[1]
                Name = row[2]
                first_Name = row[3]
                last_Name = row[4]
                phone1 = row[5]
                email = row[6]

                # if Name contains more than 2 values and firstName contains more
                # than 1 and last_Name is blank
                if last_Name == '' and len(Name.split()) >= 2 and len(first_Name.split()) >= 1:
                    Bi = first_Name.split()
                    first_Name = Bi[0]
                    last_Name = Bi[1:]
                    Name = Bi
                    csv.writer

                    print(ID, ', Name ', *Name, ', fName', first_Name, ', lName',
                          *last_Name, ', phone', phone1, 'Email ', email)

    finally:
        csvFile.close()


def findDiff(ref, diff):
    print('---------------- Diff Data ---------------------------')

    data1 = pandas.read_csv(fileName, delimiter=',', encoding='utf-8', dtype=object)
    data2 = pandas.read_csv(diff, delimiter=',', encoding='utf-8', dtype=object)

    catData = pandas.concat([data1, data2], axis=1)

    print(catData.drop_duplicates(subset='Phone 1.1'))

    print(catData[['Name', 'Phone 1.1']])


# removeDupe()

nameFix()
