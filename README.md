# ForgePDF
This project was part of the 5th semester Computer Science and Engineering mini project of the subject 'Application Development Using Python'.

# Usage
Open the folder `Code` and run the `run.sh` file in command line or git bash and it will run the project.

# Dependencies

### Python
To install all the dependencies 
run the cmd and run the command - 
pip install -r requirements.txt

### Database
Steps to setup backend

* Install MySQL 8.0
* Create the Database with name forgepdf
* Create table with the following schema

1. Files table

| Field         | Type          | Null  | Key | Default | Extra          |
|:------------- |:------------- |:----- |:--- |:------- |:-------------- |
| file_id       | int           | NO    | PRI | NULL    | auto_increment |
| file_address  | varchar(200)  | NO    |     | NULL    |                |
| user_id       | int           | YES   | MUL | NULL    |                |

2.Users table

| Field         | Type          | Null  | Key | Default | Extra          |
|:------------- |:------------- |:----- |:--- |:------- |:-------------- |
| user_id       | int           | NO    | PRI | NULL    | auto_increment |
| name          | varchar(30)   | NO    |     | NULL    |                |
| email         | varchar(30)   | NO    |     | NULL    |                |
| password      | varchar(30)   | NO    |     | NULL    |                |
| phone         | decimal(10,0) | NO    |     | NULL    |                |



# Problem Statement
In a world where online is taking over and work from home is the new trend. PDF documents are becoming an essential part of our lives. May it be notes for your subjects, bills for your transactions or report for your assignments, PDF is the go to document format as it's portable and encryptable. But not all people find it easy to work with PDFs for tasks such as merging, splitting, encrypting, decrypting, extracting etc.

We at ForgePDF realize this need and founded ForgePDF to tackle these issues and make interacting with PDF much more simple.

# Technologies Used In This Application
1. Python: Used for the main logic and functionality.
2. Tkinter: Used for UI.
3. MySQL: Used for the database.
4. BeautifulSoup: Used for Web Scraping.
5. Selenium: Used for automation.
6. PyPDF2: Used for PDF functions.
7. Flask: Used for developing custom APIs.
8. Requests: Used for calling 3rd party APIs.
9. JSON: Used for JSON file management.
10. CSV: Used for CSV functions.
11. Regular Expression: For input Validation.
12. Shutil: Used for file management.
13. OS: Used for getting the absolute path of a file.


