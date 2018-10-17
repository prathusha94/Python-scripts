import xlrd
import os

def createFolder(name):
    try:
        if not os.path.exists(name):
            os.makedirs(name)
    except OSError:
        print("Error creating folder " + name)

if __name__ == "__main__":
    loc = ("FILE_LOCATION")
    ##Open and read the excel file
    file = xlrd.open_workbook(loc)

    ##Get the first worksheet
    sheet = file.sheet_by_index(0)
    no_of_rows = sheet.nrows
    ##Extract each of the student names and create a folder for everyone
    for i in range(2,no_of_rows):
        name = sheet.cell_value(i,0)
        createFolder(name)
