import re
import csv
from py_console import console


def email_domain_changer(user):
    regex = r"[\w.-]*(\.com)"
    result = re.sub(regex, r"gmail\1", user)
    return result


def file_writter(fieldnames, content):
    with open("output.csv", 'w') as file:
        csv_f = csv.DictWriter(file, fieldnames, lineterminator='\n')
        csv_f.writeheader()
        csv_f.writerows(content)
    console.success("output.csv generated succesfully \u2713")


def domain_updater(file_path):
    result = []
    with open(file_path) as file:
        rows = csv.DictReader(file)
        fieldnames = rows.fieldnames
        for row in rows:
            row['EMAIL'] = email_domain_changer(row['EMAIL'])
            result.append(row)
    file_writter(fieldnames, result)


domain_updater('input/employees.csv')
