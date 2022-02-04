#Sort function serves to display contacts and sort/order them based on the user's input
def sort(cursor):
    #User is asked to choose how they want to order the contacts
    print("Choose how you want to order the results.")
    orderChoice = int(raw_input("Press 1 for first name and 2 for last name: "))
    
    #Variable "order" has the default value "phone_number" and it is changed based on the user's input
    #It also serves as a fallback, in case the user selects some other number
    order = "phone_number"
    if (orderChoice == 1):
        order = "first_name"
    elif (orderChoice == 2):
        order = "last_name"
    else:
        order = "phone_number"

    #Execute SQL statement containing the "ORDER BY" keyword with the argument "order" based on the user's input
    cursor.execute("SELECT * FROM contacts ORDER BY " + order + ";")
    #Variable "result" stores all records fetched from the database with fetchall() function
    result = cursor.fetchall()

    #Check if the database has returned any results
    #If there are viable results, print them, otherwise inform the user that there are no results
    if len(result) > 0:
        #Print the results header to make it easier to read in the terminal
        print("--------------------------------------------------")
        print("ID | First Name | Last Name | Phone Number")
        print("--------------------------------------------------")
        #Loop through results and print each one
        for x in result:
            print(str(x[0]) + " | " + x[1] + " | " + x[2] + " | " + x[3])
        print("--------------------------------------------------")
    else:
        print("--------------------------------------------------")
        print("No contacts found in the database.")
        print("--------------------------------------------------")    