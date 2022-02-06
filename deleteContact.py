#Delete function serves to take user input (contact ID) and based on it delete a contact
def delete(connection, cursor):
    #User is asked to enter the ID of the contact they want to delete
    id = raw_input("Enter contact's ID to delete: ")
    #If the user enters anything other than "y", the function is going to repeat itself (recursion)
    if raw_input("Are you sure you want to delete this contact? (Y/N) ") != ("y" or "Y"):
        delete(connection, cursor)
    else:
        #SQL query for deleting a contact from the database, based on the entered ID
        query = "DELETE FROM contacts WHERE id = " + id + ";"
        #By utilizing the "cursor" object, execute the SQL delete query with the entered ID
        cursor.execute(query)
        #The commit() method is used to confirm the changes made by the user to the database
        connection.commit()
        #Check if the deletion was successful and inform the user of the outcome
        if cursor.rowcount < 1:
            print("Nothing was deleted. Contact ID not found.")
        else:
            print(cursor.rowcount, "contact deleted.")    