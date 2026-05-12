import turtle

def rewrite(axiom, rules, iterations):
    current = axiom

    for i in range(iterations):
        next_string = "" # resets each iteration
        for char in current:
            next_string += rules.get(char, char) # passthrough if no rule
        current = next_string # swap for next iteration
    
    return current

def render_with_branches(lstring, step_size, angle):
    screen = turtle.Screen()
    screen.bgcolor("white")
    screen.tracer(0) # batch render

    t = turtle.Turtle()
    t.hideturtle()
    t.left(90) # face upwards
    stack = [] # empty stack

    for char in lstring:
        if char == "F" or char == "G":
            t.forward(step_size)
        elif char == "+":
            t.right(angle)
        elif char == "-":
            t.left(angle)
        elif char == "[":
            state = (t.pos(), t.heading())
            stack.append(state)
        elif char == "]":
            pos, hdg = stack.pop()
            t.penup()
            t.setpos(pos)
            t.setheading(hdg)
            t.pendown()
        elif char == "X":
            t.penup()
            t.forward(step_size)
            t.pendown
    
    screen.update()
    screen.mainloop

    turtle.done()

axiom = "F"
rules = {
    "F": "",
    "G": "",
    "X": ""
    }
iterations = 5
step = 5
angle = 60

lstring = rewrite(axiom, rules, iterations)
render_with_branches(lstring, step, angle)
