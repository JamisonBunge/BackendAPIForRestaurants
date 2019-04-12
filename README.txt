
Running instructions



I have implemented this using Restful Flask with python3 and sqlite3. In order to run the program please have the following python3 library's installed.

https://pypi.org/project/Flask/
https://pypi.org/project/Flask-RESTful/#files.

I have opted to not include a front end to this project at the recommendation of Sharebite. Instead, I have used the program "Postman" as the http client to send requests from. I recommend using this software, however, any http client should work as long as the appropriate header files are sent with the request. 

To run the server, simply type "python3 MenuAPI.py" in a bash terminal. If done correctly, the program should echo back the local address it is running on. I've found that http://127.0.0.1:5000/ is always used, at least for my enviorment. 


Functionality



I've created two routes for the menu section API. One that specifies an ID and one that does not. I have implemented the five tasks across these two route. 


Route 1: 127.0.0.1:5000/menusection/<int:id>
	
	Task 1)	Get a menu section by id
	Task 4)	Edit a menu section
	Task 5)	Delete a menu section


Route 2: 127.0.0.1:5000/menusection/

	Task 2)	Get all menu sections
	Task 3)	Add a new menu section

Usage

In this section I will provide sample request with their JSON to correctly use the API. Note*: I am providing these as they would be formatted in Postman. Using a different HTTP client may require you to put the host on it's dedicated header line.


Task 1)	Get a menu section by id

	GET 127.0.0.1:5000/menusection/3

	"Fails" response when: An invalid ID is requested 


Task 2)	Get all menu sections

	GET 127.0.0.1:5000/menusection


Task 3)	Add a new menu section

	PUT 127.0.0.1:5000/menusection
	
	{
		"name" : "Drinks"
	}


	"Fails" response when: request JSON is not of the above format

Task 4)	Edit a menu section (Specifically, edit the menu section name in the DB)


	PUT 127.0.0.1:5000/menusection/4
	
	{
		"name" : "Sugar Free Drinks"
	}
	
	
	"Fails" response when: An invalid ID is requested and when request JSON is not of the above format

Task 5)	Delete a menu section

	DELETE 127.0.0.1:5000/menusection/3

	"Fails" response when: An invalid ID is requested (That being the file was already deleted or the ID is wrong)




