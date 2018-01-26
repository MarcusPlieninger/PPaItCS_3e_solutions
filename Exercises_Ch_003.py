#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 3: Computing with Numbers
#### End-of-Chapter Exercises

### REVIEW QUESTIONS

## True/False

#  1. Information that is stored and manipulated by computers is called data. TRUE
#     [Explanation: p.57 "The information that is stored an amnipulated by computer program is
#     gneerically rferred to as data. Different kinds of data will be stored and manipulated in
#     different ways."

#  2. Since floating-point numbers are extremely accurate, they generally be used instead of ints. FALSE
#     [Explanation: p.59 "Another difference between ints and floats is hat the float type can only
#     represent approximations of real numbers. As we will see, there is a limit to the precision, or
#     accuracy of the stored values. Since float values are not exact, while ints always are, your general
#     rule of thumb should be: If you don't need fractional values, use an int.]

#  3. Operations like addition and subtraction are defined in the math library. FALSE
#     [Explanaiton: p.60, see table of built-in numeric operations in Python. These include addition,
#     subtraction, multiplication, float division, exponentiation, absolute value, integer division,
#     and remainder.]

#  4. The number of possible arrangements of n items is equalt to n!. TRUE
#     [Explanation: p.68 With 6 items, there are 720 different ways of ordering them, i.e. 6!.

#  5. The sqrt function computes the squirt of a number. FALSE
#     [Explanation: The sqrt function computes the square root of a number.]

#  6. The float data type is identical to the mathematical concept of a real number. FALSE
#     [Explanation: Floats are approximations of real numbers. See p.59: "Another difference between ints
#     and floats is that the float type can only represent approximations to real numbers." This has to
#     do with how floats are stored. See p.74 for explanation. Be able to explain this in-depth and simply.]

#  7. Computers represent numbers using base-2 (binary) representations. TRUE
#     [Explanation: p.72-3 "Computer memory is composed of electrical 'switches,' each of which can be
#     in one of two possible states, basically on or off. Each switch represents a binary digit or bit
#     of information. One bit can encode two possibilities, usually represented with the numberals 0 (for off)
#     and 1 (for on)."

#  8. A hardware float can represent a larger range of values than a hardware int. TRUE
#     [Explanation: p.74 "Using a float allows us to represent a much larger range of values than a 32-bit
#     int, but the amoutn of precision is still fixed."]

#  9. Type conversion functions such as float are a safe alternative to eval for getting a number
#     as user input. TRUE
#     [Explanation: p. 65 "Using int instead of eval in the input statements ensures that a user may
#     only enter valid whole numbers. Any illegal (non-int) inputs will cause the program to crash with
#     an erro message, thus avoiding the risk of a code injection attack...."]

# 10. In Python, 4+5 produces the same result type as 4.0+5.0. FALSE
#     [Explanation: p.60 "Python chooses the appropriate underlyng operation (int or float) based on the
#     operands."]

## Multiple Choice

#  1. Which of these is not a built-in Python data type? [C]
#     a) int     b) float     c) rational     d) string
#     [Explanation: 

#  2. Which of the following is not a built-in operation? [D]
#     a) +     b) %     c) abs()     d) sqrt()
#     [Explnaation: sqrt() "lives" in the math library. See p.

#  3. In order to use functions in the math library, a program must include [D]
#     a) a comment     b) a loop     c) an operator     d) an import statement
#     [Explanation

#  4. The value of 4! is [B]
#     a) 9     b) 24     c) 41     d) 129
#     [Explanation: 4 * 3 * 2 * 1 = 24

#  5. The most appropriate data type for storing the value of pi is [B]
#     a) int     b) float     c) irrational     d) string
#     [Explanation:

#  6. The number of distinct values that can be represented using 5 bits is [C]
#     a) 5     b) 10     c) 32     d) 50
#     [Explanation: p.73: "In general, n bits can represent 2^n different values."]

#  7. In a mixed-type expression involving ints and floats, Python will convert [C]
#     a) floats to ints                    b) ints to strings
#     b) both floats and intos to strings  c) ints to floats
#     [Explanation: p.62-3: "In general, converating a float to an int is a dangerous step, because
#     some information (the fractional part) will be lost. On the other hand, an int can be safely
#     tunred into a float just by adding a fractional part of .0. So in mixed-type expressions, Python
#     will automatically convert ints to floats and perform floating-point operations to produce
#     a float result."]

#  8. Which of the following is not a Python type-conversion function? [B]
#     a) float     b) round     c) int     d) abs
#     [Explanation: p.60: abs is a built-in numberic operator that returns the absolute value. This is not
#     type-conversion. p.75: "Programs may explicitly convert one data type into another using the functions
#     float(), int(), and round()."]

#  9. The pattern used to compute factorials is [A]
#     a) accumulator         b) input, process, output
#     c) breaks the computer d) uses more memory
#     [Explanation: p.69: "Now let's try to think to think about the algorithm [to take a factorial of a number]
#     more generally. What is actually goin on here? We are doing repeated multipliations, and as we go along,
#     we keep track of the running product. This is a very common algorithmic pattern called an accumulator. We
#     build up, or accumulate, a final value piece by pice. To accomplish this in a program, we will use an
#     accumulator variable and a loop structure."]

# 10. In modern Python, an int value that grows larger than the underlying hardware int [D]
#     a) causes an overflow     b) converts to float
#     c) breaks the computer    d) uses more memory
#     [Explanation: p.74-5: A Python int is not a fixed size, but expands to accomodate whatever value it holds. The
#     only limit is the amount of memory the computer has available to it. When the value is small, Python can just use
#     the computer's underlying int representation and operations. When the value gets larger, Python automatically converts
#     to a represetnation using more bits. Of course, in order to perform operations on larger numbers, Python has to break
#     down the operations into smaller units that the computer hardware is able to handle--similar to the way you might do
#     long division by hand. These operations will not be as efficient (they requrie more steps), but they allow our Python
#     ints to grow to arbitrary size."]

## Discussion

#  1. Show the result of evaluating each expression. Be sure that the value is in the proper form to indicate its type (int
#     or float). If the expression is illegal, explain way.
#     a) 4.0 / 10.0 + 3.5 * 2
#     b) 10 % 4 + 6 / 2
#     c) abs(4 - 20) // 3) ** 3
#     d) sqrt(4.5 - 5.0) + 7 * 3
#     e) 3 + 10 // 3 + 10 % 3
#     f) 3 ** 3

#  2. Translate each of the following mathematical expressions into an equivalent Python expression. You may assume that the math
#     library has been imported (via import math).
#     a) (3 + 4)(5)
#     b) (n(n-1))/2
#     c) 4pir^2
#     d) sqrt(r(cosa)^2 + r(sinb)^2)
#     e) (y2 - y1) / (x2 - x1)

#  3. Show the sequence of numbers that would be generated by each of the following range expressions.
#     a) range(5)
#     b) range(3,5)
#     c) range(4,13,3)
#     d) range(15,5,-2)
#     e) range(5,3)
 
#  4. Show the output that would be generated by each of the following program fragments.
#     a) for i in range(1,11):
#            print(i*i)
#
#     b) for i in [1,3,5,7,9]:
#            print(i, ":", i**3)
#        print(i)   
#
#     c) x = 2
#        y = 10
#        for j in range(0, y, x):
#            print(j, end="")
#            print(x + y)
#       print("done")

#     d) ans = 0
#        for i in range(1,11):
#            ans = ans + i*i
#            print(i)
#        print(ans)

#  5. What do you think will happen if you use a negative number as the second parameter in the round function? For example, what
#     should be the result of round(314.159265, -1)? Explain the rational for your answer. After you've written your answer, consult
#     the Python documentation or try out some examples to see what Python actually does in this case.

#  6. What do you think will happen when the operands to the integer division or remainder operations are negative? Consider each of the
#     following cases and try to predict the results. Then try them out in Python.
#     Hint: Recall the magic formula a = (a//b)(b) + (a%b).
#     a) -10 // 3
#     b) -10 % 3
#     c) 10 // -3
#     d) 10 % -3
#     e) -10 // -3


### PROGRAMMING EXERCISES

#  1. Write a program to calculate the volume and surface area of a sphere from its radius, given as input. Here are some formulas that might
#     be useful:
#     V = (4/3)3pir^3
#     A = 4pir^2

#  2. Write a program that calculates the cost per square inch of a circular pizze, given its diameter and price. The formula for area is
#     A = pir^2.

#  3. Write a program that computes the molecular weight of a carbohydrate (in grams per mole) based on the number of hydrogen, carbon, and
#     oxygen atoms in the molecule. The program should prompt the user to enter the number of hydrogen atomes, the number of carbon atoms,
#     and the number of oxygen atoms. The program then prints the total combined molecular weight of all the atoms based on these individual
#     atom weights:
#                  Atom      Weight
#                            (grams/mole)
#                  ______________________
#                  H         1.00894
#                  C         12.0107
#                  O         15.9994
#     For example, the molecular weight of water (H20) is 2(1.00794) + 15.9994 = 18.01528.

#  4. Write a program that determines the distance to a lightning strike based on the time elapsed between the flash and the sound of thunder.
#     The speed of sound is approximately 1100 ft/sec and 1 mile is 5280 ft.

#  5. The Konidtorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $.086 per pound + $1.50 fixed cost
#     for overhead. Write a program that calculates the cost of an order.

#  6. Two points in a plane are specified using the coordinates (x1,y1) and (x2,y2). Write a program that calculates the slope of a line through
#     two (non-vertical) points entered by the user.
#                                                   slope = (y2 - y1) / (x2 - x1)

#  7. Write a program that accepts two points (see previous problem) and determins the distance between them.
#     distances = sqrt((x2-x1)^2 + (y2-y1)^2)

#  8. The Gregorian epact is the number of days between Janaury 1st and the previous new moon. This value is used to figure out the date of Easter.
#     It is calculated by these formulas (using int arithmetic):
#                                                               C = year//100
#                                                               epact = (8 + (C//4) - C + ((8C + 13)//25) + 11(year%19))%30

#  9. Write a program to calcualte the area of a triangle given the length of its three sides--a, b, and c--using these formulas:
#                                         s = (a + b + c) / 2
#                                         A = sqrt(s(s - a)(s - b)(s - c))
#     
# 10. Write a program to determine the length of a ladder required to reach a given height when leaned against a house. The height and angle of the
#     ladder are given as inputs. To compute length use:
#                                                       length = height / sin angle
#     Note: The angle must be in radians. Prompt for an angle in degrees and use this formula to convert:
#                                                       radians = (pi / 180) degrees

# 11. Write a program to find the first n natural numbers, where the value of n is provided by the user.

# 12. Write a program to find the sum of the cubes of the first n natural numbers where the value of n is provided by the user.

# 13. Write a program to sum a series of numbers entered by the user. The program should first prompt the user for how many numbers are to be summed.
#     The program should then prompt the user for each of the numbers in turn and print out a total sum after all the numbers have been entered.
#     Hint: Use an input statement in the body of the loop.

# 14. Write a program that finds the average of a series of numbers entered by the user. As in the previous problem, the program will first ask the
#     user how many numbers there are. Note: The average should always be a float, even if the user inputs are all ints.

# 15. Write a program tha approximates the value of pi by summing the terms of this series:
#     4/1 - 4/3 + 4/5 = 4/7 + 4/9 - 4/11 + ...
#     The program should prompt the user for n, the number of terms to sum, and then output the sum of the first n terms of this series. Have your
#     program subtrac the approximation from the value of math.pi to see how accurate it is.

# 16. A Fibnoacci sequence is a sequence of numbers where each successive number is the sum of the previous two. The classic Fibonacii sequence
#     begins: 1, 1, 2, 3, 5, 8, 13 ... . Write a program that computes the nth Fibonacci number where n is a value input by the user. For example,
#     if n = 6, then the result is 8.

# 17. You have seen that the math library contains a function that computes the square root of numbers. In this exercise, you are to write your own
#     algorithm for computing square roots. One way to solve this problem is to use a guess-and-check approach. You first guess what the square root
#     might be, and then you see how close your guess is. You can use this information to make another guess and continue guessing until you have
#     found the square root (or a close approximation to it). One particularly good way of making guesses is to use Newton's method.
#     Suppose x is the number we want the root of, and guess is the current guessed answer.
#     The guess can be improved by using computing the next guess as:
#                                                                    (guess + (x / guess)) / 2.
#     Write a program that implements Newton's method. The program should prompt the user for the value to find the square root of (x) and the
#     number of times to improve the guess. Starting with a guess value of x/2, your program should loop the specified number of times applying Newton's
#     method and report the final value of guess. You should also subtract your estimate from the value of math.sqrt(x) to show how close it is.


