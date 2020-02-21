#! /usr/bin/python3

import csv

QandA_dict = {}
questions_completed_dict = {}

with open("QandA.csv", mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        QandA_dict.update( {row[0]:row[1]} )

print("press x to show answer." + "\n")
for subject in QandA_dict:
    print(subject)
    user_choice = ""
    while user_choice != "x":
        user_choice = input().lower()
        if user_choice == 'x':
            print(QandA_dict[subject])
        else:
            print("Please press x to show answer.\n")
            print(subject)