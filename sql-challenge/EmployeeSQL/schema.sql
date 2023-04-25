-- titles table
CREATE TABLE titles (
    title_id CHAR(10) PRIMARY KEY,
    title VARCHAR(100) NOT NULL
);

\copy titles FROM 'data/titles.csv' DELIMITER ',' CSV HEADER;

-- departments table
CREATE TABLE departments (
    dept_no CHAR(4) PRIMARY KEY,
    dept_name VARCHAR(100) NOT NULL
);

\copy departments FROM 'data/departments.csv' DELIMITER ',' CSV HEADER;

-- employees table
CREATE TABLE employees (
    emp_no INT PRIMARY KEY,
    emp_title_id CHAR(10) NOT NULL,
    birth_date DATE NOT NULL,
    first_name VARCHAR(50) NOT NULL,
    last_name VARCHAR(50) NOT NULL,
    sex CHAR(1) NOT NULL,
    hire_date DATE NOT NULL,
    FOREIGN KEY (emp_title_id) REFERENCES titles (title_id)
);

\copy employees FROM 'data/employees.csv' DELIMITER ',' CSV HEADER;

-- salaries table
CREATE TABLE salaries (
    emp_no INT,
    salary INT,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no)
);

\copy salaries FROM 'data/salaries.csv' DELIMITER ',' CSV HEADER;

-- dept_emp table
CREATE TABLE dept_emp (
    emp_no INT,
    dept_no CHAR(4),
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
);

\copy dept_emp FROM 'data/dept_emp.csv' DELIMITER ',' CSV HEADER;

-- dept_manager table
CREATE TABLE dept_manager (
    dept_no CHAR(4),
    emp_no INT,
    FOREIGN KEY (emp_no) REFERENCES employees (emp_no),
    FOREIGN KEY (dept_no) REFERENCES departments (dept_no)
);

\copy dept_manager FROM 'data/dept_manager.csv' DELIMITER ',' CSV HEADER;
