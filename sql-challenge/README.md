# Olivia's SQL Assignment
## UofT Data Analytics Bootcamp Module 9 Challenge

### Table of Contents
1. [Background](#background)
2. [Before You Begin](#before-you-begin)
3. [Instructions](#instructions)
4. [Data Modeling](#data-modeling)
5. [Data Engineering](#data-engineering)
6. [Run The Code](#run-the-code)

## Background
It’s been two weeks since you were hired as a new data engineer at Pewlett Hackard (a fictional company).
Your first major task is to do a research project about people whom the company employed during the 1980s and 1990s.
All that remains of the employee database from that period are six CSV files.

For this project, you’ll design the tables to hold the data from the CSV files, import the CSV files into a SQL database, and then answer questions about the data. That is, you’ll perform data modeling, data engineering, and data analysis, respectively.

## Before You Begin
1. Create a new repository for this project called sql-challenge. Do not add this assignment to an existing repository.
2. Clone the new repository to your computer.
3. Inside your local Git repository, create a directory for this Challenge. Use a folder name that corresponds to the Challenge, such as `EmployeeSQL`.

**Note:** You’ll add your files to this folder and push the changes to GitHub.

## Instructions
This Challenge is divided into three parts: data modeling, data engineering, and data analysis.

### Data Modeling
Inspect the CSV files, and then sketch an Entity Relationship Diagram of the tables. To create the sketch, feel free to use a tool like QuickDBDLinks to an external site..

### Data Engineering
Use the provided information to create a table schema for each of the six CSV files. Be sure to do the following:

Remember to specify the data types, primary keys, foreign keys, and other constraints.

For the primary keys, verify that the column is unique. Otherwise, create a composite keyLinks to an external site., which takes two primary keys to uniquely identify a row.

Be sure to create the tables in the correct order to handle the foreign keys.

Import each CSV file into its corresponding SQL table.

**HINT:** To avoid errors, import the data in the same order as the corresponding tables got created. And, remember to account for the headers when doing the imports.

### Data Analysis
1. List the employee number, last name, first name, sex, and salary of each employee.
2. List the first name, last name, and hire date for the employees who were hired in 1986.
3. List the manager of each department along with their department number, department name, employee number, last name, and first name.
4. List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
5. List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
6. List each employee in the Sales department, including their employee number, last name, and first name.
7. List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
8. List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).


## Run The Code

1.  To create a populate the tables:
    - `psql -U postgres -d employee -f schema.sql`

2. To connect to the database:
    - `psql -h localhost -U postgres -d employee`

3. Enter postgres password:

4. To view all tables in database:
    - `\dt`

5. To view tables contents:
    - `SELECT * FROM departments;`
    - `SELECT * FROM dept_emp;`
    - `SELECT * FROM dept_manager;`
    - `SELECT * FROM employees;`
    - `SELECT * FROM salaries;`
    - `SELECT * FROM titles;`



[Back To Top](#olivias-sql-assignment)
