import random

from questions import questions

def random_question_score():
    total_score = 50  # Set the total score you want (50 in this case)
    num_questions = 20  # Set the number of questions you want (20 in this case)

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

    return question_list

if __name__ == "__main__":
    selected_questions = random_question_score()
    for i, question in enumerate(selected_questions, start=1):
        print(f"Question {i}:")
        print(f"q_id: {question['q_id']}")
        print(f"q_code: {question['q_code']}")
        print(f"Question: {question['question']}")
        print(f"Correct Answer: {question['correct_answer']}")
        print(f"Difficulty Level: {question['difficulty_level']}")
        print(f"Score: {question['score']}")
        print("\n")
    value  = 0 
    for i in selected_questions:
        value = value+ i["score"]

    print("Value of Total : :  ", value)
