#Search function serves to take user input and return appropriate data from the database
def search(cursor):
    #User is asked to enter the contact's first, i.e. the search keyword
    first_name = raw_input("Enter First Name: ")
    
    #User gets a prompt to confirm their action
    #If they enter anything other than "y", the function is going to repeat itself (recursion)
    if raw_input("Are you sure you want to search for this contact? (Y/N) ") != ("y" or "Y"):
        search(cursor)
    else:
        #Execute SQL statement
        """
        By utilizing the LIKE operator in the SQL statement, the user has to enter only one part of the first name
        and the Phonebook app will return all contacts that match the entered string.
        """
        cursor.execute("SELECT * FROM contacts WHERE first_name LIKE '%" + first_name + "%'")
        #Variable "result" stores all records fetched from the database
        result = cursor.fetchall()

        #Check if the database has returned any (viable) results
        #If there are viable results, print them, otherwise inform the user that there are no results
        if len(result) > 0:
            #Print the results header to make it easier to read in the terminal
            print("--------------------------------------------------")
            print("ID   First Name    Last Name     Phone Number")
            print("--------------------------------------------------")
            #Loop through results and print each one
            for x in result:
                print(str(x[0]) + " | " + x[1] + " | " + x[2] + " | " + x[3])
            print("--------------------------------------------------")
        else:
            print("--------------------------------------------------")
            print("No results found for that keyword.")
            print("--------------------------------------------------")
