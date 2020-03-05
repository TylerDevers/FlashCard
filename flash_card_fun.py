#! /usr/bin/python3

import subprocess
from os import listdir #get files from a directory
import os

def list_files_in_path(my_path):
    return listdir(my_path)


def user_chooses_questions():
    choice = -1
    my_file_list = list_files_in_path("questions_dir")
    file_count = len(my_file_list)
    
    while not 0 <= choice < file_count:
        print("Enter the option number to choose the category of questions you prefer:\n")
        for item in my_file_list:
            print(f"{my_file_list.index(item)})  {item}\n")
        choice = input()
        try:
            choice = int(choice)
        except:
            subprocess.run("clear")
            print("That was not a number. Please enter a numeral.\n")
            choice = -1

        if not 0 <= choice <= file_count:
            subprocess.run("clear")
            print("Remeber to enter a number from one of the choices.\n")

    return(my_file_list[choice])
   

