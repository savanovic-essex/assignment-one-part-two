#Insert function serves to take user input and insert it into the database
def insert(connection, cursor):
    #User is asked to enter the contact's first and last name and their phone number
    first_name = raw_input("Enter First Name: ")
    last_name = raw_input("Enter Last Name: ")
    phone_number = raw_input("Enter Phone Number: ")

    #User gets a prompt about the insertion
    #If they enter anything other than "y", the function is going to repeat itself (recursion)
    if raw_input("Are you sure you want to insert this contact? (y/n) ") != ("y" or "Y"):
        insert(connection, cursor)
    else:
        #SQL query for inserting a new entry into the database
        #%s is used as a placeholder 
        query = "INSERT INTO contacts (first_name, last_name, phone_number) VALUES (%s, %s, %s)"
        #List of values enter by the user in the first part of the function
        values = (first_name, last_name, phone_number)
        #By utilizing the "cursor" module, execute the SQL query with the entered values
        cursor.execute(query, values)
        #The commit() method is used to confirm the changes made by the user to the database
        connection.commit()
        #Display a success message - inform the user about the new entry (row)
        print(cursor.rowcount, "Record inserted.")
