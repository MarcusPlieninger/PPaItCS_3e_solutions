#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 1: Computers and Programs
#### End-of-Chapter Exercises


### REVIEW QUESTIONS

## True/False

#  1. Computer science is the study of computers. FALSE
#     [Explanation: p.3 "...computer science is not the study of computers. A famous scientist named Edsger
#     Dijkstra once quipped that computers are to computer science what telescopes are to astronomy. The
#     computer is an important tool in cmoputer science, but it is not itself the object of study. Since a
#     computer can carry out any prcess that we can describe, the real question is 'What processes can we
#     describe?' To put it another way, the fundamental question of computer science is simply 'What can be
#     computed?' Computer scientists use numerous techniques of investigation to answer this question. The
#     three main ones are design, analysis, and experimentation.

#  2. The CPU is the "brain" of the computer. TRUE
#     [Explanation: p.5 "The central processing unit (CPU) is the 'brain' of the machine. This is where all
#     the basic operations of the computer are carried out."]

#  3. Secondary memory is also called RAM. FALSE
#     [Explanation: p.6 "The CPU can directly access only information that is stored in the main memory
#     (called RAM for Random Access Memory)."..."In a modern personal computer, the principal secondary
#     memory is typically an internal disk drive (HDD) or a solid state drive (SSD)."]

#  4. All information that a computer is currently working on is stored in the main memory. TRUE
#     [Explanation: The memory stores programs and data. The CPU can directly access any information that is
#     stored in main memory (called RAM for Random Acess Memory). Main memory is fast, but it is also volatile.
#     That is, when the power is turned off, the information in the memory is lost. Thus, there must be some
#     secondary memory that provides more permanent storage.]

#  5. The syntax of a language is its meaning, the semantics is its form. FALSE
#     [Explanation: p.7 "Every structure in a programming language has a precise form (its syntax) and a
#     precise meaning (its semantics)."]

#  6. A function definition is a sequence of statements that defines a new command. TRUE
#     [Explanation: p. 11 "Usually we want to move beyond one-line snippets and execute an entire sequence of
#     statements. Python lets us put a sequence together to create a brand-new command or function. The first
#     line tells Python that we are defining a new function and we are naming it hello."]

#  7. A programming environment refers to a place where programmers work. FALSE
#     [Expalantion: p.13 "A special type of application known as an Integrated Development Environment (IDE)
#     simplifies the process. An IDE is specifically designed to help programmers write programs and includes
#     features such as automatic identing, color highlighting, and interactive development. IDLE is a good
#     example. So far we have just been using IDLE as a Python shell, but it is actually a simple but
#     complete development environment."]

#  8. A variable is used to give a name to a value so it can be referred to in other places. TRUE
#     [Explanation: p. 16 "A variable is used to give a name to a value so that we can refer to it at other
#     points in the program."]

#  9. A loop is used to skip over a section of a program. FALSE
#     [Explanation: p.17 "A loop is a device that tells Python to do the same thing over and over again."]

# 10. A chaotic function can't be computed by a computer. TRUE and FALSE [need to think about this one some more]
#     [Eplanation on the basis of our chaos program: "These two features of our chaos program, apparent
#     unpredictability and extreme sensitivity to initial values, are the hallmarks of chaotic behavior. Chaos
#     has important implications for computer science. It turns out that mnay phenomena in the real world that
#     we might like to model and predict with our computers exhibit just this kind of chaotic behavior."
#     [Note: The appearance of randomness or unpredictability are not the same thing as randomness and
#     unpredictability. Because of the defined nature of computation, a function can only approximate chaos.]

## Multiple Choice

#  1. What is the fundamental question of computer science? [B]
#     a) How fast can a computer compute?
#     b) What can be computed?
#     c) What is the most effective programming language?
#     d) How much money can a programmer make?

#  2. An algorithm is like a [D]
#     a) newspaper
#     b) venus flytrap
#     c) drum
#     d) recipe

#  3. A problem is intractable when [D]
#     a) you cannot reverse its solution
#     b) it involves tractors
#     c) it has many solutions
#     d) it is not practical to solve

#  4. Which of the following is not an example of secondary memory [A]
#     a) RAM
#     b) hard drive
#     c) USB flash drive
#     d) DVD

#  5. Computer languages designed to be used and understood by humans are [B]
#     a) natural languages
#     b) high-level computer languages
#     c) machine languages
#     d) fetch-execute languages

#  6. A statement is [B]
#     a) a translation of machine language
#     b) a complete computer command
#     c) a precise description of a problem
#     d) fetch-execute languages

#  7. One difference between a compiler and an interpreter is [C]
#     a) a compiler is a program
#     b) a compiler is used to translate high-level language into machine language
#     c) a compiler is no longer needed after a program is translated
#     d) a compiler processes source code

#  8. By convention, the statements of a program are often placed in a function called [B]
#     a) import
#     b) main
#     c) program
#     d) IDLE

#  9. Which of the following is not true of comments? [A]
#     a) They make a program more efficient.
#     b) They are intended for human readers.
#     c) They are ignored by Python.
#     d) In Python, they begin with a pound sign (#).

# 10. The items listed in the parentheses of a function are called [D]
#     a) parentheticals
#     b) parameters
#     c) arguments
#     d) both b) parameters and c) arguments are correct*
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
#                                  Expected        | Actual
#    a) print("Hello, world!")     'Hello, world!' | 
#    b) print("Hello", "world!")   'Hello' 'world!'|
#    c) print(3)                   3               | 
#    d) print(3,0)                 '3,0'           | 
#    e) print(2 + 3)               5               | 
#    f) print(2.0 + 3.0)           5.0             | 
#    g) print("2" + "3")           23              | 
#    h) print("2 + 3 =", 2 + 3)    2 + 3 = 5       | 
#    i) print(2 * 3)               6               | 
#    j) print(2 ** 3)              8               | 
#    k) print(7 / 3)               2.3333333333335 | 
#    l) print(7 // 3)              2               | 

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

     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         y = eval(input("Enter a second number betweeon 0 and 1: "))
         print(input     x     y /n --------------------)
         for i in range (100):
             x = 3.9 * x * (1 - x)
             y = 3.9 * x * (1 - x)
             print(x     y)








