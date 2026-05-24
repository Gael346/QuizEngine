import random
import math

def main():
    # The user interface for create the quiz
    print("Welcome to Math Quiz")
    print("Select the type of the Quiz")
    print()
    print("1- Normal \n2- Test")
    print()
    selection = get_int()
    # if is a quiz normal
    if selection == 1:
        # Get the difficulty (from 1 to 4) and the number of questions 
        print()
        print("You selected normal Quiz")
        print()
        print("Select the difficulty of the quiz")
        print()
        print("1- Easy \n2- Medium \n3- Hard \n4- Expert")
        print()
        selection = get_int()
        print()
        print("How many questions do you want?")
        print()
        difficulty = selection
        selection = get_int()
        number_of_questions = selection
        # Create the quiz and run it
        quiz = create_quiz(number_of_questions,quiz_type="normal",dif=difficulty)
        run_quiz(quiz,type="normal")
    # if is a quiz type test
    elif selection == 2:
         # Get the difficulty (from 1 to 4) and the number of questions and the number of options in each question
        print()
        print("You selected test Quiz")
        print()
        print("Select the difficulty of the quiz")
        print()
        print("1- Easy \n2- Medium \n3- Hard \n4- Expert")
        print()
        selection = get_int()
        print()
        difficulty = selection
        print("How many questions do you want?")
        print()
        selection = get_int()
        number_of_questions = selection
        print()
        print("How many options do you want?")
        print()
        selection = get_int()
        # Create the quiz and run it
        quiz = create_quiz(number_of_questions,quiz_type="test",choices=selection,dif=difficulty)
        run_quiz(quiz,type="test")


def run_quiz(test:list,type:str):
    
    # Run the quiz and save the results in a dictionary (scores)
    scores = {"correct":0,"incorrect":0,"grade":""}
    questions = test.keys()
    # Run normal quiz
    if type == "normal":
        for question in questions :
            print()
            print(question)
            print()
            response = get_int()
            if response == test[question]:
                scores["correct"] += 1
            else:
                scores["incorrect"] += 1
    # Run quiz type test
    elif type == "test":
        for question in questions:
            print()
            print(question)
            print()
            correct = 0
            correct_answer,options = test[question]
            for i,option in enumerate(options):       
                print(f"{i}){option}")
                if option == correct_answer:
                    correct = i
            print()
            response = get_int()
            if response == correct:
                scores["correct"] += 1
            else :
                    scores["incorrect"] += 1

   # Calculate the grade and print the results
    if scores["correct"] == 0:
        scores["grade"] = 0.0
    elif scores["incorrect"] == 0:
        scores["grade"] = 10.0
    else:
        scores["grade"] = (scores["correct"] / (scores["correct"] + scores["incorrect"])) * 10.0

    print()
    print(f"Your grade is: {scores['grade']:.2f}")
    print(f"Correct answers: {scores['correct']}")
    print(f"Incorrect answers: {scores['incorrect']}")


    
PREFAB_QUESTIONS = {
    "What is the value of (π) rounded at two decimals?": 3.14,
    "What is the value of (e) rounded at two decimals?": 2.71,
    "How many vertices does a cube have?":8,
    "How many faces does a cube have?": 6,
    "How many digits does the number 1000 have?": 4,
    "How many sides does a triangle have?": 3,
    "How many sides does a square have?": 4,
    "How many prime numbers are there between 1 and 20?": 8,     
    "How many divisors does the number 12 have?": 6,             
    "How many divisors does the number 15 have?": 4,             
    "What is the smallest prime number?": 2,
    "What is the largest single-digit number?": 9,
    "How many multiples of 3 are there between 1 and 30?": 10,
    }


def create_quiz(num_of_questions:int,quiz_type:str,choices=4,dif=4)-> list:

    choices -= 1
    quiz = {}

    for i in range(num_of_questions):

        # Generate different types of questions and different numbers based on the difficulty level
        # When the level is more high there are more type of questions and the numbers are bigger
        match dif:
            case 1:
                num1 = random.randint(1, 30)
                num2 = random.randint(1, 30)
                quesType = random.randint(0,1)
            case 2:
                num1 = random.randint(1, 100)
                num2 = random.randint(1, 100)
                quesType = random.randint(0, 3)
            case 3:
                num1 = random.randint(300, 1000)
                num2 = random.randint(300, 1000)
                quesType = random.randint(0, 5)
            case 4:
                num1 = random.randint(800, 1500)
                num2 = random.randint(800, 1500)
                quesType = random.randint(0, 7)

        # Generate random questions and save in a dictionary (quiz) with the response as value
        match quesType:
            case 0:
                question = f"{num1} + {num2}?"
                response = num1 + num2
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                  quiz[question] = get_options(response,choices)
            case 1:
                question = f"{num1} - {num2}?"
                response = num1 - num2
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                     quiz[question] = get_options(response,choices)
                   
            case 2:
                num1 = random.randint(1,25) if dif <= 2 else random.randint(1,50)
                num2 = random.randint(1,25) if dif <= 2 else random.randint(1,50)
                question = f"{num1} * {num2}?"
                response = num1 * num2
                if quiz_type == "normal":
                    quiz[question] = num1 * num2
                elif quiz_type == "test":
                     quiz[question] = get_options(response,choices)
                
            case 3:
                num1 = random.randint(1,5) if dif <= 3 else random.randint(1,10)
                num2 = random.randint(1,4) if dif <= 3 else random.randint(1,10)
                question = f"{num1} to the power of {num2}?"
                response = num1 ** num2
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                    quiz[question] = get_options(response,choices)
            case 4:
                num1 = random.randint(1, 20)
                question = f"What is the square root of {num1**2}?"
                response = num1
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                    quiz[question] = get_options(response,choices)
            case 5:
                # This is special because the questions and responses are pre‑fabricated and not generated randomly
                question , response = random.choice(list(PREFAB_QUESTIONS.items()))
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                    quiz[question] = get_options(response,choices)
            case 6:
                num1  = random.randint(0, 12)
                question = f"{num1}! ?"
                response =  math.factorial(num1)
                
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                    quiz[question] = get_options(response,choices)
            case 7:
                num1 = random.randint(1, 20)
                num2 = random.randint(1, 10)
                number_to_question = random.randint(0,1)
                if number_to_question == 0:
                    question = f"What is the coefficient of the derivative of {num1}x raised to {num2}"
                    response = num1 * num2
                else:
                    question = f"What is the exponent of the derivative of {num1}x raised to {num2}"
                    response = num2 - 1
                if quiz_type == "normal":
                    quiz[question] = response
                elif quiz_type == "test":
                    quiz[question] = get_options(response,choices)
    return quiz


# Get the user input
def get_int():
    while True:
        try:
            num = int(input("Response: "))
            return num
        except ValueError:
            continue

# Generate the options for the quiz adding a random number and saving the response in a tuple with result and options
def get_options(response:int,choices:int)->tuple:
    options = [ response+random.randint(-choices*5,choices*5) for _ in range(choices)]
    options = [round(x, 2) if x != response and options.count(x) == 1 else random.randint(-choices*5,choices*5)+response for x in options]
    options.insert(random.randint(1,choices),response)
    return (response,options)


main()
