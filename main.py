#! /usr/bin/python3

# TODO sort out user_to_choose function. Issues with file name being opened by the reader.
import csv
import subprocess # needed to run $ clear bash command.
from flash_card_fun import *

QandA_dict = {}
questions_completed_dict = {}
file_to_use = user_chooses_questions()

with open(file_to_use, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        # print(row) # for debugging
        QandA_dict.update( {row[0]:row[1]} )


# for subject in QandA_dict:
#     print(f"{subject}\n")
#     input("Press enter to continue.\n")
#     print(f"{QandA_dict[subject]} \n")
#     input("Press enter to continue.\n")
#     subprocess.run('clear')