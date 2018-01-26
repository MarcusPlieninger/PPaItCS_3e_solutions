#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 4: Objects and Graphics
#### End-of-Chapter Exercises

### REVIEW QUESTIONS

## True/False

#  1. Using graphics.py allows graphics to be drawn in a Python shell window. FALSE
#     [Explanation: p.86: "The GraphWin() function creates a new window on the screen....The GraphWin
#     may overlap your Python shell window, so you might have to resize or move the shell to make
#     both windows fully visible."]

#  2. Traditionally, the upper-left corner of a graphics window has coordinates (0,0). TRUE
#     [Explanation: p.88: "Traditionally, graphics programmers locate the point (0,0) in the upper-left
#     corner of the window,"]

#  3. A single point on a graphics screen is called a pixel. TRUE
#     [Explanation: p.88: "A graphics winow is actually a collection of tiny points called pixels
#     (short for 'picture elements')."]

#  4. A function that creates a new instance of a class is called an accessor. FALSE
#     [Explanation: p.91: "To create a new instance of a class, we use a special operation called a
#     constructor. A call to a constructor is an expression that creates a brand new object."
#     p.92: Methods that "allows us to access information from the instance variables of the object"
#     are called "accessors."]

#  5. Instance variables are used to store data inside an object. TRUE
#     [Explanation: p.92: Values are stored inside an object as instance variables.]

#  6. The statement myShape.move(10,20) moves myShape to the point (10,20). FALSE
#     [Explanation: p.93: Specification of move method that all graphical objects have:
#     "move(dx, dy): Moves the object dx units in the x direction and dy units in the y direction."
#     Thus, the coordinates indicate movement, not position.]

#  7. Aliasing occurs when two variables refer to the same object. TRUE
#     [Explanation: p.95: "This situation where two vairabiles refer to the same object is called
#     aliasing."]

#  8. The copy method is provided to make a copy of a graphics object. FALSE
#     [Explanation: p.95: "The graphics library provides a better solution; all graphical objects support
#     a clone method that makes a copy of the object."]

#  9. A graphics window always has the title "Graphics Window." FALSE
#     [Explanation: p.98: "...the GraphWin constructor allows an optional parameter to specify the title
#     of the window."]

# 10. The method in the graphics library used to get a mouse click is readMouse. FALSE
#     [Explanation: p.107: "When getMouse is invoked on a GraphWin, the program pauses and waits for the
#     user to click the mouse somewhere in the graphics window."


## Multiple Choice

#  1. A method that returns the value of an ojbect's instance variable is called a(n) [D]
#     a) mutator     b) function     c) constructor     d) accessor

#  2. A method that changes the state of an object is called a(n) [B]
#     a) stator     b) mutator     c) constructor     d) changor

#  3. What graphics class would be best for drawing a square?
#     a) Square     b) Polygon     c) Line     d) Rectangle

#  4. What command would set the coordiantes of win to go from (0,0) in the lower-left corner to (10,10) in the
#     upper-right?

#  5. What expression would create a line from (2,3) to (4,5)?

#  6. What command would be sued to draw the graphics object shape into the graphics window win?

#  7. Which of the following computes the horizontal distance between points p1 and p2?

#  8. What kind of ojbect can be used to get text input in a graphics window?

#  9. A user interface organized around visual elements and user actions is called a(n)

# 10. What color is color_rgb(0,255,255)?


## Discussion

#  1. Pick an example of an interesting real-world object and describe it as a programming object by listing its
#     data (attributes, what it "knows") and its methods (behaviors, what it can "do").

#  2. Describe in your own words the object produced by each of the following operations from the graphics module.
#     Be as precise as you can. Be sure to mention such things as the size, position, and appearance of the various
#     objects. You may include a sketch if that helps.
#
#     a) Point(130, 130)
#        Constructs a point at x coordinate 130 and y coordinate 130, with 0,0 being located at upper left hand corner.
#
#     b) c = Circle(Point(30,40), 25)
#        c.setFill("blue")
#        c.setOutline("red")
#
#     c) r = Rectangle(Point(20,20), Point(40,40))
#        r.setFill(color_rgb(0,255,150)
#        r.setWidth(3)
#
#     d) l = Line(Point(100,100), Point(100,200))
#        l.setOutline("red4")
#        l.setArrow("first")

#     e) Oval(Point(50,50), Point(60,100))

#     f) shape = Polygon(Point(5,5), Point(10,10), Point(5,10), Point(10,5))
#        shape.setFill("orange")

#     g) t = Text(Point(100,100), "Hello World!")
#        t.setFace("courier")
#        t.setSize(16)
#        t.setStyle("italic")

#  3.  Describe what happens when the following interactive graphics program runs:
#
       from graphics import *
#
       def main():                          # Defines the function named main() (i.e., the program)
           win = GraphWin()                 # Openstucts GraphWin object with "Graphics Window" default title and default size 200 x 200 pixels
           shape = Circle(Point(50,50), 20) # Constructs a circle object with center Point object at 50,50 and radius of 20 pixels
           shape.setOutline("red")          # Calls setOutline method of circle object named shape, seting its outline to the color red
           shape.setFill("red")             # Calls setFill method of circle object shape, it fills itself with the color red
           shape.draw(win)                  # Calls draw method of circle object named shape, it draws itself in graphics window object named win
           for i in range(10):              # Creates a counted loop that will iterate 10 times
               p = win.getMouse()           # Calls getMouse() method of graphics window object win, pauses program for user to click in win, returns mouse click as Point object,
                                            # which is assigned to the variable p (an event object)
               c = shape.getCenter()        # Calls getCenter() method of circle object shape, returns a clone of the center point of shape
               dx = p.getX() - c.getX()     # Assignment statement whereby variable dx is assigned the expression in the getX() methods of p and c are used to calculate the
                                            # difference along the x axis of the user's mouse click with respect to the center point of shape
               dy = p.getY() - c.get&()     # Assignment statement whereby variable dy is assigned a similar expression as dx, except this time it is for the Y axis
               shape.move(dx, dy)           # Calls the move() method of shape to move shape by the x distance referred to by dx and the y distance referred to by dy, thus
                                            # changing the state of shape by moving its center point to the new coordinates encapsulated in the event object p
          win.close()                       # Calls close() method of graphics window object named, closing the graphics window after the loop is finished.
                                            # Note that it will not be possible to see the final location of the circle. To do so, comment out win.close() or call on win's
                                            # getMouse() method to make win close after a mouse click.
       main()                               # Calls the function named main() (i.e., the program).


### PROGRAMMING EXERCISES

#  1. Alter the program from the last discussion question in the following ways:
#     a) Make it draw squares instead of circles.
#        Delete:
         shape = Circle(Point(50,50), 20)
#        Replace:
         shape = Rectangle(Point(30,70), Point(70,30))
#     b) Have each sucessive click draw an additional square on the screen (rather than moving the existing one).
#        Delete:
         shape.move(dx, dy)
#        Replace:
         newshape = shape.clone()
         newshape.move(dx,dy)
         newshape.draw()
#     c) Print a message on the window "Click again to quit" after the loop, and wait for a final click before closing the window.
#        Insert immediately before win.close():
         quitmessage = Text(Point(100,100), "Click again to quit")
         quitmessage.setSize(18)
         quitmessage.setStyle("bold")
         quitmessage.setTextColor("blue")
         quitmessage.draw(win)
         win.getMouse()

#  2. An archery target consists of a central circle of yellow surrounded by concentric rings of red, bue, black and white. Each
#     ring has the same width, which is the same as the radius of the yellow circle. Write a program that draws such a target.
#     Hint: Objects drawn later will appear on top of objects drawn earlier.

#     Note: Add text here about algorithm design

#     target.py
#     A program to draw a target of any size and any number of rings of different color.

      from graphics import *

      def main():
        squareside= 200 # single point of control that allows resizing of target
        r = (squareside / 2)
        center = Point((squareside / 2),(squareside/ 2))
        color = ["white", "black", "blue", "red", "yellow", "green"] # use this list to add or delete colors for simpler or more complex targets

        win = GraphWin("Ready, Aim, Fire!", squareside, squareside)

        for i in range(len(color)): # len() is used so that a target of any number of circles can be drawn

            aim = Circle(center, r - (r * (i / len(color)))) # len(0 is used to get the proportion of part to whole
            aim.setFill(color[i])
            aim.draw(win)

      main()

#    Another idea for a solution: Is it possible to pass a decision structure (e.g., ifelif statement) as a parameter to Point method?
#    If so, this could be implemented for the different colors, which would obviate need for list. But, I think the current solution
#    is the cleanest. Also, passing a decision structure as a parameter could be more appropriate to functional programming. Need to
#    research that.


#  3. Write a program that draws some sort of face.

#  4. Write a program that draws a winter scene with a Cristmas tree and a snowman.

#  5. Write a program that draws 5 dice on the screen depicting a straight (1,2,3,4,5 or 2,3,4,5,6).

#  6. Modify the graphical future value program so that the input (principal and APR) also are done in a graphical fashion using
#     Entry objects.

#  7. Circle Intersection.
#     Write a program that computes the intersection of a circle with a horizontal line and displays the information textually and graphically.
#     Input: Radius of the circle and the y-intercept of the line.
#     Output: Draw a circle centered at (0,0) with teh given radius in a window with coordinates running from -10,-10 to 10,10.
#     Draw a horizontal line across the window and the given-y intercept.
#     Draw the two points of intersection in red.
#     Print out the x values of the points of intersection.
#     Formula: x = + or -(sqrt((r^2 = y^2)))

#  8. Line Segment Information.
#     This program allows the suer to draw a line segment that then displays some graphical and textual information about the line segment.
#     Input: Two mouse clicks for the end points of the line segment.
#     Output: Draw the midpoint of the segment in cyan.
#             Draw the line.
#             Print the length and the slope of the line.
#     Formulas: dx = x2 - x1
#               dy = y2 - y1
#               slope = dy / dx
#               length = sqrt(dx^2 + dy^2)
 
#  9. Rectangle Information.
#     This program displays information about a rectangle drawn by the user.
#     Input: Two mouse clicks for the opposite corners of a rectangle.
#     Output: Draw the rectangle.
#             Print the perimeter and area of the rectangle.
#     Formulas: area = (length)(width)
#               perimeter = 2(length + width)

# 10. Triangle Information.
#     Same as the previous problem, but with three clicks for the vertices of the triangle.
#     Formulas: For perimeter, see length fromt he Line Segment problem.
#               area = sqrt(s(s - a)(s - b)(s - c)) where a, b, and c are the lengths of the sides and s = (a + b + c) / 2.
     
# 11. Five-click House.
#     You are to write a program that allows the user to draw a simple house using five mouse clicks. The fisrt two clicks will be the opposite
#     corners of the rectangular frame of the house. The third click will indicate the center of the otp ege of a rectangular door. The door should
#     have a total width that is 1/5 the wdith of the house frame. The sides of the door should have extend from the corners of the top down to the
#     bottom of the frame. The fourth click will indicate the center of a square window. The window is half as wide as the door. The last click will
#     indicate the peak of the roof. The edges of the roof will extend from the point at the peak to the corners of the top edge of the house frame.







