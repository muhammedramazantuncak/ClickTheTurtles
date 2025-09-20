import turtle
from random import randint
from random import shuffle


# Ekran Oluşturma

screen = turtle.Screen()
screen_color_list = ["#3090C7","#98AFC7","#66CDAA","#32CD32","#ADF802","#9F8C76","#A70D2A","#7E354D","#FC6C85","#9E7BFF","#FFFFFF"]
shuffle(screen_color_list)
screen.bgcolor(screen_color_list[randint(0,len(screen_color_list)-1)])
screen.title("Click The Turtle")
screen.tracer(0) # animasyonları kapatır


# Zamanlayıcı Oluşturma

pen1 = turtle.Turtle()
pen1.hideturtle()
pen1.pensize(3)
pen1.color("black")
pen1.speed(0)


style = ("Courier",30,"bold italic")
timer = 30
starting_game = 5

def startgame():
    global starting_game
    pen1.penup()
    pen1.goto(0, 380)
    pen1.pendown()
    pen1.clear()
    if starting_game > 0:
        pen1.write(f"Game is about to start | Get ready : {starting_game}",font=style,align="center")
        starting_game -= 1
        screen.ontimer(startgame,1000)
    else:
        countdown()
        appearcircle()

def countdown():
    global timer
    shufflecolorlist()
    pen1.penup()
    pen1.goto(0,380)
    pen1.pendown()
    pen1.clear()
    if timer > 0:
        pen1.write(f"Catch the Turtle : {timer}",font=style,align="center")
        timer -= 1
        screen.ontimer(countdown,1000)
    else:
        timeup()

def timeup():
    global timer
    if timer == 0:
        pen1.penup()
        pen1.goto(0, 380)
        pen1.pendown()
        pen1.clear()
        pen1.write("Time Is Up !!!" , font=style, align="center")


# Renkli Daire Oluşturma

pen2 = turtle.Turtle()
pen2.hideturtle()
r1 = 30
pen3 = turtle.Turtle()
pen3.hideturtle()
r2 = 40
index = 0
random_color_list = ["black", "red", "blue", "green", "purple"]

def shufflecolorlist():
    global timer
    for c in range(timer):
        shuffle(random_color_list)

def appearcircle():
    global timer , index
    if timer > 0:
        change_turtle()
        pen3.clear()
        pen3.penup()
        pen3.goto(0, 290)
        pen3.pendown()
        pen3.fillcolor("white")
        pen3.begin_fill()
        pen3.circle(r2)
        pen3.end_fill()
        pen2.clear()
        pen2.penup()
        pen2.goto(0,300)
        pen2.pendown()
        pen2.fillcolor(random_color_list[index])
        pen2.begin_fill()
        pen2.circle(r1)
        pen2.end_fill()
        for turt in turtles: # bu fonksiyonun içine yazraak her renk değiştiğinde tekrar kontrol edilmesini sağlıyoruz
            turt.onclick(None)
            if turt.fillcolor() == pen2.fillcolor():
                turt.onclick(click)
        index = (index + 1) % len(random_color_list)
        screen.update() # ekranı güncelleyerek kaplumbağların yerlerini değişmesini görebildik
        screen.ontimer(appearcircle,1000)

# Turtle'ları OLuşturma

x_list = list(range(-400,450,50))
y_list = list(range(-300,350,50))
y_list.remove(-300)
y_list.remove(300)

shuffle(x_list)
shuffle(y_list)

t_size = 2

t1 = turtle.Turtle()
t1.shape("turtle")
t1.shapesize(t_size)
t1.fillcolor("black")
t1.speed(6.5)

t2 = turtle.Turtle()
t2.shape("turtle")
t2.shapesize(t_size)
t2.fillcolor("blue")
t2.speed(6.5)

t3 = turtle.Turtle()
t3.shape("turtle")
t3.shapesize(t_size)
t3.fillcolor("red")
t3.speed(6.5)

t4 = turtle.Turtle()
t4.shape("turtle")
t4.shapesize(t_size)
t4.fillcolor("green")
t4.speed(6.5)

t5 = turtle.Turtle()
t5.shape("turtle")
t5.shapesize(t_size)
t5.fillcolor("purple")
t5.speed(6.5)

turtles = [t1,t2,t3,t4,t5]


def change_turtle():
    for t in turtles:
        t.penup()
        t.goto(x_list[randint(0,len(x_list)-1)],y_list[randint(0,len(y_list)-1)])


# Ekrana Tıklama Özelliği

pen4 = turtle.Turtle()
pen4.color("black")
style1 = ("Courier",20,"bold italic")
pen4.hideturtle()

written = 0

def click(_x,_y):
    global written , timer
    if timer > 0:
        written += 1
        pen4.clear()
        pen4.penup()
        pen4.goto(-650,385)
        pen4.pendown()
        pen4.write(f"Your Score : {written}",font=style1,align="center")


screen.update() # ekranı günceller , yaptıklarımızın gözükmesini sağlar
startgame()
screen.mainloop()


