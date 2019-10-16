## MUST HAVE PYTHON 3 INSTALLED
## FILE TO BE USED MUST BE NAMED 'export.csv'
## PYTHON SCRIPT AND 'export.csv' MUST BE IN THE SAME DIRECTORY
## PHONE 1.1 FIELD IN THE PROGRAM MUST CORRESPOND TO THE SECOND PHONE 1 FIELD IN INFUSIONSOFT. (THE FIELD WITHOUT THE PHONE TYPE AT THE END)


csvPhone1FixAndDuplicatedRemoval.py: Will remove U.S. International codes from Phone 1.1 fields and will mark duplicates as "MarkDelete360 in the First Name field.

NameFix.py: Will move names to their correct fields. Fixes if First Name fields has both first name and last name.

----------------------------------------------------------------------------

How to use

-Open command prompt (Terminal in Linux/OSX/MAC).

-Change the directory to be the directory of wherever the python script
 and 'export.csv' file are. (type cd followed by the directory. 
 ex. 'cd Desktop\Python Script\' in Windows, 'cd Desktop/Python Script/' in Linux/OSX/Mac

-To execute it type python followed by the name of the script you want to use.

-To delete/merge duplicates do a search for Name "MarkDelete360" in Infusionsoft

Ex. python NameFix.py

You may need to write as python3 NameFix.py if it's not working.