import csv


def nameFix():
    fileName = 'enamedColumns.csv'

    try:
        # open file to read and write
        with open(fileName, 'r', encoding='utf-8') as csvFile:
            csvReader = csv.DictReader(csvFile, delimiter=',')
            # opens and creates file to write to.
            csvWriter = csv.DictWriter(open('FixedNames.csv', 'w+', newline=''), fieldnames=["Id", "Name", "First Name", "Last Name", "Phone 1.1", "Email"])
            csvWriter.writeheader()
            nuLines = {}

            # error may occur here if amount of columns is less than 6
            # reading file loop
            for row in csvReader:
                Id = row['Id']
                Name = row['Name']
                first_Name = row['First Name']
                last_Name = row['Last Name']
                phone1 = row['Phone 1.1']
                email = row['Email']
                # print(Id, ', Name ', Name, ', fName', first_Name, ', lName', last_Name, ', phone', phone1, 'Email ', email)

                # if last_Name is blank, Name contains more than 2 values, and firstName contains more
                # than 1
                if last_Name == '' and len(Name.split()) >= 2 and len(first_Name.split()) > 1:
                    # print("LENGTH", len(Name.split()))
                    Bi = first_Name.split()
                    first_Name = Bi[0]
                    last_Name = Bi[1:]
                    # join needed so that last_Name list is converted to string
                    last_Name = ''.join(last_Name)

                    Name = first_Name, last_Name
                    Name = ' '.join(Name)
                    # nuLines = [Id, Name, first_Name, last_Name, phone1, email]
                    nuLines.update({'Id': Id, 'Name': Name, 'First Name': first_Name, 'Last Name': last_Name, 'Phone 1.1': phone1, 'Email': email})
                    print(nuLines)
                    # print(Id, ', Name ', *Name, ', fName', first_Name, ', lName', *last_Name, ', phone', phone1, 'Email ', email)

                    csvWriter.writerow(nuLines)

                # elif last_Name is in first_Name
                elif last_Name in first_Name:
                    # creates list
                    # removes last name from first_Name array and reassigns to first_Name
                    fName = first_Name.split()
                    fName.remove(last_Name)
                    first_Name = fName

                    first_Name = ''.join(first_Name)

                    Name = first_Name
                    nuLines.update({'Id': Id, 'Name': Name, 'First Name': first_Name, 'Last Name': last_Name, 'Phone 1.1': phone1, 'Email': email})
                    print(nuLines)

                    csvWriter.writerow(nuLines)

                # prints everything else to csv (can probably be left commented out
                # else:
                #     nuLines.update({'Id': Id, 'Name': Name, 'First Name': first_Name, 'Last Name': last_Name, 'Phone 1.1': phone1, 'Email': email})
                #     csvWriter.writerow(nuLines)

    finally:
        csvFile.close()


# boolean function that returns True if list1 contains something in list2
def bool_List(list1, list2):
    boo = False
    for it2 in list2:
        for it1 in list1:
            if it1 == it2:
                return True


nameFix()
