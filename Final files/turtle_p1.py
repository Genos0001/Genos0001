import turtle, time
t = turtle.Turtle()
s = turtle.Screen()
def screen():
    s.setup(800,600)
    s.title('Python Turtle Graphics')
    s.bgcolor('black')
    t.pencolor('white')
    t.speed(0)
    t.penup()
    t.goto(0,50)
    t.pendown()
    t.hideturtle()
    t.pensize(2)
    t.speed(2)
screen()

r = 'Enter the number for the shape you want to draw: \n1. Square\n2. Triangle\n3. Circle\n4. Star\n5. Hexagon\n6. Octagon\n7. Exit\n'
p= 2

def write(text):
    t.write(text, align='center', font=('Arial', 16, 'bold'))
    
def square():
    for i in range(4):
        t.forward(100)
        t.right(90)

def triangle():
    for i in range(3):
        t.forward(100)
        t.right(120)

def circle():
    t.circle(100)

def star():
    for i in range(5):
        t.forward(100)
        t.right(144)

def hexagon():
    for i in range(6):
        t.forward(100)
        t.right(60)
        
def octagon():
    for i in range(8):
        t.forward(100)
        t.right(45)

def gui():
    t.penup()
    t.goto(0, 200)
    t.pendown()
    write('Select the shape you want to draw')
    t.penup()
    t.goto(0,0)
    t.pendown()
    shape = s.textinput('Shape', 'Enter the number for the shape you want to draw: \n1. Square\n2. Triangle\n3. Circle\n4. Star\n5. Hexagon\n6. Octagon\n7. Exit\n')
    if shape == '1':
        square()
    elif shape == '2':
        triangle()
    elif shape == '3':
        circle()
    elif shape == '4':
        star()
    elif shape == '5':
        hexagon()
    elif shape == '6':
        octagon()
    elif shape == '7':
        t.clear()
        write('Thank You')
    else:
        t.goto(50,0)
        write('Invalid Input')
        time.sleep(2)
        t.terminator()
        gui()
    time.sleep(2)
    t.clear()
    gui()
    
gui()

s.mainloop()
