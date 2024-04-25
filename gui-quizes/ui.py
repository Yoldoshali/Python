from tkinter import *
from quiz_brain import QuizBrain
THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz_brain: QuizBrain):

        self.score = 0
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.config(padx=50, pady=50, bg=THEME_COLOR)
        self.window.minsize(width=340, height=400)

        self.label = Label(text=f"Score: ", fg="white", bg=THEME_COLOR, font=("Arial", 20, "italic"))
        self.label.grid(row=0, column=1)
        self.canvas = Canvas(width=300, height=250)
        self.text = self.canvas.create_text(150, 120, width=280, font=("Arial", 20, "italic"))
        self.canvas.grid(column=0, row=1, columnspan=2, pady=50)

        right_image = PhotoImage(file='./images/true.png')
        self.right_button = Button(image=right_image, command=self.right_button, highlightthickness=0)
        self.right_button.config(padx=10, pady=10)
        self.right_button.grid(column=0, row=2)

        wrong_image = PhotoImage(file='./images/false.png')
        self.wrong_button = Button(image=wrong_image, command=self.wrong_button, highlightthickness=0)
        self.wrong_button.grid(column=1, row=2)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.text, text=q_text)
            self.canvas.configure(bg="white")
        else:
            self.canvas.itemconfig(self.text, text=f"Game is Over."
                                                   f" You got {self.score} / {len(self.quiz.question_list)}")
            self.canvas.configure(bg="yellow")
            self.right_button.config(state="disabled")
            self.wrong_button.config(state="disabled")

    def right_button(self):
        self.give_feedback(self.quiz.check_answer("True"))

    def wrong_button(self):
        self.give_feedback(self.quiz.check_answer("False"))

    def give_feedback(self, is_right):
        if is_right:
            self.score += 1
            self.canvas.configure(bg="green")
            self.label.config(text=f"Score:{self.score}")
        else:
            self.canvas.configure(bg="red")
        self.window.after(1000, func=self.get_next_question)

