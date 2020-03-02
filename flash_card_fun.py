import subprocess

def user_chooses_questions():
    choice = 0
    file_count = 2

    while not 1 <= choice <= file_count:
        choice = input(" Enter the Number for the questions you like to review:\n1) questions that need better answers\n2)QandA\n")
        try:
            choice = int(choice)
        except:
            subprocess.run("clear")
            print("That was not a number. Please enter a numeral.\n")
            choice = 0

        if not 1 <= choice <= file_count:
            print("Remeber to enter a number from one of the choices.\n")

    if choice == 1:
        return("questions_to_research")
    elif choice == 2:
        return("QandA")
