import turtle
turtle.shape("turtle")

length=int(input("길이:"))

# turtle.forward(length*1)
# turtle.right(45)
# turtle.forward(length*2)
# turtle.right(45)
# turtle.forward(length*4)
# turtle.right(45)
# turtle.forward(length*8)
# turtle.right(45)
# turtle.forward(length*16)
# turtle.right(45)


for i in range(5):
    s=2**i
    turtle.forward(length*s)
    turtle.right(45)

turtle.done()