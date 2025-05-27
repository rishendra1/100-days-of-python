import random

class AddQuestions:
    def __init__(self):
        self.question_list = []
    def add_question(self,question,answer):
        self.question_list.append((question,answer))
    def quiz(self):
        print("Welcome!!!")
        Quiz = self.question_list
        score = 0
        tot_questions = 0
        while True:
            print(f"Your Score is {score}/{tot_questions}")
            choice1 = random.choice(Quiz)
            answer = input(choice1[0]).lower()
            if answer == choice1[1]:
                print("Correct")
                score += 1
                tot_questions += 1
            else:
                print("Incorrect")
                print("Correct answer is :", choice1[1])
                tot_questions += 1
            if tot_questions == 3 or tot_questions == 6 or tot_questions == 9 or tot_questions == 15:
                choice2 = input("Do you want to end quiz y/n: ").lower()
                if choice2 == "y":
                   break
                if choice2 == "n":
                   continue
            elif tot_questions == 20:
                break
        print("Thank you for taking the quiz")

general_fact_qa = [
    ("what is the capital of france?", "paris"),
    ("which planet is known as the red planet?", "mars"),
    ("what gas do humans breathe in to survive?", "oxygen"),
    ("what is the hardest natural substance?", "diamond"),
    ("what is the chemical symbol for water?", "h2o"),
    ("who wrote 'hamlet'?", "shakespeare"),
    ("what is the largest mammal on earth?", "bluewhale"),
    ("which continent is egypt located in?", "africa"),
    ("what is the boiling point of water in celsius?", "100"),
    ("which ocean is the largest?", "pacific"),
    ("what is the national sport of japan?", "sumo"),
    ("which country invented pizza?", "italy"),
    ("who painted the mona lisa?", "davinci"),
    ("what is the tallest mountain in the world?", "everest"),
    ("what organ pumps blood through the body?", "heart"),
    ("which color is made by mixing red and blue?", "purple"),
    ("what is the smallest prime number?", "2"),
    ("which bird is known for its colorful tail?", "peacock"),
    ("what is the longest river in the world?", "nile"),
    ("which planet is closest to the sun?", "mercury"),
]
Question = AddQuestions()
for i in range(0, len(general_fact_qa)):
    Question.add_question(general_fact_qa[i][0], general_fact_qa[i][1])
Question.quiz()
