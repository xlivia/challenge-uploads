-- List the employee number, last name, first name, sex, and salary of each employee.
SELECT employee_id, last_name, first_name, sex, salary
FROM employees;

-- List the first name, last name, and hire date for the employees who were hired in 1986.
SELECT first_name, last_name, hire_date
FROM employees
WHERE EXTRACT(YEAR FROM hire_date) = 1986;

-- List the manager of each department along with their department number, department name, employee number, last name, and first name.
SELECT d.dept_no, d.dept_name, m.employee_id, m.last_name, m.first_name
FROM departments d
JOIN employees m ON d.dept_manager = m.employee_id;

-- List the department number for each employee along with that employee’s employee number, last name, first name, and department name.
SELECT e.employee_id, e.last_name, e.first_name, d.dept_no, d.dept_name
FROM employees e
JOIN dept_emp de ON e.employee_id = de.employee_id
JOIN departments d ON de.dept_no = d.dept_no;

--List first name, last name, and sex of each employee whose first name is Hercules and whose last name begins with the letter B.
SELECT first_name, last_name, sex
FROM employees
WHERE first_name = 'Hercules' AND last_name LIKE 'B%';

-- List each employee in the Sales department, including their employee number, last name, and first name.
SELECT e.employee_id, e.last_name, e.first_name
FROM employees e
JOIN dept_emp de ON e.employee_id = de.employee_id
JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name = 'Sales';

-- List each employee in the Sales and Development departments, including their employee number, last name, first name, and department name.
SELECT e.employee_id, e.last_name, e.first_name, d.dept_name
FROM employees e
JOIN dept_emp de ON e.employee_id = de.employee_id
JOIN departments d ON de.dept_no = d.dept_no
WHERE d.dept_name IN ('Sales', 'Development');

-- List the frequency counts, in descending order, of all the employee last names (that is, how many employees share each last name).
SELECT last_name, COUNT(*) as frequency
FROM employees
GROUP BY last_name
ORDER BY frequency DESC;
