# This is a quiz bee game for kids

name = input("Enter player name: ")
print("*************************")
print("Welcome" + " " + name)
print("*************************")
print("This is a Quiz Game for kids")
print("There will be 3 Categories")
print("The categories are: Easy, Medium and Hard")
print("Each categories will have 5 questions")
print("Good Luck!!!")

def easyround():
    answer = []
    correct_answer = 0
    easyopt_num = 1
    print("**************************")
    print("EASY Categories")
    print("**************************")
    for eround in easy_questions:
        print("++++++++++++++++++++++++++")
        print(eround)
        for easyopt in easy_option[easyopt_num-1]:
            print(easyopt)
        easy = input("Please enter your answer (A, B, C, or D): ")
        easy = easy.upper()
        easyopt_num += 1


def check_answer():
    pass

def display_score():
    pass

def play_again():
    pass

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

easyround()

