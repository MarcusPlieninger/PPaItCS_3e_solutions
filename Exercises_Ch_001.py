#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 1: Computers and Programs
#### End-of-Chapter Exercises

### REVIEW QUESTIONS

## True/False

#  1. Computer science is the study of computers. FALSE

#  2. The CPU is the "brain" of the computer. TRUE

#  3. Secondary memory is also called RAM. FALSE

#  4. All information that a computer is currently working on is stored in the main memory. TRUE

#  5. The syntax of a language is its meaning, the semantics is its form. FALSE

#  6. A function definition is a sequence of statements that defines a new command. TRUE

#  7. A programming environment refers to a place where programmers work. FALSE

#  8. A variable is used to give a name to a value so it can be referred to in other places. TRUE

#  9. A loop is used to skip over a section of a program. FALSE

# 10. A chaotic function can't be computed by a computer. FALSE


## Multiple Choice

#  1. What is the fundamental question of computer science? b) What can be computed?

#  2. An algorithm is like a d) recipe

#  3. A problem is intractable when d) it is not practical to solve

#  4. Which of the following is not an example of secondary memory a) RAM

#  5. Computer languages designed to be used and understood by humans are b) high-level computer languages

#  6. A statement is b) a complete computer command

#  7. One difference between a compiler and an interpreter is c) a compiler is no longer needed after a program is translated

#  8. By convention, the statements of a program are often placed in a function called b) main

#  9. Which of the following is not true of comments? a) They make a program more efficient

# 10. The items listed in the parentheses of a function are called d) both b) parameters and c) arguments are correct*
#     *Note: I have a feeling that parameter refers more accurately to a *function definition* where as *argument* is used
#     to refer to the value that is passed to the function when it is called, so that the argument replaces all instances
#     of the parameter in the definition.

## Discussion

#  1. Compare and contrast the following pairs of concepts from the chapter:
#     a) Hardware vs. Software
#     b) Algorithm vs. Program
#     c) Programming Lnaguage vs. Natural Language
#     d) High-Level Language vs. Machine Language
#     e) Interpreter vs. Compiler
#     f) Syntax vs. Symantics

#  2. List and explain in your own words the role of each of the five basic functional units of a computer depicted in Figure 1.1.

#  3. Write a detailed algorithm for making a peanut butter and jelly sandwich (or some other everyday activity). You should assume
#     that you are talking to someone who is conceptually able to do the task, but has never actually done it before. For example,
#     you might be telling a young child.

#  4. As you will learn in a later chapter, many of the numbers stored in a computer are not exact values, but rather close
#     approximations. For example, the value 0.1 might be sotred as 0.10000000000000000555. Usually, such small differences are not
#     a problem; however, given what you have learned about chaotic behavior in Chapter 1, you should realize the need for caution in
#     certain situations. Can you think of exmaples where this might be a problem? Explain.

#  5. Trace through the chaos program from Section 1.6 by hand using 0.15 as the input value. Show the sequence of output that results.


### PROGRAMMING EXERCISES

# 1. Start up an interactive Python session and try typing in each of the following commands. Write down the results you see there.
#    a) print("Hello, world!")   | Expected result: 'Hello, world!' | Actual result:
#    b) print("Hello", "world!") | Expected result: 'Hello' 'world!'| Actual result:
#    c) print(3)                 | Expected result: 3               | Actual result:
#    d) print(3,0)               | Expected result: '3,0'           | Actual result:
#    e) print(2 + 3)             | Expected result: 5               | Actual result:
#    f) print(2.0 + 3.0)         | Expected result: 5.0             | Actual result:
#    g) print("2" + "3")         | Expected result: 23              | Actual result:
#    h) print("2 + 3 =", 2 + 3)  | Expected result: 2 + 3 = 5       | Actual result:
#    i) print(2 * 3)             | Expected result: 6               | Actual result:
#    j) print(2 ** 3)            | Expected result: 8               | Actual result:
#    k) print(7 / 3)             | Expected result: 2.3333333333335 | Actual result:
#    l) print(7 // 3)            | Expected result: 2               | Actual result:

# 2. Enter and run the chaos program from Section 1.6. Try it out with various values of input to see that it functions as described
#    in the chapter.

# 3. Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. Your modified line of code should
#    look like this:
#    x = 2.0 * x * (1 - x)
#    Run the program for various input values and compare the results to those obtained from the original program. Write a short paragraph
#    describing any differences that you notices in the behavior of the two versions.

# 4. Modify the chaos program so that it prints out 20 values instead of 10.
#    Solution:
     # File: chaos.py
     #A simple program illustrating chaotic behavior.
     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range (20):
             x = 3.9 * x * (1 - x)
             print(x)
        
# 5. Modfiy the chaos program so taht the number of values to print is determined by the user. You wil have to add a line near the top of the
#    program to get another value from the user:
#    n = eval(input("How many numbers should I print? "))
#    Then you will need to change the loop to use n instead of a specific number.
     def main():
         print("This program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         n = eval(input("How many numbers should I print? "))
         for i in range (n):
             x = 3.9 * x * (1 - x)
             print(x)
         
# 6. The calculation performed in the chaos program can be written in a number of ways that are algebraically equivalent. Write a version of
#    the program for each of the following ways of doing the computation. Have your modified programs print out 100 iterations of the calculation
#    and compare the results when run on the same input.
#    a) 3.9 * x * (1 - x)
     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range (100):
             x = 3.9 * x * (1 - x)
             print(x)

#    b) 3.9 * x (x - x * x)
     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range (100):
             x = 3.9 * x(X - X * x)
             print(x)
             
#    c) 3.9 * x - 3.9 * x * x
     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range (100):
             x = 3.9 * x - 3.9 * X * X
             print(x)

#    Explain the results of this experiment. Hint: See discussion question number 4, above.

# 7. (Advanced) Modify the chaos program so that it accepts two inputs and then prints a table with two columns similar to the one shown in Section
#    1.8. (Note: You will probably not be able to get the columns to line up as nicely as those in the example. Chapter 5 discusses how to print
#    numbers with a fixed number of decimal places).







