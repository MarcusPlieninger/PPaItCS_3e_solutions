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
#     [Explanation: pp.3-4: "A famous computer scientist named Edsger Dikjstra once quipped that computers are to
#     computer science what telescopes are to astronomy. The computer is an important tool in computer science, but
#     it is not itself the object of study. Since a computer can carry out any process that we can describe, the real
#     question is, 'What processes can we describe?' To put it another way, the fundamental question of computer
#     science is simply, 'What can be computed?' Computer scientists use numerous techniques of investigation to
#     answer this question. The three main ones are design, analysis, and experimentation."

#  2. An algorithm is like a [D]
#     a) newspaper
#     b) venus flytrap
#     c) drum
#     d) recipe
#     [Explanation: p.4: "One way to demonstrate that a particular problem can be solved is to actually design a solution.
#     That is, we develop a step-by-step process for achieving the desired result. Computer scientists call this an
#     algorithm. That's a fancy word that basically means 'recipe.' The design of algorithms is one of the most important
#     facets of computer science. In this book you will find techniques for designing and implementing algorithms."

#  3. A problem is intractable when [D]
#     a) you cannot reverse its solution
#     b) it involves tractors
#     c) it has many solutions
#     d) it is not practical to solve
#     [Explanation: p.4: "Analysis is the process of examining algorithms and problems mathematically. Computer scientists
#     have shown that some seemingly simple problems are not solvably by any algorithm. Other problems are intractable. The
#     algorithms that solve these problems take too long or require too much memory to be of practical value. Analysis of
#     algorithms is an important part of computer science; throughout this book we will touch on some of the fundamental
#     principals. Chapter 13 has examples of unsolvable and intractable problems."]

#  4. Which of the following is not an example of secondary memory [A]
#     a) RAM
#     b) hard drive
#     c) USB flash drive
#     d) DVD
#     [Explanation: p.6: Secondary memory provides more permanent storage. RAM is volatile and is another term for main memory.]

#  5. Computer languages designed to be used and understood by humans are [B]
#     a) natural languages
#     b) high-level computer languages
#     c) machine languages
#     d) fetch-execute languages
#     [Explanation: p.7: Programming languages that are "designed to be used and understood by humans" are known as "high-level
#     computer langagues."]

#  6. A statement is [B]
#     a) a translation of machine language
#     b) a complete computer command
#     c) a precise description of a problem
#     d) fetch-execute languages
#     [Explanation: p.10: "In programming languages, a complete computer command is called a statement."]

#  7. One difference between a compiler and an interpreter is [C]
#     a) a compiler is a program
#     b) a compiler is used to translate high-level language into machine language
#     c) a compiler is no longer needed after a program is translated
#     d) a compiler processes source code
#     [Explanation: p.8: "The difference between interpreting and compiling is that compiling is a one-shot translation; once a
#     program is compiled, it may be run over and over again without further need for the compiler or the source code."]

#  8. By convention, the statements of a program are often placed in a function called [B]
#     a) import
#     b) main
#     c) program
#     d) IDLE
#     [Explanation: p.14: ("Programs are often placed in a function called main.")

#  9. Which of the following is not true of comments? [A]
#     a) They make a program more efficient.
#     b) They are intended for human readers.
#     c) They are ignored by Python.
#     d) In Python, they begin with a pound sign (#).
#     [Explanation: p.16: "They...are ignored by Python."

# 10. The items listed in the parentheses of a function are called [D]
#     a) parentheticals
#     b) parameters
#     c) arguments
#     d) both b) parameters and c) arguments are correct*
#     *Note: I have a feeling that parameter refers more accurately to a *function definition* where as *argument* is used
#     to refer to the value that is passed to the function when it is called, so that the argument replaces all instances
#     of the parameter in the definition.
#     [Explanation: p.11: "Commands can have changeable parts called parameters (also called arguments) that are placed within
#     the parentheses." p.12: "...parentheses must be included after the function name whenever we want to execute a function."

## Discussion

#  1. Compare and contrast the following pairs of concepts from the chapter:
#     a) Hardware vs. Software
#        Hardware is the body, software is the soul. In other words, hardware refers to the actual physical machine, while
#        software denotes the programs that tell the machine what to do. Software makes hardware useful for specific purposes
#        (p.3). Software could not exist without hardware. Hardware would be useless without software. Software serves as the
#        intermediary between man and machine. The process of creating software is a human one, as is the making of hardware.
#        Both are a form of engineering.
#     b) Algorithm vs. Program
#        An algorithm is a recipe or a step-by-step process to achieve a specific result (p.4). A program is a more general term
#        referring to a detailed, step-by-step sequence of instructions telling a computer exactly what to do (p.2). A program
#        may contain one or more algorithms, but an alogorithm need not be a program. Both, however, share a common characteristic:
#        they specify a process step by step. Algorithms can be turned into programs that determine what the physical machine can
#        do and does do.
#     c) Programming Language vs. Natural Language
#        Any language is a kind of code for communicating meaning and thus has both syntax and semantics. Natural language is encoded
#        in speech which in turn is encoded in writing and serves to communicate meaning among humans. Meaning among humans is something
#        that is extraordinarly complex and is the result of our collective as well as individual experience and the store of this experience
#        in what we commonly call culture. Therefore, the ambiguity and imprecision that is often a characteristic of natural language reflects
#        the organic development of natural language as a means of expressing the vicissitudes of human experience. These qualities also serve
#        the creation of human culture. Poetry can be created from the ambiguity and imprecision in language. Ambiguity and imprecision also
#        make it possible to lie as well as miscommunicate, but they also reflect the mystery of the soul.
#        A programming language also uses code to transmit meaning with precise semantics, in the form of notations with precise syntax. This
#        precision is the consequence of the need to express computations precisely and unambiguously since computations themselves have these
#        characteristics. Thus, programming languages cannot be said to have "evolved" in the same way that human languages have. The need to
#        express computations precisely is necessary because the computer is a precise machine, and there for precise instructions are
#        needed for the computer to follow them. This precision is a reflection of the mathematical underpinnings of the hardware.
#     d) High-Level Language vs. Machine Language
#        A high-level language is meant to be understood by humans. A machine language is understood by the computer.
#     e) Interpreter vs. Compiler
#        An interpreter translates code into machine language line-by-line. A compiler does so in one shot.
#     f) Syntax vs. Symantics
#        Syntax is form. Symantics is meaning.

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
#    a) print("Hello, world!")     'Hello, world!' | Hello, world! [See p.33 for explanation.]
#    b) print("Hello", "world!")   'Hello' 'world!'| Hello world!  [See p.33 for explanation.]   
#    c) print(3)                   3               | 3
#    d) print(3,0)                 '3,0'           | 3 0 [Explanation: Without "", , is separator.]
#    e) print(2 + 3)               5               | 5
#    f) print(2.0 + 3.0)           5.0             | 5.0
#    g) print("2" + "3")           23              | 23
#    h) print("2 + 3 =", 2 + 3)    2 + 3 = 5       | 2 + 3 = 5
#    i) print(2 * 3)               6               | 6
#    j) print(2 ** 3)              8               | 8
#    k) print(7 / 3)               2.3333333333335 | 2.3333333333333335 [Question: What determines length of mantissa?]
#    l) print(7 // 3)              2               | 2

# 2. Enter and run the chaos program from Section 1.6. Try it out with various values of input to see that it functions as described
#    in the chapter.
#
#    INPUT:  .1          INPUT: .2           INPUT: .3           INPUT: .9243        INPUT: .00001         INPUT: .000011
#    OUTPUT:             OUTPUT:             OUTPUT:             OUTPUT:             OUPUT:                OUTPUT:
#    0.35100000000000003 0.6240000000000001  0.819               0.27288108899999997 3.899961e-05          4.28995281e-05 
#    0.8884161           0.9150335999999998  0.5781321000000001  0.7738263010380788  0.0001520925472186374 0.0001673009821489063
#    0.3866184397170808  0.30321373239705673 0.951191962303401   0.6825747117532334  0.0005930707187953    0.0006523646708680855
#    0.9248640249724619  0.8239731430433209  0.18106067129594494 0.8449992510500727  0.00231160404507945   0.0025425624556967255
#    0.2710131851083772  0.5656614700878645  0.5782830479626462  0.5108045154220668  0.008994416074091065  0.009890781544236867
#    0.7705036505625796  0.9581854282490118  0.9510998811665442  0.9745447235413278  0.034762714558951066  0.0381925205402561
#    0.6896283226260395  0.1562578420270518  0.18138469912496583 0.09674849090043053 0.13086164611823145   0.14326202246864903
#    0.8347602871063352  0.5141811824451928  0.5790887311884146  0.34081405959478733 0.443573815204487     0.4786782600086812
#    0.5379486456882877  0.9742156868513789  0.950605393136126   0.8761733618715016  0.9625827341107481    0.9732269952745961
#    0.9693836111326567  0.09796598114189214 0.1831236407388855  0.42312504709133986 0.1404671350002371    0.10161922267917184

# 3. Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. Your modified line of code should
#    look like this:
#
#    x = 2.0 * x * (1 - x)
#    Run the program for various input values and compare the results to those obtained from the original program. Write a short paragraph
#    describing any differences that you notices in the behavior of the two versions.
#
#
#    INPUT:  .1          INPUT: .2           INPUT: .3           INPUT: .9243        INPUT: .00001          INPUT: .000011
#    OUTPUT:             OUTPUT:             OUTPUT:             OUTPUT:             OUPUT:                 OUTPUT:
#    0.18000000000000002 0.32000000000000006 0.42                0.13993901999999997 1.99998e-05            2.1999758e-05
#    0.2952              0.43520000000000003 0.4872              0.24071218136287917 3.9998800015999924e-05 4.3998548021295886e-05
#    0.41611392          0.49160192          0.49967231999999995 0.36553965421280704 7.99944002239944ee-05  8.79932242981358e-05
#    0.4859262511644672  0.4998589445046272  0.4999997852516352  0.46384083082157695 0.00015997600223985442 0.00017597096298122686
#    0.49960385918742867 0.49999996020669446 0.4999999999999078  0.4973850289686524  0.00031990081983712356 0.0003518799944028286
#    0.49999968614491325 0.49999999999999684 0.49999999999999994 0.4999863238530105  0.0006395969666051822  0.0007035123497447354
#    0.49999999999980305 0.49999999999999994 0.49999999999999994 0.49999999962592606 0.0012783757646509832  0.0014060348402369842
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.0025534830401106722  0.002808115812530048
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.005093925528949078   0.005600460596226933
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.010135954903309199   0.011138190874674084

#    Observation: In general, when the multiplier is 2, the logistic function appears to behave in a "less random" fashion insofar as it
#    returns values that have less variance. In fact, even when the input values are close together, the output values are very similar.
#    So, it is less "choatic" in its output both for one given input as well as across differnt inputs., especially if they are close together.


# 4. Modify the chaos program so that it prints out 20 values instead of 10.
#    Solution:
     # File: chaos.py
     #A simple program illustrating chaotic behavior.
     def main():
         print("Ths program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range(20):
             x = 3.9 * x * (1 - x)
             print(x)
        
# 5. Modfiy the chaos program so taht the number of values to print is determined by the user. You wil have to add a line near the top of the
#    program to get another value from the user:
#    n = eval(input("How many numbers should I print? "))
#    Then you will need to change the loop to use n instead of a specific number.
#
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
        
main()
         
# 6. The calculation performed in the chaos program can be written in a number of ways that are algebraically equivalent. Write a version of
#    the program for each of the following ways of doing the computation. Have your modified programs print out 100 iterations of the calculation
#    and compare the results when run on the same input.
#
#    Chaos programs:
#
#    a) 3.9 * x * (1 - x)                                                                   
#    def main():                                             
#        print("Ths program illustrates a chaotic function")
#        x = eval(input("Enter a number between 0 and 1: "))     
#        for i in range(100):                                    
#            x = 3.9 * x * (1 - x)
#            print(x)
#
#    b) 3.9 * x (x - x * x)
#     def main():
#         print("Ths program illustrates a chaotic function")
#         x = eval(input("Enter a number between 0 and 1: "))
#         for i in range (100):
#             x = 3.9 * (x - x * x)
#             print(x)
#             
#    c) 3.9 * x - 3.9 * x * x
#     def main():
#         print("Ths program illustrates a chaotic function")
#         x = eval(input("Enter a number between 0 and 1: "))
#         for i in range (100):
#             x = 3.9 * x - 3.9 * x * x
#             print(x)
#
#     OUTPUT COMPARISON
#
#





#    Explain the results of this experiment. Hint: See discussion question number 4, above.

# 7. (Advanced) Modify the chaos program so that it accepts two inputs and then prints a table with two columns similar to the one shown in Section
#    1.8. (Note: You will probably not be able to get the columns to line up as nicely as those in the example. Chapter 5 discusses how to print
#    numbers with a fixed number of decimal places).

#    Basic version with bad formatting.

def main():
     print("Ths program illustrates a chaotic function")
     x, y = eval(input("Enter 2 numbers between 0 and 1 separated by a comma: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * x * (1 - x)
         print(x, "   ", y)
     
main()

#    More secure version with bad formatting.
def main():
     print("Ths program illustrates a chaotic function")
     x = float(input("Enter first numbers between 0 and 1: "))
     y = float(input("Enter second number between 0 and 1: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * x * (1 - x)
         print(x, "   ", y)
     
main()

#    More secure version with good formatting.

def main():
     print("Ths program illustrates a chaotic function")
     x = float(input("Enter first numbers between 0 and 1: "))
     y = float(input("Enter second number between 0 and 1: "))
     z = "input"
     print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x,y,z))
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * x * (1 - x)
         print("{0:>14.6f}{0:>13.6f}".format(x, y))
     
main()




