#!/usr/bin/env python3
import csv

def csv_writter(content):
    with open("writtind_demo.csv", 'w') as file:
        csv_f = csv.writer(file)
        #csv_f.writerow([['a1', 'b2', 'c3']])
        csv_f.writerows(content)
    print("\u2713 OK")


content = [
    ['a1', 'b1', 'c1', 'd1'], 
    ['a2', 'b2', 'c2', 'd2'], 
    ['a3', 'b3', 'c3', 'd3']
]

csv_writter(content)