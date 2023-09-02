#For from Sql Database Sever
from flask import Flask, request, jsonify
import psycopg2
import random

app = Flask(__name__)

def get_db_connection():
    return psycopg2.connect(
        host="your_host",
        database="your_database",
        user="your_user",
        password="your_password"
    )

@app.route('/API1', methods=['GET'])
def random_question_score():
    try:
        total_score = int(request.args.get('total_score'))
        num_questions = int(request.args.get('num_questions'))
        
        connection = get_db_connection()
        cursor = connection.cursor()

        question_list = []
        
        # Select questions randomly based on total score and number of questions
        while total_score > 0 and num_questions > 0:
            difficulty_level = random.choice(["Easy", "Medium", "Advanced"])
            max_score = 5 if difficulty_level == "Advanced" else 3 if difficulty_level == "Medium" else 1
            
            if max_score <= total_score:
                cursor.execute(
                    f"SELECT q_id, question, score FROM QuestionBank WHERE difficulty_level = %s AND score = %s ORDER BY random() LIMIT 1",
                    (difficulty_level, max_score)
                )
                question = cursor.fetchone()
                if question:
                    question_list.append(question)
                    total_score -= max_score
                    num_questions -= 1

        connection.close()
        return jsonify(question_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/API2', methods=['GET'])
def random_question_level():
    try:
        Easy = int(request.args.get('Easy'))
        Medium = int(request.args.get('Medium'))
        Advanced = int(request.args.get('Advanced'))
        num_questions = int(request.args.get('num_questions'))
        
        connection = get_db_connection()
        cursor = connection.cursor()

        question_list = []

        while Easy > 0 or Medium > 0 or Advanced > 0 or num_questions > 0:
            if Easy > 0:
                cursor.execute(
                    f"SELECT q_id, question, score FROM QuestionBank WHERE difficulty_level = 'Easy' AND score = 1 ORDER BY random() LIMIT 1"
                )
                question = cursor.fetchone()
                question_list.append(question)
                Easy -= 1
                num_questions -= 1
            elif Medium > 0:
                cursor.execute(
                    f"SELECT q_id, question, score FROM QuestionBank WHERE difficulty_level = 'Medium' AND score = 3 ORDER BY random() LIMIT 1"
                )
                question = cursor.fetchone()
                question_list.append(question)
                num_questions -= 1
                Medium -= 1
            elif Advanced > 0:
                cursor.execute(
                    f"SELECT q_id, question, score FROM QuestionBank WHERE difficulty_level = 'Advanced' AND score = 5 ORDER BY random() LIMIT 1"
                )
                question = cursor.fetchone()
                question_list.append(question)
                num_questions -= 1
                Medium -= 1
            elif num_questions > 0:
                difficulty_level = random.choice(["Easy", "Medium", "Advanced"])
                max_score = 5 if difficulty_level == "Advanced" else 3 if difficulty_level == "Medium" else 1
                
                if max_score <= total_score:
                    cursor.execute(
                        f"SELECT q_id, question, score FROM QuestionBank WHERE difficulty_level = %s AND score = %s ORDER BY random() LIMIT 1",
                        (difficulty_level, max_score)
                    )
                    question = cursor.fetchone()
                    if question:
                        question_list.append(question)
                        num_questions -= 1

        connection.close()
        return jsonify(question_list)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5000)
