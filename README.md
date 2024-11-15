**Overview**


This is a simple Employee Payroll Program developed in Python using SQLite done for a Computing Logic Group Project.
The program allows you to store employee data, calculate gross and net pay based on total hours worked, and apply dependent deductions and taxes.
The database stores the employee ID and hourly rate, and querys the users hourly rate after it is given the employee ID to complete the calculations.


**Features**

Stores employeeId and employeeHourlyRate in a database table

Creates a database table if one doesn't exist and inputs the data

Calculates gross pay, including any overtime pay for all hours worked above 40. (Any overtime is time and a half)

Calculates dependent reductions and applies the state and federal taxes.

Outputs all of the payroll information, including gross pay, taxes, and take-home pay.


**Setup**


Make sure Python 3 and the sqlite3 library are installed on your device.

Run the Python script (employeePayroll.py). The database employeePayroll.db will be created if it doesn't already exist.


**Example**

Please enter your first and last name: John Smith
Valid employee IDs range from 1-16
Please enter your employee ID: 5
Please enter the number of your dependents: 2
Please enter the total hours worked this week: 45

--- Payroll Information ---
Employee Name: John Smith
Gross Pay: $2050.75
Dependent Reduction: $50.00
State Taxes: $111.84
Federal Taxes: $157.01
Take Home Pay: $1731.90

This project was created for practice, anyone is welcome to use and modify as needed. 
