CREATE TABLE departments(
   dept_no VARCHAR (50) PRIMARY KEY,
   dept_name VARCHAR (50) NOT NULL
);

CREATE TABLE dept_emp(
   emp_no SERIAL NOT NULL,
   dept_no VARCHAR (50) NOT NULL,
   from_date DATE NOT NULL,
   to_date DATE NOT NULL
);

CREATE TABLE dept_manager(
   dept_no VARCHAR (50) NOT NULL,
   emp_no SERIAL NOT NULL,
   from_date DATE NOT NULL,
   to_date DATE NOT NULL
);

CREATE TABLE employees(
   emp_no SERIAL PRIMARY KEY,
   birth_date DATE NOT NULL,
   first_name VARCHAR (50) NOT NULL,
   last_name VARCHAR (50) NOT NULL,
   gender VARCHAR (50) NOT NULL,
   hire_date DATE NOT NULL
);

CREATE TABLE salaries(
   emp_no SERIAL NOT NULL,
   salary SERIAL NOT NULL,
   from_date DATE NOT NULL,
   to_date DATE NOT NULL
);

CREATE TABLE titles(
   emp_no SERIAL NOT NULL,
   title VARCHAR (50) NOT NULL,
   from_date DATE NOT NULL,
   to_date DATE NOT NULL
);

select * from employees

-- 1. List the following details of each employee: 
--employee number,last name, first name, gender, and salary.
select employees.emp_no, last_name, first_name, gender, salaries.salary
from employees 
inner join salaries on employees.emp_no = salaries.emp_no;

-- 2. List employees who were hired in 1986.
select employees.last_name, first_name, hire_date
from employees
where hire_date between ('1986-01-01') and ('1986-12-31');

-- 3. List the manager of each department with the following information: 
-- department number, department name, the manager's employee number, 
-- last name, first name, and start and end employment dates.
select departments.dept_no, dept_name, dept_manager.emp_no, from_date, to_date, employees.last_name, first_name
from departments 
inner join dept_manager on departments.dept_no = dept_manager.dept_no
inner join employees on dept_manager.emp_no = employees.emp_no;

-- 4. List the department of each employee with the following information: 
-- employee number, last name, first name, and department name.
select departments.dept_name, dept_emp.emp_no, employees.last_name, first_name
from departments
inner join dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no

-- 5. List all employees whose first name is "Hercules" and last names begin with "B."
select employees.first_name, last_name
from employees
where first_name = 'Hercules'
and last_name like 'B%'

-- 6. List all employees in the Sales department, including their 
-- employee number, last name, first name, and department name.
select dept_emp.emp_no, employees.last_name, first_name, departments.dept_name
from departments
inner join dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no
where dept_name = 'Sales'

-- 7. List all employees in the Sales and Development departments, including their 
-- employee number, last name, first name, and department name.
select dept_emp.emp_no, employees.last_name, first_name, departments.dept_name
from departments
inner join dept_emp on departments.dept_no = dept_emp.dept_no
inner join employees on dept_emp.emp_no = employees.emp_no
where dept_name = 'Sales' 
or dept_name = 'Development'

-- 8. In descending order, list the frequency count of employee last names, 
-- i.e., how many employees share each last name.
select employees.last_name, count(last_name) 
from employees
group by last_name
having count(last_name) > 1

