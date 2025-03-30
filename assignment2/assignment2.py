# Task 2

import csv
import traceback
import os
import custom_module
from datetime import datetime

def read_employees ():
    dict = {}
    rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            headers = next(reader)
            
            dict['fields'] = headers
            for row in reader:
                rows.append(row) 

            dict['rows'] = rows
            return dict

    except Exception as e:
        trace_back = traceback.extract_tb(e.__traceback__)
        stack_trace = list()
        for trace in trace_back:
            stack_trace.append(f'File : {trace[0]} , Line : {trace[1]}, Func.Name : {trace[2]}, Message : {trace[3]}')
        print(f"Exception type: {type(e).__name__}")
        message = str(e)
        if message:
            print(f"Exception message: {message}")
        print(f"Stack trace: {stack_trace}")

employees = read_employees()

# Task 3

def column_index(column_name):
    return employees["fields"].index(column_name)

employee_id_column = column_index("employee_id")

# Task 4

def first_name(row_number):
    index = column_index("first_name")
    return employees["rows"][row_number][index]

# Task 5

def employee_find (employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches=list(filter(employee_match, employees["rows"]))
    return matches

# Task 6

def employee_find_2(employee_id):
    matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
    return matches

# Task 7

def sort_by_last_name():
    index = column_index('last_name')
    employees['rows'].sort(key = lambda row: row[index])
    return employees['rows']


# Task 8

def employee_dict(row):
    employee = {}
    for key, value in zip(employees["fields"], row):
        if key != "employee_id":
            employee[key] = value
    return employee

# Task 9

def all_employees_dict():
    all_employees = {}
    for row in employees["rows"]:
        employee_id = row[0]
        all_employees[employee_id] = employee_dict(row)
    return all_employees


# Task 10

def get_this_value():
    return os.getenv("THISVALUE")

# Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret("banana!")
print("Secret is:", custom_module.secret)

# Task 12

def read_csv_as_dict(path):
    with open(path, 'r') as file:
        reader = csv.reader(file)
        headers = next(reader)
        rows = [tuple(row) for row in reader]  
    return {"fields": headers, "rows": rows}

def read_minutes():
    minutes1 = read_csv_as_dict("../csv/minutes1.csv")
    minutes2 = read_csv_as_dict("../csv/minutes2.csv")
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print("Minutes 1:", minutes1)
print("Minutes 2:", minutes2)

# Task 13

def create_minutes_set():
    set1 = set(minutes1["rows"])
    set2 = set(minutes2["rows"])
    combined = set1.union(set2)
    return combined

minutes_set = create_minutes_set()
print("Combined minutes set:", minutes_set)

# Task 14

def create_minutes_list():
    minutes_list = list(minutes_set)
    converted = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return converted

minutes_list = create_minutes_list()
print("Minutes list with datetime:", minutes_list)

# Task 15

def write_sorted_list():
    sorted_list = sorted(minutes_list, key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], x[1].strftime("%B %d, %Y")), sorted_list))
    with open("minutes.csv", "w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(minutes1["fields"])
        writer.writerows(converted)
    return converted

final_minutes = write_sorted_list()
print("Final minutes written to file:", final_minutes)

