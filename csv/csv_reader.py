#!/usr/bin/env python3
import csv
import os

def csv_reader (filename):
  # print(os.path.isfile(filename))
  with open(filename, 'r') as file:
    excel = csv.reader(file)
    for row in excel:
      name, age, status = row
      print("{:<15} | {} | {}".format(name, age, status))

csv_reader("reading_demo.txt")
