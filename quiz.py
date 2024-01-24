name = input("What is your name?: ").lower()
start_quiz = input("Do you want to start the quiz?, enter yes or no: ").lower()
if start_quiz == "no":
    quit()
else:
    print(f"Let's start the quiz {name}, you will get 5 questions")

score = 0

question_1 = input("What colour is the sky?: ").lower()
if question_1 != "blue":
    print("Incorrect")
else:
    print("Well done you got it right you get a point!")
    score += 1
question_2 = input("What colour is the grass?: ").lower()
if question_2 != "green":
    print("Incorrect")
else:
    print("Well done you got it right you get a point")
    score += 1
question_3 = input("What noise does a dog make?: ").lower()
if question_3 != "woof":
    print("Incorrect")
else:
    print("Well done you got it right you get a point")
    score += 1
print("Question 4 and 5 is multiple choice worth 2 points each")

question_4 = input("When did the england football club win the world cup?\n "
                   "A: 1966, B: 1970, C:1986 ").lower()
if question_4 == "1966" or "A":
    print("Well done you get 2 points")
    score += 2
else:
    print("Incorrect")

question_5 = input("Who has scored the most goals in the premier league?\n "
                   "A: Alan Shearer, B: Harry Kane, C: Wayne Rooney ").lower()
if question_5 == "Alan Shearer" or "A":
    print("Well done you got 2 points")
    score += 2
else:
    print("Incorrect")

print(f"{name}, your final score is {score}.")


