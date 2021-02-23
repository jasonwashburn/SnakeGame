from turtle import Screen
import time
from snake import Snake

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')

# Turn off screen refreshing so we can control the animation
screen.tracer(0)

# Create the snake
snake = Snake()

# Start listening for key presses
screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.right, 'Right')
screen.onkey(snake.left, 'Left')

game_is_on = True

# Start our game loop
while game_is_on:
    # Update the screen, wait 0.1s and move the snake
    screen.update()
    time.sleep(0.1)
    snake.move()


screen.exitonclick()
