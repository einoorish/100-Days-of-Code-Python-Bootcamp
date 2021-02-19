from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
import requests

from ui import QuizInterface

API_URL = "https://opentdb.com/api.php?amount=10&category=19&type=boolean"

response = requests.get(url=API_URL)
response.raise_for_status()
data = response.json()["results"]

question_bank = []
for question in data:
    text = question["question"]
    answer = question["correct_answer"]
    question_bank.append(Question(text, answer))

quiz = QuizBrain(question_bank)
quiz_ui = QuizInterface(quiz)

#while quiz.still_has_questions():
 #   quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{quiz.question_number}")
