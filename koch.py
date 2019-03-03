import turtle
t=turtle.Turtle()
height=800
width=600
turtle.setup(width,height)
t.penup()
t.backward(width/2)
#t.forward(100)
def koch(t,order,size):
    if order==0:
        t.forward(size)
    else:
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)
        t.right(120)
        koch(t,order-1,size/3)
        t.left(60)
        koch(t,order-1,size/3)

t.pendown()
t.color("blue")
t.pensize(8)
koch(t,3,600)
turtle.done()
