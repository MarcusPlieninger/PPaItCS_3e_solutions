#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 2: Writing Simple Programs
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. The best way to write a program is to immediately type in some code and then debug it
#     until it works. FALSE
#     [Explanation: p.27-8 "Writing large programs is daunting challenge. It would be almost
#     impossible without a systematic approach. The process of creating a program is often
#     broken down into stages according to the information that is produced in each phase."
#     p. 29 "Susan knows better than to just dive in and start writing a program without first
#     having a clear idea of what to build."]

#  2. An algorithm can be written without using a programming language. TRUE
#     [Explanation: p.30 "Susan could write her algorithm down in a computer language. However,
#     the precision required to write it out formally tends to stifle the creative process of
#     developing the algorithm. Instead, she writes her algorithm using pseudocode. Pseudocode
#     is just precise English that describes what a program does. It is meant to communicate
#     without all the extra mental overhead getting the details right in any particular
#     programming language."]

#  3. Programs no longer require modification after they are written and de-bugged. FALSE
#     [Explanation: see step called "Maintaining the Program' on p.28: "Continue developing the
#     program in response to the needs of your users. Most programs are never really finished;
#     they kepp evolving over years of use."]

#  4. Python identifiers must start with a letter or underscore. TRUE
#     [Explanation: p.31 "Python has rules about how identifiers are formed. Every identifier must
#     begin with a letter or underscore (the "_" character) which may be followed by any sequence
#     of letters, digits, or underscores. This implies that a single identifier cannot contain any
#     spaces."]

#  5. Keywords make good variable names. FALSE
#     [Explanation: p.31 "One important thing to be aware of is that some identifiers are part of
#     Python itself. These names are called reserved words or keywords and cannot be used as ordinary
#     identifiers."]

#  6. Expressions are built from literals, variables and operators.
#     [Explanation: p.32: "The simplest kind of expression is a literal." p.33 "A simple identifier
#     can also be an expression. We use identifiers as variables to give names to values. When an
#     identifier appears as an expression, its value is retrieved to provide a result for the
#     expression. p.34 "More complex and interesting expressions can be constructed by combining
#     simpler expressions with operators."]

#  7. In Python, x = x + 1 is a legal statement. TRUE
#     [Explanation: p.37 "Sometimes it's helpful to think of a variable as a sort of named storage
#     location in computer memory, a box that we can put a value in. When the variable changes, the old
#     value is erased and a new one written in. Figure 2.1 shows how we might picture the effect of
#     x = x + 1 using this model. This is exactly the way assignment works in some computer languages.
#     It's also a very simple way to view the effect of assignment, and you'll find pictures similar to
#     this throughout the book."]
#     [Interesting aote: In a functional programming language (e.g., Racket), this would be illegal.]

#  8. Python does not allow the input of multiple values with a single statement. FALSE
#     [Explanaion: drawn from p. 41 on simultaneous assignment and p. 39 on input: Since Python allows
#     simultaneous assignment, the built-in input function can be used to prompt the user for multiple
#     values which are simultaneously assigned to varriables.]

#  9. A counted loop is designed to iterate a specific number of times. TRUE
#     [Explanation: p.43-4 "The simplest kind of loop is called a definite loop. This is a loop that will
#     execute a definite number of points. That is, at the point in the program when the loop begins, Python
#     knows how many times to go around (or iterate) the body of the loop....This particular loop pattern is
#     called a counted loop, and it is build using a Python for statement.]

# 10. In a flowchart, diamonds are used to show statement sequences, and rectangles are used
#     for decision points. FALSE
#     [Explanation: p.47: Other way around. "The diamond-shaped box in the flowchart represents a decision
#     in the program."]

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

