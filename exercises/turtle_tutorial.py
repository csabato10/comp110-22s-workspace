"""Gary the Pit Preacher Turtle."""

from random import randint
from turtle import Turtle, colormode, done
colormode(255)
leo: Turtle = Turtle()


def machine(leo: Turtle) -> None:
    leo.penup()
    leo.color("black")
    leo.goto(0, -40)
    leo.pendown()
    leo.circle(175)


def stand(leo: Turtle) -> None:
    leo.penup()
    leo.goto(-110, -150)
    leo.pendown()
    leo.color("red")
    leo.begin_fill()
    leo.forward(225)
    leo.left(100)
    leo.forward(150)
    leo.left(80)
    leo.forward(175)
    leo.left(80)
    leo.forward(150)
    leo.left(100)
    leo.end_fill()


def turner(leo: Turtle) -> None:
    leo.penup()
    leo.color("gray")
    leo.goto(10, -40)
    leo.pendown()
    leo.begin_fill()
    leo.circle(60)
    leo.end_fill()
    leo.penup()



def gumball(leo: Turtle, x: int, y: int, balls: int) -> None:
    i: int = 0
    leo.penup()
    leo.goto(x, y)
    while i < balls:
        leo.pendown()
        leo.color(randint(0, 200), randint(0, 200), randint(0, 200))
        leo.begin_fill()
        leo.circle(20)
        leo.end_fill()
        leo.penup()
        leo.forward(40)
        i += 1


def main() -> None:
    leo.speed(50)
    gumball(leo, -100, 50, 6)
    gumball(leo, -115, 90, 7)
    gumball(leo, -130, 130, 8)
    gumball(leo, -115, 170, 7)
    machine(leo)
    stand(leo)
    turner(leo)


if __name__ == "__main__":
    main()
    done()