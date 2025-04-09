import pandas as pd

# Task 1

# Create initial dictionary with employee data
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],
    'Age': [25, 30, 35],
    'City': ['New York', 'Los Angeles', 'Chicago'],
}

# Convert dictionary into a DataFrame using Pandas
task1_data_frame = pd.DataFrame(data)
print(task1_data_frame)

# Add a column Salary to a copy of the original DataFrame
task1_with_salary = task1_data_frame.copy()
task1_with_salary['Salary'] = [70000, 80000, 90000]
print(task1_with_salary)

# Create another copy and increment a column Age by 1
task1_older = task1_with_salary.copy()
task1_older['Age'] += 1
print(task1_older)

# Save task1_older DataFrame to a CSV file and check its content
task1_older.to_csv('employees.csv', index=False)
task1_older_check = pd.read_csv('employees.csv')
print(task1_older_check.head())

# Task 2

# Load CSV file into a new DataFrame
task2_employees = pd.read_csv('employees.csv')
print(task2_employees.head())

# Create a dictionary with 2 new employees 
new_employees = {
    'Name': ['Eve', 'Frank'],
    'Age': [28, 40],
    'City': ['Miami', 'Seattle'],
    'Salary': [60000, 95000]
}

# Create a JSON file, add new employees into it 
pd.DataFrame(new_employees).to_json('additional_employees.json')

# Create new DataFrame and load the data from JSON file into that
json_employees = pd.read_json('additional_employees.json')
print(json_employees)

# Combine 2 DataFrames from the JSON file and CSV file
more_employees = pd.concat([task2_employees, json_employees], ignore_index=True)
print(more_employees)

# Task 3

# Assign the first 3 rows to the variable
first_three = more_employees.head(3)
print(first_three)

# Assign the last 2 rows to the variable
last_two = more_employees.tail(2)
print(last_two)

# Assign the shape of the DataFrame to the variable
employee_shape = more_employees.shape
print(employee_shape)

# Print a summary of the DataFrame
print(more_employees.info())

# Task 4

# Create a DataFrame from the CSV file
dirty_data = pd.read_csv('dirty_data.csv')

# Remove any duplicate rows from the DataFrame
clean_data = dirty_data.copy().drop_duplicates()
print(clean_data)

# Convert Age to numeric and handle missing values
clean_data['Age'] = pd.to_numeric(clean_data['Age'], errors="coerce")

# Fill missing numeric values with the mean
clean_data['Age'] = clean_data['Age'].fillna(clean_data['Age'].mean())
print(clean_data)

# Convert Salary to numeric
clean_data['Salary'] = pd.to_numeric(clean_data['Salary'], errors="coerce")

#  Replace unknown, n/a with NaN and fill missing numeric values with the median
clean_data['Salary'] = clean_data['Salary'].replace(["unknown", "n/a"], pd.NA).fillna(clean_data['Salary'].median())
print(clean_data)

# Convert Hire Date column values to datetime
clean_data['Hire Date'] = pd.to_datetime(clean_data['Hire Date'], errors="coerce")
print(clean_data)

# Strip extra whitespace and standardize Name and Department as uppercase
clean_data["Name"] = clean_data["Name"].str.strip().str.upper()
clean_data["Department"] = clean_data["Department"].str.strip().str.upper()
print(clean_data)