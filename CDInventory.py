#------------------------------------------#

# Title: Assignment06_Starter.py

# Desc: Working with classes and functions.

# Change Log: (Who, When, What)

# DBiesinger, 2030-Jan-01, Created File

# HongyiZhu, 2021-Nov-21, Added Contents into File

# HongyiZhu, 2021-Nov-26, Added Try-Except Constructs into File

#------------------------------------------#
# -- DATA -- #

strChoice = '' # User input
lstTbl = []  # list of lists to hold data
dicRow = {}  # list of data row
strFileName = 'CDInventory.txt'  # data storage file
objFile = None  # file object

# -- PROCESSING -- #

class DataProcessor:

    @staticmethod
    def add_item(ID, Title, Artist, table):
        """Function to add a new item into the existed table.

    Combines the user’s input including (1) ID (2) CD name (3) CD artist to a dict and then add it into the existed table

    Args:
         ID (string): an integer string of the user’s input;
         Title (string): a string of user’s input
         Artist (string): a string of user’s input
         table (list of dicts): a list of dicts (the dicts include 3 key(‘ID’,’Title’,’Artist’))
    Returns:
          table (new list of dicts): a list of dicts (the dicts include 3 key(‘ID’,’Title’,’Artist’)) which has been added the new item from the user’s input.
    """
        dic = {'ID': ID, 'Title': Title, 'Artist': Artist}
        table.append(dic)
        return table

    @staticmethod
    def delete_item(table,IDDel):
        """Function to delete the item whose ID is provided by user.

    Delete the corresponding item of the existed table.

        Args:
             table (list of dicts): a list of dicts which is the existed CDInventory 
             IDDel (int): an integer which corresponds to the ID that the item the user wants to delete
        Returns:
            table (list of dicts): a list of dicts whose corresponding item has been deleted.
        """

        intRowNr = -1
        blnCDRemoved = False
        for row in table:
            intRowNr += 1
            if row['ID'] == IDDel:
                del table[intRowNr]
                blnCDRemoved = True
                break

        if blnCDRemoved:
            print('The CD was removed')
        else:
            print('Could not find this CD!')
        return table

class FileProcessor:
    """Processing the data to and from text file"""

    @staticmethod
    def read_file(file_name, table):
        """Function to manage data ingestion from file to a list of dictionaries

        Reads the data from file identified by file_name into a 2D table
        (list of dicts) table one line in the file represents one dictionary row in table.
        
        If the file gets removed or does not exist at all, then the “FileNotFound” error will occur and the program will return to menu.
        
        In the first column of CDInventory.txt text file, if the ID number here is not an integer, Line 105 'ID': int(data[0]) will have the “ValueError”.
        “Try-except” construction can handle the error and print “invalid line, please modify the ID as integer”, then return to menu.

        Args:
            file_name (string): name of file used to read the data from
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime

        Returns:
            None.
        """
        table.clear()  # this clears existing data and allows to load data from file
        try:
            objFile = open(file_name, 'r')
        except:
            print('invalid filename')
            return
        for line in objFile:
            try:
                data = line.strip().split(',')
                dicRow = {'ID': int(data[0]), 'Title': data[1], 'Artist': data[2]}
                table.append(dicRow)
            except:
                print('invalid line, please modify the ID as integer')
                objFile.close()
                return
        objFile.close()
    @staticmethod
    def write_file(file_name, table):
        """Function to write the table to the file.

        Args:
             file_name (string): an string which is the file name that the user want to use for saving the data.
             table (list of dicts): a list of dicts which is the existed CDInventory 
        Returns:
             None.
        """

        objFile = open(file_name, 'w')

        for row in table:
            lstValues = list(row.values())
            lstValues[0] = str(lstValues[0])
            objFile.write(','.join(lstValues) + '\n')
        objFile.close()

class IO:
    """Handling Input / Output"""
    @staticmethod
    def print_menu():
        """Displays a menu of choices to the user

        Args:
            None.

        Returns:
            None.
        """
        print('Menu\n\n[l] load Inventory from file\n[a] Add CD\n[i] Display Current Inventory')
        print('[d] delete CD from Inventory\n[s] Save Inventory to file\n[x] exit\n')

    @staticmethod
    def menu_choice():
        """Gets user input for menu selection

        Args:
            None.

        Returns:
            choice (string): a lower case sting of the users input out of the choices l, a, i, d, s or x

        """
        choice = ' '
        while choice not in ['l', 'a', 'i', 'd', 's', 'x']:
            choice = input('Which operation would you like to perform? [l, a, i, d, s or x]: ').lower().strip()
        print()  # Add extra space for layout
        return choice

    @staticmethod
    def show_inventory(table):
        """Displays current inventory table


        Args:
            table (list of dict): 2D data structure (list of dicts) that holds the data during runtime.

        Returns:
            None.

        """
        print('======= The Current Inventory: =======')
        print('ID\tCD Title (by: Artist)\n')
        for row in table:
            print('{}\t{} (by:{})'.format(*row.values()))
        print('======================================')

    @staticmethod
    def ask_newID():
        """Function to ask user to input a new item.

          Receives the input from user including (1) ID (2) CD name (3) CD artist.
          
          If the user’s input is not an integer, then it is a “ValueError” and will print out “invalid input” and does not terminate the program.
          
          When an ID is to be deleted, if the input is not an integer, line 248 “intIDDel = int(strIDDel)” will occur the “ValueError”.
          “Try-except” block will handle the error, printing “your input is not an integer”.

        Args:
            None
        Returns:
            strID (string): an integer string of the user’s input;
            strTitle (string): a string of the user’s input;
            stArtist (string): a string of the user’s input.
        """

        while True:
            strID = input('Enter ID: ').strip()
            try:
                intID = int(strID)
                break
            except ValueError as e:
                print('invalid input')
                print(e)
        strTitle = input('What is the CD\'s title? ').strip()
        stArtist = input('What is the Artist\'s name? ').strip()
        return intID, strTitle, stArtist

FileProcessor.read_file(strFileName, lstTbl)

while True:
    IO.print_menu()
    strChoice = IO.menu_choice()

    if strChoice == 'x':
        break

    if strChoice == 'l':
        print('WARNING: If you continue, all unsaved data will be lost and the Inventory re-loaded from file.')
        strYesNo = input('type \'yes\' to continue and reload from file. otherwise reload will be canceled')
        if strYesNo.lower() == 'yes':
            print('reloading...')
            FileProcessor.read_file(strFileName, lstTbl)
            IO.show_inventory(lstTbl)
        else:
            input('canceling... Inventory data NOT reloaded. Press [ENTER] to continue to the menu.')
            IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    elif strChoice == 'a':
        strID, strTitle, stArtist = IO.ask_newID()
        lstTbl = DataProcessor.add_item(strID, strTitle, stArtist, lstTbl)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    elif strChoice == 'i':
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    elif strChoice == 'd':
        IO.show_inventory(lstTbl)
        while True:
            strIDDel = input('Which ID would you like to delete? ').strip()
            try:
                intIDDel = int(strIDDel)
                break
            except:
                print('your input is not an integer')
        lstTbl = DataProcessor.delete_item(lstTbl, intIDDel)
        IO.show_inventory(lstTbl)
        continue  # start loop back at top.

    elif strChoice == 's':
        IO.show_inventory(lstTbl)
        strYesNo = input('Save this inventory to file? [y/n] ').strip().lower()
        if strYesNo == 'y':
            FileProcessor.write_file(strFileName, lstTbl)
        else:
            input('The inventory was NOT saved to file. Press [ENTER] to return to the menu.')
        continue  # start loop back at top.

    else:
        print('General Error')