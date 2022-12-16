from tkinter import *
from quiz_brain import QuizBrain


THEME_COLOR = "#375362"


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(pady=20, padx=20, background=THEME_COLOR)

        self.score_text = Label(text=f"Score: 0", bg=THEME_COLOR, fg="white",
                                font=("Ariel", 18))

        self.score_text.grid(column=1, row=0)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(150, 125,
                                                     width=280,
                                                     text="questions go here!!",
                                                     fill=THEME_COLOR,
                                                     font=("Arial", 20, "italic"))

        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        tick_image = PhotoImage(file="images/true.png")
        self.correct_button = Button(image=tick_image, highlightthickness=0, command=self.correct_answer)
        self.correct_button.grid(column=0, row=2)

        cross_image = PhotoImage(file="images/false.png")
        self.wrong_button = Button(image=cross_image, highlightthickness=0, command=self.wrong_answer)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_text.config(text=f"Score: {self.quiz.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="No more questions")
            self.correct_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def correct_answer(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_answer(self):
        is_right = self.quiz.check_answer("False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.window.after(1000, self.get_next_question)
        else:
            self.canvas.config(bg="red")
            self.window.after(1000, self.get_next_question)




