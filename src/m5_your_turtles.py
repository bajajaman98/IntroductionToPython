"""
Your chance to explore Loops and Turtles!

Authors: David Mutchler, Dave Fisher, Valerie Galluzzi, Amanda Stouder,
         their colleagues and Aman Bajaj.
"""
########################################################################
# DONE: 1.
# On Line 5 above, replace  PUT_YOUR_NAME_HERE  with your own name.
########################################################################

########################################################################
# DONE: 2.
#
#  You should have RUN the PREVIOUS module and READ its code.
#  (Do so now if you have not already done so.)
#
#  Below this comment, add ANY CODE THAT YOUR WANT, as long as:
#    1. You construct at least 2 rg.SimpleTurtle objects.
#    2. Each rg.SimpleTurtle object draws something
#         (by moving, using its rg.Pen).  ANYTHING is fine!
#    3. Each rg.SimpleTurtle moves inside a LOOP.
#
#  Be creative!  Strive for way-cool pictures!  Abstract pictures rule!
#
#  If you make syntax (notational) errors, no worries -- get help
#  fixing them at either this session OR at the NEXT session.
#
#  Don't forget to COMMIT your work by using  VCS ~ Commit and Push.
########################################################################
import rosegraphics as rg
window = rg.TurtleWindow

blue_turtle = rg.SimpleTurtle('turtle')
blue_turtle.pen = rg.Pen('blue',10)
blue_turtle.speed = 10
circle_size = 250
blue_turtle.pen_up()
blue_turtle.go_to(rg.Point(0,-200))
blue_turtle.pen_down()

red_turtle = rg.SimpleTurtle('turtle')
red_turtle.pen = rg.Pen('red',5)
red_turtle.speed = 5
square_size = 50
red_turtle.pen_up()
red_turtle.go_to(rg.Point(-15,-165))
red_turtle.pen_down()
for k in range(10):

    blue_turtle.draw_circle(circle_size)
    circle_size -= 20
    red_turtle.draw_square(square_size)
    red_turtle.pen_up()
    red_turtle.right(90)
    red_turtle.backward(30)
    red_turtle.pen_down()

window.close_on_mouse_click()