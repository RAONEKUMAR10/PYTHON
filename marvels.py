



# # STAR
import turtle
turtle.bgcolor('black')
star= turtle.Turtle()
star.pensize(10)
star.color('red','black')
star.begin_fill()
star.left(65)
star.forward(200)
star.right(125)
star.forward(200)
star.right(145)
star.forward(240)
star.right(155)
star.forward(240)
star.right(152)
star.forward(232)
star.end_fill()
star.hideturtle()
turtle.done()





# # # 1) IRON MAN:
# import turtle
# turtle.bgcolor('black')

# piece1=[[(-40, 120), (-70, 260), (-130, 230), (-170, 200),
#          (-170, 100), (-160, 40), (-170, 10), (-150, -10),
#          (-140, 10), (-40, -20), (0, -20)],
#         [(0, -20), (40, -20), (140, 10), (150, -10), (170, 10),
#          (160, 40), (170, 100), (170, 200), (130, 230), (70, 260),
#          (40, 120), (0, 120)]]

# piece2=[[(-40, -30), (-50, -40), (-100, -46), (-130, -40), (-176, 0),
#          (-186, -30), (-186, -40), (-120, -170), (-110, -210),
#          (-80, -230), (-64, -210), (0, -210)],
#         [(0, -210), (64, -210),
#          (80, -230), (110, -210), (120, -170), (186, -40), (186, -30),
#          (176, 0), (130, -40), (100, -46), (50, -40), (40, -30), (0, -30)]]

# piece3=[[(-60, -220), (-80, -240), (-110, -220), (-120, -250),(-90, -280),
#          (-60, -260), (-30, -260), (-20, -250), (0, -250)],
#         [(0, -250), (20, -250),
#          (30, -260), (60, -260), (90, -280), (120, -250),(110, -220), (80, -240),
#          (60, -220), (0, -220)]]

# piece1goto = (0,120)
# piece2goto = (0,-30)
# piece3goto = (0,-220)

# def draw_piece(piece,piecegoto):
#     turtle.penup()
#     turtle.goto(piecegoto)
#     turtle.pendown()
#     turtle.color('red')
#     turtle.begin_fill()
#     for i in range(len(piece[0])):
#         x,y =piece[0][i]
#         turtle.goto(x,y)

#     for i in range(len(piece[1])):
#         x,y=piece[1][i]
#         turtle.goto(x,y)

#     turtle.end_fill()

# draw_piece(piece1,piece1goto)
# draw_piece(piece2,piece2goto)
# draw_piece(piece3,piece3goto)

# turtle.hideturtle()
# turtle.done()


# 2) CAPTAIN AMERICA SHIELD:
# import turtle

# def circle(radius,color):
#     turtle.color(color)
#     turtle.begin_fill()
#     turtle.circle(radius)
#     turtle.end_fill()
    
# turtle.goto(-30,-280)
# circle(300,'red')

# turtle.goto(-30,-240)
# circle(260,'white')

# turtle.goto(-30,-200)
# circle(220,'red')

# turtle.goto(-30,-160)
# circle(180,'blue')

# turtle.goto(-200,75)
# turtle.begin_fill()
# turtle.color('white')

# for i in range(5):
#     turtle.forward(340)
#     turtle.right(144)
# turtle.end_fill()

# turtle.hideturtle()
# turtle.done()


# # # 3) BATMAN LOGO:
# import turtle
# turtle.bgcolor('black')
# bat = turtle.Turtle()
# bat.pensize(4)
# bat.color('yellow','black')
# bat.begin_fill()

# bat.left(90)
# bat.circle(50,85)
# bat.circle(15,110)
# bat.right(180)
# bat.circle(30,150)
# bat.right(5)
# bat.forward(10)

# bat.right(90)
# bat.circle(-70,140)
# bat.forward(40)
# bat.right(110)
# bat.circle(100,30)
# bat.circle(30,100)
# bat.left(50)
# bat.forward(50)

# bat.right(145)
# bat.forward(30)
# bat.left(55)
# bat.forward(20)
# bat.left(55)
# bat.forward(30)
# bat.right(145)
# bat.forward(50)
# bat.left(50)

# bat.circle(30,100)
# bat.circle(100,30)
# bat.right(110)
# bat.forward(40)
# bat.circle(-70,140)
# bat.right(90)
# bat.forward(10)
# bat.right(5)
# bat.circle(30,150)
# bat.left(180)
# bat.circle(15,110)
# bat.circle(50,85)
# bat.end_fill()
# bat.hideturtle()
# turtle.done()
