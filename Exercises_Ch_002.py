#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 2: Writing Simple Programs
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. The best way to write a program is to immediately type in some code and then debug it
#     until it works. FALSE

#  2. An algorithm can be written without using a programming language. TRUE

#  3. Programs no longer require modification after they are written and de-bugged. FALSE

#  4. Python identifiers must start with a letter or underscore. TRUE

#  5. Keywords make good variable names. FALSE

#  6. Expressions are built from literals, variables and operators.

#  7. In Python, x = x + 1 is a legal statement. TRUE
#     [Note: In a functional programming language, it would be illegal.]

#  8. Python does not allow the input of multiple values with a single statement. FALSE

#  9. A counted loop is designed to iterate a specific number of times. TRUE

# 10. In a flowchart, diamonds are used to show statement sequences, and rectangles are used
#     for decision points. FALSE
#     [Explanation: Other way around.]


## Multiple Choice

#  1. Which of the following is not a step in the software development process? [C]
#     (a) specification     (b) testing/Debugging
#     (c) fee setting       (d) maintenance

#  2. What is the correct formula for converting Celsius to Fahrenheit? [?]
#     (a) F = 9/5(C) + 32       b) F = 5/9(C) - 32
#     (c) F = B^2 - 4AC         d) F = (212 - 32) / (100 - 0)

#  3. The proces of describing exactly what a computer program will do to solve a problem is called [D]
#     (a) design     (b) implementation     (c) programming     (d) specification

#  4. Which of the following is not a legal identifier? [C]
#     (a) spam     (b) spAm     (c) 2spam     (d) spam4U

#  5. Which of the following are not used in expressions? [B]
#     a) variables     (b) statements     (c) operators     (d) literals

#  6. Fragments of code that produce or calculate new data values are called [B]
#     a) identifiers            b) expressions
#     c) productive clauses     d) assignemnt statements    

#  7. Which of the following is not a part of the IPO pattern? [B]
#     a) input     b) program     c) process     d) output

#  8. The template for <variable> in range(<expr>) describes [D]
#     a) a general for loop     b) an assignment statement
#     c) a flowchart            d) a counted loop        

#  9. Which of the following is the most accurate model of assignment in Python? [A}
#     a) sticky-note     b) variable-as-box     c) simultaneous     d) plastic-scale

# 10. In Python, getting user input is done with a special expression called [D]
#     a) for     b) read     c) simulataneous assignment     d) input


## Discussion

#  1. List and describe in your own words the six steps in the software development process.

#  2. Write out the chas.py prgoram (Section 1.6) and identify the parts of the program as follows:
#     a) Each identifier
#     b) Each expression
#     c) Put a comment at the end of each line indicating the type of statement on that line
#        (e.g., output, assignment, input, loop, etc.)

#  3. Explain the relationship among the concepts: definite loop, for loop, and counted loop.

#  4. Show the output from the following fragments:
#     a) for i in range(5):
#            print(i + i)
#     b) for d in [3,1,4,1,5]:
#            print(d, end=" ")
#     c) for i in range(6):
#            print(i, 2**i)
#     d) for i in range(5):
#            print(i, 2**1)

#  5. Why is it a good idea to first write out an algorithm in pseudocode rather than jumping
#     immediately to Python code?

#  6. The Python print function supports other keyboard parameters besides end. One of these other
#     keyboard parameters is sep. What do you think the sep parameter does? Hint: sep is short for
#     separator. Test your idea either by trying it interactively or by consulting the Python
#     documenation.

#  7. What do you think will happen if the following code is executed?
#
#     print("start")
#     for i in range(0):
#          print("Hello")
#     print("end")
#
#     Look at teh flowchart for the for statement in this chapter to help you figure this out. Then test
#     your prediction by tring out these lines in a program.



### PROGRAMMING EXERCISES

#  1.

#  2.

#  3.

#  4.

#  5. Modfiy the convert.py program (Section 2.2) with a loop so that it executes 5 times before quitting. Each
#     time through the loop, the program should get another temperature from the user and print the converted value.

#  6. Modify the futval.py program (SEction 2.7) so that the number of yaers for the investment is also a user
#     input. Make sure to change the final message to reflect teh correct number of years.

#  7. Suppose you have an investment plan where you invest a certain fixed amount every year. Modify futeval.py
#     to compute the total accumulation of your investment. The inputs to the program will be the amount to invest
#     each year, the interest rate, and the number of years for the investment.

#  8. As an alternative to APR, the interest accrued on an account is often described in terms of a nominal
#     rate and the number of compounding periods. For example, if the interest rate is 3% and the interest is
#     compounded quarterly, the account actually earns .75% interest every 3 months.
#
#     Modify the futval.py program to use this method of entering the interest rate. The program should prompt
#     the user for the yearly rate (rate) and the number of times that the interest is compounded each year
#     (periods). To compute the value in ten years, the program will loop 10 * periods times and accrue
#     rate/period interest on each iteration.

#  9. Write a program that converts temperatures from Fahrenheit to Celsius.

# 10. Write a program that converts distances measured in kilometers to miles. One kilometer is approximately
#     0.62 miles.

# 11. Write a program to perform a unit conversion of your own choosing. Make sure that the program prints
#     an introduction that explains what it is.

# 12. Write an interactive Python calculator program. The program should allow the user to type a
#     mathematical expression, and then print the value of the expression. Include a loop so that the
#     user can perform many calculations (say, up to 100). Note: To quit early, the user can make the
#     program crash by typing a bad expression or simply clsoing the window that the calculator program
#     is running in. You'll learn better ways of terminating interactive programs in later chapters. 

