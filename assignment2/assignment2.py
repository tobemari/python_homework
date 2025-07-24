import traceback
import csv
import os
import custom_module
from datetime import datetime

# Task 2

def read_employees():
    dict_data = {}
    list_rows = []
    try:
        with open('../csv/employees.csv', 'r') as file:
            reader = csv.reader(file)
            for i, row in enumerate(reader):
                if i == 0:
                    dict_data['fields'] = row
                else:
                    list_rows.append(row)
            dict_data['rows'] = list_rows
            
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

    return dict_data

employees = read_employees()
print(employees)


# Task 3

def column_index(index_to_search):  
    return employees['fields'].index(index_to_search)

employee_id_column = column_index('employee_id')


# Task 4

def first_name(row_number):
    first_name_index = column_index('first_name')
    row = employees['rows'][row_number]
    return row[first_name_index]


# Task 5

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id
    matches = list(filter(employee_match, employees['rows']))
    return matches


# Task 6

def employee_find_2(employee_id): 
    matches = list(filter(lambda row : 
        int(row[employee_id_column]) == employee_id , employees['rows'])) 
    return matches


# Task 7

def sort_by_last_name():
    employees['rows'].sort(key = lambda row: row[column_index('last_name')])
    return employees['rows']


# Task 8

def employee_dict(row):
    excluded_key = 'employee_id'
    new_dict = {key:value for key, value in zip(employees['fields'], row) if key != excluded_key}
    return new_dict


# Task 9

def all_employees_dict():
    result = {}
    for row in employees['rows']:
        employee_id = row[employee_id_column]
        result[employee_id] = employee_dict(row)
    return result
print(all_employees_dict())


# Task 10

def get_this_value():
    return os.getenv("THISVALUE")


# Task 11

def set_that_secret(new_secret):
    custom_module.set_secret(new_secret)

set_that_secret('wow')
print(custom_module.secret)

# Task 12

def read_minutes_file(filepath):
    result = {}
    rows = []
    with open(filepath) as file:
        reader = csv.reader(file)
        for i, row in enumerate(reader):
            if i == 0:
                result['fields'] = row
            else:
                rows.append(tuple(row))
        result['rows'] = rows
    return result

def read_minutes():
    minutes1 = read_minutes_file('../csv/minutes1.csv')
    minutes2 = read_minutes_file('../csv/minutes2.csv')
    return minutes1, minutes2

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)


# Task 13

def create_minutes_set():
    set1 = set(minutes1['rows'])
    set2 = set(minutes2['rows'])
    
    return set1 | set2

minutes_set = create_minutes_set()
print("-------------------------")

print("MINUTES SET:", minutes_set)

# Task 14
print("-------------------------")

def create_minutes_list():
    minutes_list = list(minutes_set)
    convert_to_tuple = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
    return convert_to_tuple

minutes_list = create_minutes_list()

print("MINUTES LIST:", minutes_list)


# Task 15

def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    converted = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), sorted_minutes))

    with open('../csv/minutes.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(minutes1['fields'])
        writer.writerows(converted)
    
    return converted

write_sorted_list()