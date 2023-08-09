REQUIREMENT:

Build out a service in the language/framework of your choice that will integrate between Asana 
and Airtable. The requirement here is that whenever a new task is created on Asana then we 
need to copy that task over to Airtable. The task created in Asana needs be stored as a new row 
in an Airtable table called “Asana Tasks” and it needs to have the following columns:
1. TaskID
2. Name
3. Assignee
4. Due Date
5. Description
----------------------------------------------------------------------------------------------------


Problem Statement:  
	Integration between Asana and Airtable. Whenever a new task is created on Asana then it should be copied to the airtable. The task created in Asana needs be stored as a new row in an Airtable table called “Asana Tasks”. 

Operations involved:

1. Creating Base
2. Creating Table
3. Generating API, Base ID, URL
4. Copying
5. Storing

Explaination for the code:

	The code is periodically fetches tasks from an Asana project using the Asana API, checks if these tasks have been processed before (by comparing their IDs with a list stored in a file), and then creates records in an Airtable table to store information about the tasks.

Importing the necessary modules:
	It imports several modules required for interacting with different APIs and performing file operations.

There are two utility functions are defined: 
	write_list_to_file and read_list_from_file. These functions are used to write and read lists from a file.

Defines a function to create a file if it doesn't exist: 
	The create_file_if_not_exists function checks if a file exists and creates it if it doesn't.

Initializes an API connection: 
	It creates an instance of the Api class from the pyairtable library, which is used to interact with an Airtable database.

Starts a loop: The code enters an infinite loop.

Delays execution: 
	It waits for 10 seconds before proceeding to the next iteration.

Makes a request to the Asana API:
	 It sends an HTTP GET request to the Asana API to retrieve tasks.

Reads and writes to a file: 
	The code reads task IDs from a file called 'my_list.txt', compares them with the retrieved tasks, and writes new task IDs back to the file.

Creates records in an Airtable table: 
	For each task retrieved from the Asana API, it extracts relevant information (such as ID, name, assignee, due date, and description) and creates records in an Airtable table using the table. create method.

Catches exceptions: 
	If an exception (such as an ApiException) occurs during the process, it is caught and an error message is printed.

