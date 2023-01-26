import csv
import os
from py_console import console


def dict_writter(key, content):
    filename = "writting_demo.csv"
    with open(filename, 'w') as file:
        csv_f = csv.DictWriter(file, fieldnames=key)
        csv_f.writeheader()
        csv_f.writerows(content)
    report(filename)


def report(filename):
    console.success(
        '\n\t\u2713 DONE\n\t\u2713 "{}" created succesfully'.format(filename))
    print("\t\u2713", os.path.getsize(filename), "kb")
    print("\t\u2713", os.path.abspath(filename), "\n")


fieldnames = ['user', 'id', 'BMI', 'suggesstion']
content = [
    {'user': 'Jeyaseelan', 'id': '235', 'BMI': '25',
        'suggesstion': 'Be careful with you diet'},
    {'user': 'Tamilkumaran', 'id': '233', 'BMI': '22',
        'suggesstion': 'Eat well'},
    {'user': 'Thanavanthan', 'id': '278', 'BMI': '24',
        'suggesstion': 'No worries'},
    {'user': 'Sandy', 'id': '765', 'BMI': '19',
        'suggesstion': 'Risky condition'}
]

dict_writter(fieldnames, content)
