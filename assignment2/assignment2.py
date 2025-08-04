import csv
import os
import custom_module
from datetime import datetime
def read_employees():
    data = {}
    rows = []
    try:
        with open("../csv/employees.csv",'r') as employees_table:
            reader = csv.reader(employees_table)
            count = 0
            for row in reader:
                if count == 0:
                    data["fields"] = data.get("fields", row)
                    count +=1
                else:
                    rows.append(row)
            data["rows"] = data.get("rows",rows)
            
    except Exception as e:
        return e 
    return data

employees = read_employees()

def column_index(employee_id):
    return employees["fields"].index(employee_id)
    
employee_id_column = column_index("employee_id")
def first_name(row_num):
    return employees["rows"][row_num][column_index("first_name")]

def employee_find(employee_id):
    def employee_match(row):
        return int(row[employee_id_column]) == employee_id

    matches=list(filter(employee_match, employees["rows"]))
    return matches

def employee_find_2(employee_id):
    matches = list(filter(lambda row: int(row[employee_id_column])==employee_id, employees["rows"]))
    return matches

def sort_by_last_name():
    employees["rows"].sort(key = lambda row: row[column_index("last_name")])
    return employees["rows"]
sort_by_last_name()
print(sort_by_last_name())

def employee_dict(row):
    return {
        key: value
        for key, value in zip(employees["fields"], row)
        if key != "employee_id"
    }
employee_dict(sort_by_last_name()[0][0])

def all_employees_dict():
    new_dict = {}
    for row in employees["rows"]:
        new_dict[row[column_index("employee_id")]] = employee_dict(row)
        
    return new_dict

def get_this_value():
    return os.getenv("THISVALUE")

def  set_that_secret(new_secret):
    custom_module.set_secret(new_secret)
    
set_that_secret("hello")
print(custom_module.secret)

def read_minutes():
    def read_to_dict(csv_to_read):
        data = {}
        rows = []
        try:
            with open(csv_to_read,'r') as csv_table:
                reader = csv.reader(csv_table)
                count = 0
                for row in reader:
                    if count == 0:
                        data["fields"] = data.get("fields", tuple(row))
                        count +=1
                    else:
                        rows.append(tuple(row))
                data["rows"] = data.get("rows",rows)
                
        except Exception as e:
            return e 
        return data
    minutes1 = read_to_dict("../csv/minutes1.csv")
    minutes2 = read_to_dict("../csv/minutes2.csv")
    return minutes1, minutes2
minutes1, minutes2 = read_minutes()
print(minutes1)
print(minutes2)

def create_minutes_set():
    minutes1Set = set(minutes1["rows"])
    minutes2Set = set(minutes2["rows"])
    united = minutes1Set.union(minutes2Set)
    return united

minutes_set = create_minutes_set()

def create_minutes_list():
    return list(map(lambda x: (x[0], datetime.strptime(x[1], "%B %d, %Y")), minutes_set))

minutes_list = create_minutes_list()
print(minutes_list)

def write_sorted_list():
    sorted_minutes = sorted(minutes_list, key=lambda x: x[1])
    new_converted =list(map(lambda x: (x[0],datetime.strftime(x[1], "%B %d, %Y")),sorted_minutes))
    try:
        with open("./minutes.csv",'w') as selected_csv:
            writer = csv.writer(selected_csv)
            writer.writerow(minutes1["fields"])
            for row in new_converted:
                writer.writerow(row)
    except Exception as e:
        return e 
    return new_converted
write_sorted_list()
print(write_sorted_list())