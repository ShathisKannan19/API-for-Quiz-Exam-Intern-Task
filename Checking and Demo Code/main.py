#Checking in CMD
import random

# Define your questions in a separate module or file and import them here
from questions import questions

# # API 1: Get random questions based on total score and number of questions
def random_question_score():
    total_score = int(input("Enter Total Score You Want :"))
    num_questions = int(input("Enter No. of Questions : "))

    question_list = []

    while total_score > 0 and num_questions > 0:
        difficulty_level = random.choice(["Easy", "Medium", "Advanced"])
        max_score = 5 if difficulty_level == "Advanced" else 3 if difficulty_level == "Medium" else 1

        if max_score <= total_score:
            available_questions = [q for q in questions if q['difficulty_level'] == difficulty_level and q['score'] == max_score]
            if available_questions:
                selected_question = random.choice(available_questions)
                question_list.append(selected_question)
                total_score -= max_score
                num_questions -= 1

    for i in question_list:
        print(i)

# API 2: Get random questions based on the number of each difficulty level and total number of questions
def random_question_level():
    num_easy = int(input("Enter the No. of Easy Questions :"))
    num_medium = int(input("Enter the No. of Medium Questions :"))
    num_advanced = int(input("Enter the No. of Advanced Questions :"))
    num_questions = int(input("Enter the No. of Total Questions :"))

    question_list = []

    while num_easy > 0 or num_medium > 0 or num_advanced > 0 or num_questions > 0:
        if num_easy > 0:
            available_questions = [q for q in questions if q['difficulty_level'] == 'Easy' and q['score'] == 1]
            if available_questions:
                selected_question = random.choice(available_questions)
                question_list.append(selected_question)
                num_easy -= 1
                num_questions -= 1

        if num_medium > 0:
            available_questions = [q for q in questions if q['difficulty_level'] == 'Medium' and q['score'] == 3]
            if available_questions:
                selected_question = random.choice(available_questions)
                question_list.append(selected_question)
                num_medium -= 1
                num_questions -= 1

        if num_advanced > 0:
            available_questions = [q for q in questions if q['difficulty_level'] == 'Advanced' and q['score'] == 5]
            if available_questions:
                selected_question = random.choice(available_questions)
                question_list.append(selected_question)
                num_advanced -= 1
                num_questions -= 1

        if num_questions > 0:
            difficulty_level = random.choice(["Easy", "Medium", "Advanced"])
            max_score = 5 if difficulty_level == "Advanced" else 3 if difficulty_level == "Medium" else 1

            available_questions = [q for q in questions if q['difficulty_level'] == difficulty_level and q['score'] == max_score]
            if available_questions:
                selected_question = random.choice(available_questions)
                question_list.append(selected_question)
                num_questions -= 1

    for i in question_list:
        print(i)

# For Checking this File is Working or Not
#random_question_score()
# random_question_level()