from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score= int(data.read())
        self.color('white')
        self.penup()
        self.goto(0,265)
        self.hideturtle()
        self.update_score()

    def reset_score(self):
        self.goto(0,265)

        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode='w') as data:
                data.write(f"{self.high_score}")
        self.score=0
        self.update_score()


    def update_score(self):
        self.goto(0,265)
        self.clear()
        self.write(f"Score: {self.score}  High Score :{self.high_score}"  , align="center", font=("Courier", 24, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("You Lost Press 'R' To restart",align="center",font=("Courier", 24, "normal"))