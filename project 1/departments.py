import os
import csv
from py_console import console


def generator(filename):
    departments = {}
    with open(filename) as file:
        employees = csv.DictReader(file)
        for employee in employees:
            department = employee["DEPARTMENT"]
            if department not in departments:
                departments[department] = 0
            departments[department] += 1
    return departments


def report_generator(departments):
    with open("output.txt", "w") as file:
        for department, count in departments.items():
            file.write("{:<10} = {}\n".format(department, count))
    print()
    console.success("\t\u2713 output file generated\n")


departments = generator('input/employees.csv')
report_generator(departments)
