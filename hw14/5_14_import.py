# !/usr/bin/env python3
# import using pickle
import pickle

class Employee:
    def init(self, name, id, department, title):
        self.employee_name = name
        self.employee_id = id
        self.employee_department = department
        self.employee_title = title

file_to_import = open("first_employee.pickle",'rb')
first_employee = pickle.load(file_to_import)
file_to_import.close()
print(first_employee.employee_name, first_employee.employee_id, first_employee.employee_department, first_employee.employee_title, sep="\n")