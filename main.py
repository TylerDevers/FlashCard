#! /usr/bin/python3

# TODO sort out user_to_choose function. Issues with file name being opened by the reader.
import csv
import subprocess # needed to run $ clear bash command.
from flash_card_fun import user_chooses_questions

QandA_dict = {}
questions_completed_dict = {}

# gets input from user about which file to read questions from.
file_to_use = f"questions_dir/{user_chooses_questions()}"

# Reads questions file and stores in Dictionary for easy iteration
with open(file_to_use, mode="r") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=";")
    for row in csv_reader:
        # print(row) # for debugging
        QandA_dict.update( {row[0]:row[1]} )

# Prints question to standard output
for question in QandA_dict:
    answer = QandA_dict[question]
    print(f"{question}\n")
    input("Press enter to continue.\n")
    print(f"{answer} \n")
    input("Press enter to continue.\n")
    subprocess.run('clear')