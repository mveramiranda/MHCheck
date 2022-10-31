"""
Alpha version of MHCheck. This version uses a command line interface for the users to respond the quiz
and return their results. The quiz in this version is not powered by machine learning, but rather
it just assesses the user score. The questions are taken from 
https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/depression-anxiety-self-assessment-quiz/
"""


def welcome(): 
    # welcome message 
    print("Welcome to MHCheck, a mental health self-assessment questionnaire designed by students for students!\n\n")

    #selection
    print("To begin your assesment, please type 1.\n")
    print("If you wish to view your previous results, please type 2 (NOT IMPLEMENTED)\n")
    print("If you wish to exit, press 3\n3")

    selection = input("Enter 1, 2 or 3: ")

    if selection == "1":
        quiz()

    elif selection == "2":
        results()

    elif selection == "3":
        print("Thank you for using MHCheck!\n")
        print("Exiting...")
        quit()

    else: 
        print("Invalid input, please try again")
        welcome()

#TODO: implement quiz
def quiz():
    print("Quiz!")

#TODO implement results
def results():
    print("Results")

welcome()