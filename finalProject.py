import sqlite3
from tabulate import tabulate

dbname = "employeePayroll.db"

#define connection

connection = sqlite3.connect("employeePayroll.db")
cursor = connection.cursor()

#create table if one does not exist

command1 = """CREATE TABLE IF NOT EXISTS employeePayroll (
    employeeId INTEGER PRIMARY KEY,
    employeeHourlyRate REAL
    )"""

connection.execute(command1)

#initialize variables

employeeID, employeeDependents, dependentReduction = 0, 0, 0
employeeHourlyRate, grossPay, preTax, stateTax, federalTax, postTax, hoursOverForty, overtimeHours, employeeTotalHours = 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00
employeeName = ""

#insert data into table

employeePayroll = [
    (1, 36.00),
    (2, 30.00),
    (3, 26.50),
    (4, 38.00),
    (5, 45.70),
    (6, 22.00),
    (7, 29.00),
    (8, 25.50),
    (9, 38.00),
    (10, 45.70),
    (11, 22.00),
    (12, 29.00),
    (13, 26.50),
    (14, 38.00),
    (15, 40.50),
    (16, 24.00),
]

#check if the employee ID exists in the table

cursor.execute("SELECT COUNT(*) FROM employeePayroll")
if cursor.fetchone()[0] == 0:
    cursor.executemany("INSERT INTO employeePayroll VALUES (?, ?)", employeePayroll)
    connection.commit()

#gather the initial required information

while True:
    employeeName = input("Please enter your first and last name: ").strip()
    if employeeName and all(c.isalpha() or c.isspace() for c in employeeName): #is alpha checks to make sure the name contains only letters, is space allows spaces
        break
    print("Invalid input. Name can only contain letters and spaces and cannot be left empty.")

print("Valid employee IDs range from 1-16") ##let user know how many employee IDs exist

while True:
    try:
        employeeID = int(input("Please enter your employee ID: "))
        if 1 <= employeeID <= 16:
            break
        print("Invalid ID. Please enter a number between 1 and 16.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#query the table using the employee ID to get the employee's hourly rate

cursor.execute("SELECT employeeHourlyRate FROM employeePayroll WHERE employeeId = ?", (employeeID,))
result = cursor.fetchone()
if result: 
    employeeHourlyRate = result[0]
else:
    print("Employee ID does not exist")
    connection.close()
    exit()

#gather the additional required information

while True:
    try:
        employeeDependents = int(input("Please enter the number of your dependents: "))
        if employeeDependents >= 0:
            break
        print("Invalid input. Number of dependents cannot be negative.")
    except ValueError:
        print("Invalid input. Please enter a valid whole number.")

while True:
    try:
        employeeTotalHours = float(input("Please enter the total hours worked this week: "))
        if 0 < employeeTotalHours <= 168:  ## 168 is the max amount of hours in a week
            break
        print("Invalid input. Hours must be between 0 and 168.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")

#logic to calculate pay

if employeeTotalHours > 40:
    hoursOverForty = (employeeTotalHours - 40)
    overtimeHours = (hoursOverForty * 1.5)
    grossPay = (((employeeTotalHours - hoursOverForty) + overtimeHours) * employeeHourlyRate)
else:
    grossPay = employeeTotalHours * employeeHourlyRate
dependentReduction = employeeDependents * 25
preTax = grossPay - dependentReduction
stateTax = ((preTax * 1.056) - preTax) #where the state tax rate is 5.6%
federalTax = ((preTax * 1.079) - preTax) #where the federal tax rate is 7.9%
postTax = preTax - (stateTax + federalTax)

#make sure that the Final Payroll information is rouned to two decimal places

grossPay = round(grossPay, 2)
dependentReduction = round(dependentReduction, 2)
stateTax = round(stateTax, 2)
federalTax = round(federalTax, 2)
postTax = round(postTax, 2)

#create a table to display the results

payrollTable = [["Employee Name", employeeName],
         ["Gross Pay", "$" + str(grossPay)],
         ["Dependent Reduction", "$" + str(dependentReduction)],
         ["State Taxes", "$" + str(stateTax)],
         ["Federal Taxes", "$" + str(federalTax)],
         ["Take Home Pay", "$" + str(postTax)]]

#print the results

print(tabulate(payrollTable, headers="firstrow", tablefmt="fancy_grid"))

#close the connection

connection.close()
