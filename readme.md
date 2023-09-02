# Random Question Generator API

This is a simple Python application that provides an API for generating random questions based on different difficulty levels and a total score constraint. The questions are retrieved from a PostgreSQL database, and you can customize the total score and the number of questions you want.

## Prerequisites

Before using this application, make sure you have the following prerequisites installed:

1. Python 3
2. Flask (Python web framework)
3. PostgreSQL (for the database)

## Setting Up the PostgreSQL Database

1. Install PostgreSQL on your system if you haven't already. You can download it from the official website: https://www.postgresql.org/download/

2. Create a new PostgreSQL database for this application:

   ```bash
   createdb random_question_generator```

3. Create a table to store your questions. You can use the following SQL script as a reference:
```sql
    CREATE TABLE QuestionBank (
        q_id SERIAL PRIMARY KEY,
        q_code VARCHAR(10) NOT NULL,
        question TEXT NOT NULL,
        correct_answer TEXT NOT NULL,
        difficulty_level VARCHAR(10) NOT NULL,
        score INT NOT NULL
    );
```
Populate the QuestionBank table with your questions. You can use SQL INSERT statements to add questions to the table.

## Requirements
`requirements.txt`
blinker==1.6.2
click==8.1.7
colorama==0.4.6
Flask==2.3.2
itsdangerous==2.1.2
Jinja2==3.1.2
MarkupSafe==2.1.3
psycopg2==2.9.7
Werkzeug==2.3.7

## Running the Application
1. Clone this repository to your local machine.

2. Navigate to the project directory:
```bash
cd API-for-Quiz-Exam-Intern-Task/Flask_API
```

3. Install the required Python packages using `pip`:
```bash
pip install -r requirements.txt
```

4. Start the Flask application:
```bash
python app.py
```

The API should now be running locally.

## Using the API
### API Endpoint 1: Generate Questions by Total Score and Number of Questions
You can use this API endpoint to generate a list of questions based on your desired total score and the number of questions you want.

* Endpoint: `/API1`
* HTTP Method: GET
* Parameters:
    * total_score: The total score constraint (e.g., 50).
    * num_questions: The number of questions you want (e.g., 20).

Example Request:
```
"http://localhost:5000/API1?total_score=50&num_questions=20"
```

### API Endpoint 2: Generate Questions by Difficulty Levels and Number of Questions
This API endpoint allows you to generate questions by specifying the number of questions you want for each difficulty level (Easy, Medium, Advanced) and the total number of questions you want.
* Endpoint: /API2
* HTTP Method: GET
* Parameters:
    * Easy: The number of Easy difficulty questions you want.
    * Medium: The number of Medium difficulty questions you want.
    * Advanced: The number of Advanced difficulty questions you want.
    * num_questions: The total number of questions you want.

Example Request:
```
"http://localhost:5000/API2?Easy=5&Medium=5&Advanced=10&num_questions=20"
```

## Notes
* The questions are retrieved from the PostgreSQL database and randomly selected based on the specified constraints.
* The API returns a JSON response containing the generated questions.

Feel free to customize the database, questions, and constraints as needed for your specific use case.

## Example Responses

### API 1: Generate Questions by Total Score and Number of Questions

Example Response:

```json
{
    "questions": [
        {
            "q_id": 1,
            "q_code": "Q1",
            "question": "What is the capital of France?",
            "correct_answer": "Paris",
            "difficulty_level": "Easy",
            "score": 1
        },
        {
            "q_id": 5,
            "q_code": "Q5",
            "question": "What is the formula for water?",
            "correct_answer": "H2O",
            "difficulty_level": "Medium",
            "score": 3
        },
        {
            "q_id": 8,
            "q_code": "Q8",
            "question": "Solve for x: 2x + 5 = 15",
            "correct_answer": "x = 5",
            "difficulty_level": "Advanced",
            "score": 5
        },
        // More questions...
    ]
}
```

### API 2: Generate Questions by Difficulty Levels and Number of Questions

Example Response:

```json
{
    "questions": [
        {
            "q_id": 2,
            "q_code": "Q2",
            "question": "Who wrote the play 'Romeo and Juliet'?",
            "correct_answer": "William Shakespeare",
            "difficulty_level": "Easy",
            "score": 1
        },
        {
            "q_id": 6,
            "q_code": "Q6",
            "question": "What is the largest planet in our solar system?",
            "correct_answer": "Jupiter",
            "difficulty_level": "Medium",
            "score": 3
        },
        {
            "q_id": 10,
            "q_code": "Q10",
            "question": "What is the chemical symbol for gold?",
            "correct_answer": "Au",
            "difficulty_level": "Advanced",
            "score": 5
        },
        // More questions...
    ]
}
```


# Conclusion

> [!NOTE]
> This README provides an overview of the Random Question Generator API, including setup instructions, API usage and example responses You can integrate this API into your applications to generate random questions for quizzes, tests, or educational purposes.

`Thank you For Visiting ` [Shathis Kannan Dev Page](https://github.com/ShathisKannan19).
Happy Coding!

