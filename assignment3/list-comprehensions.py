import os
import csv
import traceback

def read_employees():
    new_dict = {}
    row_list = []
    try:
        if os.path.exists('../csv/employees.csv'):
            with open('../csv/employees.csv', 'r') as file:
                reader = csv.reader(file)
                next(reader, None)
                full_name_list = [x[1] + " " + x[2] for x in reader]
                print(full_name_list)
                only_e_list = [x for x in full_name_list if any(vowel in x for vowel in 'e')]
                print(only_e_list)
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

read_employees()         