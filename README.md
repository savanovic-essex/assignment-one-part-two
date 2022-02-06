# Phonebook Console Application


## Introduction and objective

Phonebook is a simple application, executed in a console/terminal, which allows users to **insert**, **search**, **sort(display)** and **delete** contacts.
The objective of this application is to help users with their everyday actions, such as finding contact information.
In order to execute this application, some technical requirements need to be fulfilled: Python and MySQL need to be installed on the machine. Afterwards, the database and its table need to be created with the following commands in this order:
 1. Open the MySQL CLI with the `mysql` command in terminal
 2. Create the database with the following command:
> `CREATE DATABASE IF NOT EXISTS phonebook DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
USE phonebook;`

 3. Create the table with the following command:
> `CREATE TABLE contacts (`
`  id int(11) NOT NULL,`
`  first_name varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,`
`  last_name varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL,`
`  phone_number varchar(50) COLLATE utf8_unicode_ci DEFAULT NULL`
`) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_unicode_ci;`
 
 4. Add primary key to the `id` column with the following command:
> `ALTER TABLE contacts ADD PRIMARY KEY (id);`

 5. Alter the `id` column to automatically increment with new entries
> `ALTER TABLE contacts MODIFY id int(11) NOT NULL AUTO_INCREMENT;`

Once the technical requirements have been fulfilled, the application can be executed in the terminal with the following command:
> `python main.py`

## Design of data structure and algorithms

For the purpose of achieving the desired functionality, certain data structures and algorithms had to be defined. Starting with the database, I decided to keep everything simple and use the most basic form of the MySQL database. I created one database, called `phonebook`, which consists of one table, called `contacts`.
The table `contacts` is the core of this application, because it stores all the data that make this application meaningful. After some consideration, I decided to only create the fields, which can serve this MVP. By looking at the table structure below, one can see that it has 4 fields: `id`, `first_name`, `last_name` and `phone_number`. The first field (id) is of type `int` (integer) and it can not be null. It does not have a default value, but it automatically increments itself with each new entry, starting with 1. This field is also the primary key for the table `contacts`. When a user creates a new entry, they have no control over it.
The three other fields are all of the same type, `varchar` and have the same length of 50. They can call be null and that is their default value. I chose this type in order to not limit users to certain characters. Their data can vary, and this type will accept anything a user enters. 

#### Table structure
| # | Name         | Type        | NULL | Default | Extra          |
|:-:|--------------|-------------|------|---------|----------------|
| 1 | id           | int(11)     | No   | None    | AUTO_INCREMENT |
| 2 | first_name   | varchar(50) | Yes  | NULL    |                |
| 3 | last_name    | varchar(50) | Yes  | NULL    |                |
| 4 | phone_number | varchar(50) | Yes  | NULL    |                |


#### Functions
The Phonebook app has 5 functions. They are named and described in the table below. Alongside the descriptions, you can also see the algorithms used for them, presented in the form of a flowchart.
| # | Function       | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Flowchart                                       |
|:-:|----------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-------------------------------------------------|
| 1 | Main           | When a user starts the app, the first thing they see is the main function, which asks them to select one of the five possible options. Once they have entered their desired option, they will either be redirected to that function or the app will shut down if the user selects the fifth and final option.                                                                                                                                                                                                                                                                                      | <img src="https://i.ibb.co/w0M1b3D/Main.png">   |
| 2 | Insert         | This function serves to insert data(contacts) into the database. It starts by taking user input for the first and last name and the phone number. Afterwards, the user gets a prompt about their decision to insert this contact into the database. If they press `y` this app will save the contact into the database, otherwise it will keep restarting itself. With this action, we can see an example of recursion, where a function keeps calling itself until the requirement has been fulfilled.                                                                                            | <img src="https://i.ibb.co/myHskfW/Insert.png" height=400> |
| 3 | Search         | The search function starts by taking user input for the contact's first name. The user then gets a prompt about their action. If they choose to continue, by entering `y`the app will fetch the data from the database. By utilizing the `LIKE` operator in the SQL syntax, the user only has to enter one part of the name and Phonebook app will return all contacts that match the entered string. Once the data has been fetched from the database, the app will check if there are any matches and display them. In case that there are no results, the user will receive a message about it. | <img src="https://i.ibb.co/1005Bv5/Search.png"> |
| 4 | Sort / Display | This function displays all data from the contacts table. The user is prompted with a question about the sorting order of the contacts. They can decide for the data to be ordered either by the first name or the last name, by entering 1 or 2 respectively. If they enter anything else, the data will be ordered by the phone number. When the app fetches the information from the database, it checks whether there are any results and displays them. In case that there are no results, the user will receive a message about it.                                                           |  <img src="https://i.ibb.co/PMHQRt7/Sort.png">  |
| 5 | Delete         | The purpose of the delete function is to remove entries from the database. It starts by asking the user for the contact's ID, they want to remove. In the next step, the user gets a prompt about their decision. If they choose to continue, the app will send a deletion request to the database. Otherwise, the process will repeat itself. Once the app has received the answer from the database, it checks whether the deletion was successful and informs the user of the either possible outcome.                                                                                          | <img src="https://i.ibb.co/L54QK3X/Delete.png"> |

