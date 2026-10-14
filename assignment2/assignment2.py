
import csv
import os
import traceback
import custom_module
from datetime import datetime

#Task 2
def read_employees():
    new_dict = {}
    row_list = []
    try:
        if os.path.exists('../csv/employees.csv'):
            with open('../csv/employees.csv', 'r') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i == 0:
                        new_dict['fields'] = row
                    else:
                        row_list.append(row)
                new_dict['rows'] = row_list
                return(new_dict)             
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
print(employees)

#Task 3
def column_index(input_str:str):
    try:
        return_value = employees["fields"].index(f"{input_str}")
        if return_value == -1:
            return("No value found, please try again.")
        else:
            return return_value
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
        
employee_id_column = (column_index("employee_id"))

#Task 4
def first_name(input_row_num:int):
    try:
        first_name_column = column_index("first_name")
        employee_name = employees["rows"][input_row_num][first_name_column]
        return(employee_name)  
    except Exception as e:
        return(f"{type(e).__name__} — {e}")

first_name_check = first_name(3)
print(first_name_check)

#Task 5
def employee_find(employee_id:int):
    try:
        def employee_match(row):
            return int(row[employee_id_column]) == employee_id
        matches=list(filter(employee_match, employees["rows"]))
        if matches != []:
            return (matches)
        else:
            print("No matches were found.")
            return []
    except Exception as e:
        return(f"{type(e).__name__} — {e}")
    
employee_find_check = employee_find(20)
print(employee_find_check)

#Task 6
def employee_find_2(employee_id:int):
    try:
        matches = list(filter(lambda row : int(row[employee_id_column]) == employee_id , employees["rows"]))
        return matches
    except Exception as e:
            return(f"{type(e).__name__} — {e}")
        
employee_check = employee_find_2(1)
print(employee_check)

#Task 7
def sort_by_last_name():
    last_name_column = column_index("last_name")
    sorted_rows = list(employees["rows"])
    sorted_rows.sort(key= lambda row: row[last_name_column])
    return sorted_rows

employees["rows"] = sort_by_last_name()
print(employees)

#Task 8
def employee_dict(user_row):
    new_dict = {}
    field_list = list(employees["fields"])
    for field in field_list:
        if field != "employee_id":
            new_dict[field] = user_row[column_index(field)]
    return new_dict

employee_dict_check = employee_dict(employees["rows"][2])
print(employee_dict_check)

#Task 9
def all_employees_dict():
    new_dict = {}
    employee_id_list = []
    for row in employees["rows"]:
        employee_id_list.append(row[column_index("employee_id")])
    for i, id in enumerate(employee_id_list):
        subset_row = employee_find_2(int(id))
        new_dict[id] = employee_dict(subset_row[0])
    return new_dict

all_employees_dict_data = all_employees_dict()
print(all_employees_dict_data)

#Task 10
def get_this_value():
    path_variable = os.environ.get('THISVALUE')
    return(path_variable)

print(get_this_value())

#Task 11
def set_that_secret(user_input:str):
    result = custom_module.set_secret(user_input)
    return(result)

new_secret = set_that_secret("Porsche")
print(custom_module.secret)

#Task 12
def read_minutes():
    minutes1 = {}
    minutes1_list = []
    minutes2 = {}
    minutes2_list = []
    try:
        if os.path.exists('../csv/minutes1.csv'):
             with open('../csv/minutes1.csv', 'r') as file:
                reader = csv.reader(file)
                for i, row in enumerate(reader):
                    if i == 0:
                        minutes1['fields'] = tuple(row)
                    else:
                        minutes1_list.append(tuple(row))
                minutes1['rows'] = minutes1_list
        if os.path.exists('../csv/minutes2.csv'):
                     with open('../csv/minutes2.csv', 'r') as file:
                        reader = csv.reader(file)
                        for i, row in enumerate(reader):
                            if i == 0:
                                minutes2['fields'] = tuple(row)
                            else:
                                minutes2_list.append(tuple(row))
                        minutes2['rows'] = minutes2_list
        return(minutes1, minutes2)                        
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

minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

#Task 13
def create_minutes_set():
    try:
        if minutes1 != {}:
            minutes_1_dict = minutes1
            minutes_2_dict = minutes2
            minutes_1_set = set(minutes_1_dict["rows"])
            minutes_2_set = set(minutes_2_dict["rows"])
            new_minutes_set = minutes_1_set.union(minutes_2_set)
            return(new_minutes_set)
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
    
minutes_set = create_minutes_set()
print(minutes_set)

#Task 14
def create_minutes_list():
    try:
        if minutes_set != {}:
            minutes_list = list(minutes_set)
            new_list = list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_list))
            return(new_list)
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

minutes_list = create_minutes_list()
print(minutes_list)

#Task 15
def write_sorted_list():
    try:
        if minutes_list != []:
            new_list = sorted(minutes_list, key=lambda x: x[1])
            new_list = list(map(lambda x: (x[0], datetime.strftime(x[1], "%B %d, %Y")), new_list))
            with open('./minutes.csv', 'w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(minutes1["fields"])
                for x, y in new_list:
                    writer.writerow([x, y])
        return(new_list)
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

sorted_list = write_sorted_list()
print(sorted_list)