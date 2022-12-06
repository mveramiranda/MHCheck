"""
Alpha version of MHCheck. This version uses a command line interface for the users to respond the quiz
and return their results. The quiz in this version is not powered by machine learning, but rather
it just assesses the user score. The questions are taken from 
https://www.nhs.uk/mental-health/self-help/guides-tools-and-activities/depression-anxiety-self-assessment-quiz/
"""
def exit():
    print("Thank you for using MHCheck!\n")
    print("Exiting...")
    quit()

def welcome(): 
    """
    This function is the initial point of the application. It displays a welcome message to the user, prompts
    the menu, and calls the selected function by the user
    """
    # welcome message 
    print("Welcome to MHCheck, a mental health self-assessment questionnaire designed by students for students!\n\n")

    #selection
    print("To begin your assesment, please type 1.\n")
    print("If you wish to view your previous results, please type 2 (NOT IMPLEMENTED)\n")
    print("If you wish to exit, press 3\n")

    selection = input("Enter 1, 2 or 3: ")

    if selection == "1":
        quiz()

    elif selection == "2":
        results()

    elif selection == "3":
        exit()

    else: 
        print("Invalid input, please try again")
        welcome()

#TODO: implement quiz
def quiz():
    print("This is the MHCHeck questionnaire. The following 16 questions are designed to help you better understand your feelings and state of mind\n")
    print("When answering each of the questions, think on how you have been feeling over the past 1-2 weeks. Please be truthful with your answers\n")
    print("Remember that MHCheck is not meant to replace a professional consultation, it simply will help point you in the right direction\n")
    print("When you're ready to begin, press 1 to start the questionnaire\n")
    print("If you press anything else, the application will exit\n")

    selection = input("Your input: ")
    
    if (selection != "1"):
        exit()
    else:
        depscore = 0
        print("For each question, type the number corresponding to the option that feels more accurate to your current feelings in the past few weeks.\n")
        print("\n1. How often have you been bothered by feeling down, depressed or hopeless?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n2. How often have you had little interest or pleasure in doing things?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n3. How often have you been bothered by trouble falling or staying asleep, or sleeping too much?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n4. How often have you been bothered by feeling tired or having little energy?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n5. How often have you been bothered by poor appetite or overeating?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n6. How often have you been bothered by feeling bad about yourself, or that you are a failure, or have let yourself or your family down?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n7. How often have you been bothered by trouble concentrating on things, such as reading the newspaper or watching television?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n8. How often have you been bothered by moving or speaking so slowly that other people could have noticed, or the opposite - being so fidgety or restless that you have been moving around a lot more than usual?\n")
        depscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)

        anxscore = 0
        print("\n9. How often have you been bothered by feeling nervous, anxious or on edge?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n10. How often have you been bothered by not being able to stop or control worrying?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n11. How often have you been bothered by worrying too much about different things?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n12. How often have you been bothered by having trouble relaxing?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n13. How often have you been bothered by being so restless that it is hard to sit still?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n14. How often have you been bothered by becoming easily annoyed or irritable?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)
        print("\n15. How often have you been bothered by feeling afraid as if something awful might happen?\n")
        anxscore += (int(input("1 - Not at all\n 2 - Several days\n 3 - More than half the days\n 4 - Nearly every day\n")) - 1)

        print("You have reached the end of the MHCheck questionnaire!\n")
        print("The following are your results:\n")
        print("Depression score: ", round((depscore/24) * 100), "%\n")
        print("Anxiety score: ", round((anxscore/21) * 100), "%\n")

        #TODO: optional questions

        #TODO: add results meaning personalized to reult
        print("The obtained scores represent the likelihood of presenting anxiety and depression, respectively, based on your symptoms\n")
        print("Remember that this isn't a formal evaluation; MHCheck is only a tool to point you in the right direction for your next steps. Please consult a medical professional with all your concerns\n")

        return