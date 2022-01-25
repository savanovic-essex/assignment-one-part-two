from connection import connection, cursor
from insertContact import insert
from searchContact import search
from sortContact import sortContact
from deleteContact import delete


def main():
    #Starting point for the menu  
    choice = 0
    # This while loop will show the menu until the user enters 5 or a higher number
    while (choice <= 4):
        #Print menu options in console
        print("---------------------MENU-------------------------")
        print("1. INSERT")
        print("2. SEARCH")
        print("3. SORT & DISPLAY")
        print("4. DELETE")
        print("5. EXIT")
        print("---------------------MENU-------------------------")
        #User gets a prompt about their menu choice
        choice = int(raw_input("Enter Your choice:"))
        #Based on user's input in the "choice" variable, call the appropriate function
        if (choice == 1):
            insert(connection, cursor)
        if (choice == 2):
            search(cursor)
        if (choice == 3):
            display(cursor)
        if (choice == 4):
            delete(connection, cursor)


#Call the main function
main()