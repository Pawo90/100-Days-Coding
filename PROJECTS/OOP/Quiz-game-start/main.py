from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

# Building Question Bank
question_bank = []
# First solution
# for index in range(len(question_data)-1):
#     question_bank.append(Question(question_data[index]['text'], question_data[index]['answer']))

# Second solution
for question in question_data:
    question_text = question['text']
    question_answer = question['answer']
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

