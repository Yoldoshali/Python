from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("highest_score.txt") as score:
            self.highest_score = int(score.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 265)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}   High Score:{self.highest_score}", align=ALIGNMENT, font=FONT)

    def refresh_score(self):
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.highest_score:
            self.highest_score = self.score
            with open("highest_score.txt", mode="w") as file2:
                file2.write(str(self.highest_score))
        self.score = 0
        self.update_scoreboard()
