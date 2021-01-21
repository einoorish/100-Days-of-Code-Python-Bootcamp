from turtle import Turtle, Screen
from time import sleep

MOVE_DISTANCE = 20

class Snake :

  def __init__(self):
    self.snake = []  
    self.add_initial_segments()
    

  def add_initial_segments(self):
    for i in range(0, 3) :
      segment = Turtle()
      segment.shape("square")
      segment.color("white")
      segment.penup()
      segment.goto(-20*i, 0)
      
      self.snake.append(segment)

  def move(self):
      for seg_num in range(len(self.snake)-1, 0, -1):
        new_x = self.snake[seg_num-1].xcor()
        new_y = self.snake[seg_num-1].ycor()
        self.snake[seg_num].goto(new_x, new_y)

      self.snake[0].forward(MOVE_DISTANCE)

  def turn_up(self):
    self.snake[0].setheading(90)

  def turn_down(self):
    self.snake[0].setheading(270)
  
  def turn_right(self):
    self.snake[0].setheading(0)

  def turn_left(self):
    self.snake[0].setheading(180)



screen = Screen()
screen.setup(width=500, height=500)
screen.bgcolor("black")
screen.tracer(0) # to remove animation
#screen.title("Snake Game")

snake = Snake()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True

while game_is_on:
  sleep(0.1)  #to slower the snake
  snake.move()

  screen.update()


screen.exitonclick()
