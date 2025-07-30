import csv

def read_employees():
    try:
        with open("../csv/employees.csv",'r') as employees_table:
            reader = csv.reader(employees_table)
            
            fullNames = [row[0]+" "+row[1] for row in reader[1:]]
            filteredFullNames = [name for name in fullNames if "e" in name]
            
            
    except Exception as e:
        return e 
    return [fullNames,filteredFullNames]
print(read_employees()[0])
print(read_employees()[1])
