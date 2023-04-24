from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.score = 0

        self.window = Tk()
        self.window.title("Quizzler")
        # self.window.geometry("500x500")
        self.window.configure(padx=20, pady=20, bg=THEME_COLOR)

        self.lbl_score = Label(text=f"Score: {self.score}",
                               bg=THEME_COLOR,
                               fg="white",
                               font=("Arial", 20, "italic")
                               )
        self.lbl_score.grid(row=0, column=1)

        self.canvas = Canvas()
        self.canvas.configure(bg='white', height=250, width=300)
        self.question_text = self.canvas.create_text(125, 150, text="Question_Text",
                                                     width=260, font=("Arial", 20, "italic"),
                                                     fill=THEME_COLOR
                                                     )

        self.canvas.grid(row=1, column=0, columnspan=2, pady=10, sticky="nesw")

        btn_true_img = PhotoImage(file="./images/true.png")
        self.btn_true = Button(image=btn_true_img, highlightthickness=0, command=self.true_pressed)
        self.btn_true.grid(row=2, column=0)

        btn_false_img = PhotoImage(file="./images/false.png")
        self.btn_false = Button(image=btn_false_img, highlightthickness=0, command=self.false_pressed)
        self.btn_false.grid(row=2, column=1)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.configure(bg="white")
        if self.quiz.still_has_questions():
            self.lbl_score.configure(text=f"Score: {self.quiz.score}/{self.quiz.question_number}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=f"{q_text}")
        else:
            self.canvas.itemconfig(self.question_text, text="You reached to the end of questions")
            self.btn_true.configure(state='disabled')
            self.btn_false.configure(state='disabled')

    def true_pressed(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.configure(bg="green")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, self.get_next_question)


