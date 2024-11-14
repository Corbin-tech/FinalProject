import sqlite3
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
employeeHourlyRate, grossPay, preTax, stateTax, federalTax, postTax, hoursOverForty, overtimeHours, employeeTotalHours = 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0
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

#gather the required information

employeeName = str(input("Please enter your first and last name: "))
print("Valid employee IDs range from 1-16")
employeeID = int(input("Please enter your employee ID: "))

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

employeeDependents = int(input("Please enter the number of your dependents: "))
employeeTotalHours = float(input("Please enter the total hours worked this week: "))

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

#print the results

print("Employee Name:", employeeName)
print("Gross Pay: $", grossPay)
print("Dependent Reduction: $", dependentReduction)
print("State Taxes: $", stateTax)
print("Federal Taxes: $", federalTax)
print("Take Home Pay: $", postTax)

#close the connection

connection.close()