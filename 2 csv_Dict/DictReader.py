#!/usr/bin/env python3

import csv


def dict_reader(filename):
    with open(filename) as file:
        csv_f = csv.DictReader(file)
        for user in csv_f:
            print("{:<8}|{:5}|{}".format(user["name"],
                  user["likes"], user["comments"]))


dict_reader("reading_demo.csv")
