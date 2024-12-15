Start

   Initialize database connection ("employeePayroll.db")
    Create table "employeePayroll" if it doesn't exist

   Define employee payroll data

  If table is empty, insert sample data

   Prompt user for:
        - Name (only letters and spaces)
        - Employee ID (valid ID between 1 and 16)
        - Number of dependents (non-negative integer)
        - Total hours worked (between 0 and 168)

  Find hourly rate using employee ID

   If ID is invalid, show error and exit

   Calculate:
        - Gross Pay (with overtime if hours > 40)
        - Dependent Reduction ($25 per dependent)
        - Pre-Tax Salary (gross pay - reduction)
        - State Tax (5.6% of pre-tax)
        - Federal Tax (7.9% of pre-tax)
        - Post-Tax Salary (pre-tax - taxes)

   Round values to two decimal places

   Create payroll table with:
        - Employee Name
        - Gross Pay
        - Dependent Reduction
        - State Tax
        - Federal Tax
        - Take Home Pay

   Display table using tabulate

  Close database connection

End

