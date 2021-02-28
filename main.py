from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Turn off screen refreshing so we can control the animation
screen.tracer(0)

# Create the snake, food, and scoreboard
snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Start listening for key presses
screen.listen()
screen.onkey(snake.go_up, 'Up')
screen.onkey(snake.go_down, 'Down')
screen.onkey(snake.go_right, 'Right')
screen.onkey(snake.go_left, 'Left')

game_is_on = True

# Start our game loop
while game_is_on:
    # Update the screen, wait 0.1s and move the snake
    screen.update()
    time.sleep(0.1)
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:
        scoreboard.score += 1
        scoreboard.update_score()
        snake.extend()
        food.refresh()

    # Detect snake out of bounds on x-axis
    if (snake.head.xcor() > 280) or (snake.head.xcor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect snake out of bounds on y-axis
    if (snake.head.ycor() > 280) or (snake.head.ycor() < -280):
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()



screen.exitonclick()
