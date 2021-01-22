import turtle as turtle_module
import random


turtle_module.colormode(255)
t = turtle_module.Turtle()
t.speed("fastest")
t.penup()
t.hideturtle()

color_list = [
    (223, 224, 228),
    (167, 106, 56),
    (186, 159, 52),
    (6, 57, 83),
    (108, 68, 85),
    (112, 161, 175),
    (21, 122, 174),
    (63, 153, 138),
    (39, 36, 35),
    (76, 40, 48),
    (9, 68, 47),
    (90, 141, 52),
    (182, 96, 79),
    (131, 38, 41),
    (141, 171, 156),
    (210, 200, 149),
    (179, 201, 186),
    (173, 153, 159),
    (212, 183, 176),
    (151, 114, 119),
    (177, 198, 203),
    (206, 184, 190),
    (37, 73, 84),
    (45, 74, 63),
    (48, 66, 80)
]

#  Set first dot position
t.setheading(225)
t.forward(300)
#  Set heading back to 0 to move horizontally
t.setheading(0)

number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    t.dot(20, random.choice(color_list))
    t.forward(50)

    # If its multiple of 10 then we reach the end of the line
    if dot_count % 10 == 0:
        # Turn up
        t.setheading(90)
        # Move up
        t.forward(50)
        #  Turn left
        t.setheading(180)
        # Move forward by 500 to end up at start position
        t.forward(500)
        # Turn right to go back and create dots
        t.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()


# Get colors from image
import colorgram
# rgb_colors = []
# colors = colorgram.extract('hirst.jpg', 30)
#
# for color in colors:
#
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
