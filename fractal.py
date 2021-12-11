import turtle as tu

roo = tu.Turtle()  
wn = tu.Screen()  
wn.bgcolor("black")  
wn.title("Fractal Tree Pattern")
roo.left(90)  
roo.speed(50)  
roo.pensize(2)  


def draw(l,color,bo1,bo2):
    if (l < 10):
        return
    else:
        roo.pencolor(color)  
        roo.forward(l)  
        roo.left(30) 
        draw(bo1 * l / bo2,color,bo1,bo2)  
        roo.right(60)  
        draw(bo1 * l / bo2,color,bo1,bo2) 
        roo.left(30)  
        roo.backward(l)  


draw(20,"yellow",3,4)
roo.right(90)
draw(20,"green",3,4)
roo.left(270)
draw(20,"red",3,4)
roo.right(90)
draw(20,'white',3,4)

draw(40,"white",4,5)
roo.right(90)
draw(40,"red",4,5)
roo.left(270)
draw(40,"green",4,5)
roo.right(90)
draw(40,'yellow',4,5)


wn.exitonclick()














































