from turtle import Turtle, Screen
import random

is_game_on = False
screen = Screen()
# jimmy = Turtle()
user_bet = screen.textinput(title= "Make your bet", prompt= "Which turtle will win the race? Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

# jimmy.penup()
# jimmy.shape("turtle")
# jimmy.goto(x= - 240, y= 0)

y = -100
for _ in range(6):
    turt = Turtle()
    turt.penup()
    turt.shape("turtle")
    turt.color(colors[_])
    y += 30
    turt.goto(x= -240, y= y)
    all_turtles.append(turt)

screen.setup(width =500, height=400)

if user_bet:
    is_game_on = True

while is_game_on:
    for turt in all_turtles:
        if turt.xcor() > 230:
            is_game_on = False
            winning_color = turt.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turt.forward(rand_distance)

screen.exitonclick()