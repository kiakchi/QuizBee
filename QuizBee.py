# This is a quiz bee game for kids

def easyround():
    answer = []
    correct_answer = 0
    easyopt_num = 1

    print("**************************")
    print("EASY Categories")
    print("**************************")
    for eround in easy_questions:
        print(eround)
        for easyopt in easy_option[easyopt_num-1]:
            print(easyopt)
        easy_ans = input("Please enter your answer (A, B, C, or D): ")
        easy_ans = easy_ans.upper()
        answer.append(easy_ans)
        correct_answer += easycheck_answer(easy_questions.get(eround), easy_ans) # (easy_questions.get(eround) - means to get the value from dictionary
        easyopt_num += 1

    edisplay_score(correct_answer, easy_ans)
    return correct_answer

def easycheck_answer(ecorrect_answer, easy_ans):
    if ecorrect_answer == easy_ans:
        print("Correct!")
        print("**************************")
        return 1

    else:
        for a in easy_questions:
            print("Incorrect!")
            print("**************************")
            return 0

def edisplay_score(correct_answer, easy_ans):
    print("*******************************")
    print("Results:")
    print("You got", correct_answer, "correct answers for easy round")
    print("Round 1 finished")
    print("*******************************")
    input("Press enter to continue...")
    print("++++++++++++++++++++++++++")
    print("Let's proceed to Round 2")
    print("++++++++++++++++++++++++++")

def medround():
    answer = []
    medcorrect_answer = 0
    medopt_num = 1
    print("**************************")
    print("MEDIUM Categories")
    print("**************************")
    for mround in med_questions:
        print(mround)
        for medopt in med_option[medopt_num - 1]:
            print(medopt)
        med_ans = input("Please enter your answer (A, B, C, or D): ")
        med_ans = med_ans.upper()
        answer.append(med_ans)
        medcorrect_answer += medcheck_answer(med_questions.get(mround),
                                           med_ans)  # (med_questions.get(mround) - means to get the value from dictionary
        medopt_num += 1

    mdisplay_score(medcorrect_answer, med_ans)
    return medcorrect_answer

def medcheck_answer(mcorrect_answer, med_ans):
    if mcorrect_answer == med_ans:
        print("Correct!")
        print("**************************")
        return 1

    else:
        for a in med_questions:
            print("Incorrect!")
            print("**************************")
            return 0

def mdisplay_score(medcorrect_answer, med_ans):
    print("*******************************")
    print("Results:")
    print("You got", medcorrect_answer, "correct answers for medium round")
    print("Round 2 finished")
    print("*******************************")
    input("Press enter to continue...")
    print("++++++++++++++++++++++++++")

def hardround():
    answer = []
    hardcorrect_answer = 0
    hardopt_num = 1
    print("**************************")
    print("HARD Categories")
    print("**************************")
    for hround in hard_questions:
        print(hround)
        for hardopt in hard_option[hardopt_num - 1]:
            print(hardopt)
        hard_ans = input("Please enter your answer (A, B, C, or D): ")
        hard_ans = hard_ans.upper()
        answer.append(hard_ans)
        hardcorrect_answer += hardcheck_answer(hard_questions.get(hround),
                                             hard_ans)  # (med_questions.get(mround) - means to get the value from dictionary
        hardopt_num += 1

    hardisplay_score(hardcorrect_answer, hard_ans)
    return hardcorrect_answer

def hardcheck_answer(hcorrect_answer, hard_ans):
    if hcorrect_answer == hard_ans:
        print("Correct!")
        print("**************************")
        return 1

    else:
        for a in hard_questions:
            print("Incorrect!")
            print("**************************")
            return 0
def hardisplay_score(hardcorrect_answer, hard_ans):
    print("*******************************")
    print("Results:")
    print("You got", hardcorrect_answer, "correct answers for Hard round")
    print("Round 3 finished")
    print("*******************************")
    input("Press enter to continue...")
    print("++++++++++++++++++++++++++")
def play_again():
    playagain = input("Do you want to play again: (yes or no): ")
    playagain = playagain.upper()

    if playagain == "YES" or playagain == "Y":
        return True
    else:
        return False

easy_questions = {
    "What color do you get when you mix blue and yellow?":"B",
    "How many legs does a spider have?":"A",
    "What is the tallest land animal?":"B",
    "What do caterpillars turn into?":"C",
    "What do we call baby dogs?":"D"
}

med_questions = {
    "What do plants need from sunlight to make food?":"D",
    "What gas do we breathe in that our bodies need?":"D",
    "What is the largest ocean on Earth?":"B",
    "Which animal is famous for black-and-white stripes?":"A",
    "Which planet is known as the Red Planet?":"C"
}

hard_questions = {
    "What do we call Earth’s blanket of air?":"C",
    "Which continent has the most people?":"A",
    "What force keeps us on the ground?":"A",
    "What is the center of an atom called?":"B",
    "What is the freezing point of water in Celsius?":"D"


}
easy_option = [["A: ", "B: Green", "C: ", "D: "],
              ["A: Eight", "B: ", "C:  ", "D: "],
              ["A: " , "B: Giraffe", "C: ", "D: "],
              ["A: ", "B: ", "C: Butterflies", "D: "],
              ["A: ", "B: ", "C: ", "D: Puppies "]]
med_option = [["A: ", "B: ", "C: ", "D: Energy for photosynthesis"],
              ["A: ", "B: ", "C: ", "D: Oxygen "],
              ["A: ", "B: Pacific Ocean", "C: ", "D: "],
              ["A: Zebra", "B: ", "C: ", "D: "],
              ["A: ", "B: ", "C: Mars", "D: "]]
hard_option = [["A: ", "B: ", "C: The atmosphere", "D: "],
               ["A: Asia", "B: ", "C: ", "D: "],
               ["A: Gravity", "B: ", "C: ", "D: "],
               ["A: ", "B: The nucleus", "C: ", "D: "],
               ["A: ", "B: ", "C: ", "D: 0°C"]]

#main program
name = input("Enter player name: ")
print("*************************")
print("Welcome:" + " " + name)
print("*************************")
print("This is a Quiz Game for kids")
print("There will be 3 Categories")
print("The categories are: Easy, Medium and Hard")
print("Each categories will have 5 questions")
print("Good Luck!!!")
input("Press enter to continue...")

round_1 = easyround()
round_2 = medround()

print("Lets recap the score")
print("Round 1 score: ", round_1)
print("Round 2 score: ", round_2)
input("press enter to continue")

round_3 = hardround()
print("*************************")
print("Lets recap the score")
print("*************************")
print("Round 1 score: ", round_1)
print("Round 2 score: ", round_2)
print("Round 3 score: ", round_3)
print("*************************")

while play_again():
    easyround()
    medround()
    print("Lets recap the score")
    print("Round 1 score: ", round_1)
    print("Round 2 score: ", round_2)
    input("press enter to continue")
    hardround()
    print("*************************")
    print("Lets recap the score")
    print("*************************")
    print("Round 1 score: ", round_1)
    print("Round 2 score: ", round_2)
    print("Round 3 score: ", round_3)
    print("*************************")

print("See you")

