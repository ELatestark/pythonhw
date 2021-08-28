# !/usr/bin/env python3
# export using pickle

import pickle

class Employee:
    def __init__(self, name, id, department, title):
        self.employee_name = name
        self.employee_id = id
        self.employee_department = department
        self.employee_title = title

first_employee = Employee("Mary Flint", "1337", "IT Department", "DevOps Engineer")

file_to_export = open("first_employee.pickle", "wb")
pickle.dump(first_employee, file_to_export)
file_to_export.close()