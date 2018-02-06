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

#  6. Expressions are built from literals, variables and operators. TRUE
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
#     [Explanation: p.50: The software development process involves the following steps:
#                             1. Problem Analysis
#                             2. Program Specification
#                             3. Design
#                             4. Implementation
#                             5. Testing/Debugging
#                             6. Maintenance

#  2. What is the correct formula for converting Celsius to Fahrenheit? [A]
#     (a) F = 9/5(C) + 32       b) F = 5/9(C) - 32
#     (c) F = B^2 - 4AC         d) F = (212 - 32) / (100 - 0)
#     [Explanation: p.29 "She knows that 0 degrees Celsisus (freezing) is equal ti 32 degrees
#     Fahrenheit. With this information, she computes the ratio of Fahrenheit to Celsius degrees as
#     (212-32)/(100-0) = 180/100 = 9/5. Using F to represent the Fahrenheit temperature and C for
#     Celsius, the conversion formula will have the form F = (9/5)C + k for some constant K. Plugging
#     in 0 and 32 for C and F, respectively, Susan immediately sees that k = 32. So the final formula
#     for the relationship is F = (9/5)C + 32."]

#  3. The proces of describing exactly what a computer program will do to solve a problem is called [D]
#     (a) design     (b) implementation     (c) programming     (d) specification
#     [Explanation: p.50: "Program Specification: Deciding exactly what the program will do."]

#  4. Which of the following is not a legal identifier? [C]
#     (a) spam     (b) spAm     (c) 2spam     (d) spam4U
#     [Explanation: p.31: "Python has some rules about how identifiers are formed. Every identifier must
#     begin with a letter or underscore (the "_" character) which may be followed by any sequence of
#     letters, digits, or underscores."]

#  5. Which of the following are not used in expressions? [B]
#     a) variables     (b) statements     (c) operators     (d) literals
#     [Explanation: p.32: "The simplest kind of expression is a literal." p.33: "A simple identifier
#     can also be an expression. We use identifiers as variables to give names to values." p.32: "More
#     complex and interesting expressions can be constructed by combining simpler expressions with
#     operators." p.523: "statement: A Single command in a programming langauge."]

#  6. Fragments of code that produce or calculate new data values are called [B]
#     a) identifiers            b) expressions
#     c) productive clauses     d) assignemnt statements
#     [Explanation: p.32: "The fragments of program code that produce or calculuate new data values are
#     called expressions."]

#  7. Which of the following is not a part of the IPO pattern? [B]
#     a) input     b) program     c) process     d) output
#     [Explanation: p.29: "...a standard pattern: Input, Process, Output (IPO)." As discussed in the
#     previous chapter, a program is a specific set of instructions telling a computer precisely
#     what to do step by step.]

#  8. The template for <variable> in range(<expr>) describes [D]
#     a) a general for loop     b) an assignment statement
#     c) a flowchart            d) a counted loop        
#     [Explanation: p.44: "This particular loop patter is called a counted loop.."]

#  9. Which of the following is the most accurate model of assignment in Python? [A}
#     a) sticky-note     b) variable-as-box     c) simultaneous     d) plastic-scale
#     [Explanation: p.38: "The effect is like moving a sticky note from one object to another."]

# 10. In Python, getting user input is done with a special expression called [D]
#     a) for     b) read     c) simulataneous assignment     d) input
#     [Explanation: p.39: "The purpose of an input statement is to get some information from the user of
#     a program and store it in a variable. Some programming languages have a special statemetn to do
#     this. In Python, input is accomplished using an assignment statement combined with a built-in
#     function called input."]

## Discussion

#  1. List and describe in your own words the six steps in the software development process.
#     The software development process consists of six distinct steps. Only when one is complete should
#     the next one be undertaken.
#
#     First, it is necessary to understand the problem as precisely as possible. This is the most
#     important step, and it may require a lot of research and thinking. In fact, this step may take
#     longer than all the other steps. But, without it, it is not possible to proceed to the other steps.
#     In other words, this step requires what is commonly referred to as "analysis." But, really what we are
#     talking about here is defining (or describing) the problem in a precise and unambiguous way. A true 
#     definition/description of the problem is the key for the next step.
#     -In other words, this step answers the question: What is the problem?
#
#     Second, only after you define (or describe) the problem can you start thinking about what could be done
#     to solve it. In the context of programming, this means deciding (and describing) what precisely your program
#     will do to solve the problem that you defined/described. Even more precisely, it means defining/describing
#     what the inputs and outpus of the program will be. Their description should include how they relate to each other.
#     A true definition/desription of the program (including the relation of inputs to outpus)
#     is the key for the next step.
#     -In other words, this step answers the question: What are the specifications of a solution to the problem?
#
#     Third, after describing the program in response to the problem description, it is necessary to describe the
#     structure of the program, itself. This means designing the step-by-step process(es) (aka algorithm(s)) that will meet the
#     specifications set forth above.
#     -In other words, this step answers the question: How should the program be designed to meet its specifications?
#
#     Fourth, after deciding deciding on the appropriate design, it is time to implement the design by translating it
#     into a programming language and put it into the computer so that the computer can follow the instructions.
#     -In other words, this step answers the question: How should I translate the program design into code?
#
#     Fifth, after implementation is complete, it is necessary to verify whether or not the program works as expected,
#     i.e. according to its specifications. This can be seen as a feedback loop whereby the program is tested for errors.
#     If errors arise, these must be dealt with in a process called debuging.
#     -In other words, this step answers the question: What will break the program?
#
#     Sixth, over time the program will have to be maintained in response to user needs. Thus, it will need to be further
#     developed as user habits and expectations evolve.
#     -In other words, this step calls for evolving the program, thus repeating steps one through five, where the problem
#     is defined as a change in user needs.

#  2. Write out the chas.py prgoram (Section 1.6) and identify the parts of the program as follows:
#     a) Each identifier
#     b) Each expression
#     c) Put a comment at the end of each line indicating the type of statement on that line
#        (e.g., output, assignment, input, loop, etc.)
#
# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():                                                # function definition
    print("This program illustrates a chaotic funciton.")  # output statement
    x = eval(input("Enter a number between 0 and 1: "))    # assignment statement wrapped around input statement
    for i in range(10):                                    # loop statement
        x = 3.9 * x * (1 - x)                              # expression
        print(x)                                           # output statement

# Identifiers:
#      chaos, main(), print(), x, eval, input, for, i, in, range()
# Expressions:
#      literals: "This program illustrates a chaotic funciton.", "Enter a number betwee 0 and 1", 10, 3.9
#      more complex using operators: 3.9 * x * (1 - x)
#      even more complex using loop statement: for i in range(10) - technically, this is a control construct, but it does produce
#      new values so I am counting it as an expression

#  3. Explain the relationship among the concepts: definite loop, for loop, and counted loop.
#     A definite loop is the simplest kind of loop that will go around the loop body a definite number of times that is defined
#     at the start of the loop.
#     A counted loop is a particular loop pattern. It is a common way to use a definite loop. It will go around the loop body according
#     to a defined count or number of times.
#     A for loop is a statement in Python that is used to implement a counted loop and has the form
#     for <var> in <sequence>:
#         <body>
#     [See pp. 43-6.]

#  4. Show the output from the following fragments:
#                                 Expected           |        Actual
#     a) for i in range(5):
#            print(i + i)         0
#                                 2
#                                 4
#                                 6
#                                 8
#     b) for d in [3,1,4,1,5]:
#            print(d, end=" ")    3 1 4 1 5
#
#     c) for i in range(4):       
#            print("Hello")       Hello
#                                 Hello
#                                 Hello
#                                 Hello
#
#
#
#     d) for i in range(6):
#            print(i, 2**i)       0, 1
#                                 1, 2
#                                 2, 4
#                                 3, 8
#                                 4, 16
#                                 5, 32   
#                            

#  5. Why is it a good idea to first write out an algorithm in pseudocode rather than jumping
#     immediately to Python code?
#
#     It reduces the mental overhead of having to write the algorithm in a more complicated
#     fashion, which can stifle the creative process (p.30).


#  6. The Python print function supports other keyboard parameters besides end. One of these other
#     keyboard parameters is sep. What do you think the sep parameter does? Hint: sep is short for
#     separator. Test your idea either by trying it interactively or by consulting the Python
#     documenation.
#
#     The sep parameter separates specifies the separator between multiple values when printing. 


#  7. What do you think will happen if the following code is executed?
#                            Expected          |   Actual
#     print("start")         "Start"
#     for i in range(0):     "end"
#          print("Hello")
#     print("end")
#
#     Look at teh flowchart for the for statement in this chapter to help you figure this out. Then test
#     your prediction by tring out these lines in a program.
#
#     Explanation: p.45: "In general, range(<expr>) will produce a sequence of numbers that starts with 0
#     and goesup to, but does not include the value of <expr>. If you think about it, the value of the
#     expression determines the number of items in the resulting sequence." According to the flowchart on
#     p.46, since there are no more items in the sequence defined by range(0), the loop never goes around
#     the loop body.

### PROGRAMMING EXERCISES

#  1. A user-friendly program should print an introduction that tells the user what the program does. Modify the
#     convert.py program (Section 2.2) to print out an introduction.
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    print("This program coverts a temperature in Celsius to a temperature in Fahrenheit.")
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()


#  2. On many systems with Python, it is posible to run a program by simply clicking (or double-clicking) on the
#     icon of the program file. If you are able to run the convert.py program this way, you may discover another
#     usability issue. The program starts running in a new window, but as soon as the program is finished, the
#     window disappears so that you cannot read the results. Add an input statement at the end of the program so
#     that it pauses to give the user a chance to read the results. Something like this should work:
#
#     input("Press the <Enter> key to quit.")
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit
# by: Susan Computewell

def main():
    
    print("This program coverts a temperature in Celsius to a temperature in Fahrenheit.")
    
    celsius = eval(input("What is the Celsius temperature? "))
    fahrenheit = 9/5 * celsius + 32
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.")
    
main()


#  3. Modify the avg2.py program (Section 2.5.3) to find the average of three exam scores.
#
# avg3.py
#   A simple program to average three exam scores  
#   Illustrates use of multiple input

def main():
    
    print("This program computes the average of two exam scores.")

    score1, score2, score3 = eval(input("Enter two scores separated by a comma: "))
    average = (score1 + score2 + score3) / 3

    print("The average of the three scores is:", average)

main()

#  4. Modify the convert.py program (Section 2.2) with a loop so that it executes 5 times before quitting. EAch time
#     through the loop, the program should get another temperature from the user and print a converted value.
#
# convert.py
#     A program to convert Celsius temps to Fahrenheit five times
# by: Susan Computewell

def main():
    
    for i in range(5):
        celsius = eval(input("What is the Celsius temperature? "))
        fahrenheit = 9/5 * celsius + 32
        print("The temperature is", fahrenheit, "degrees Fahrenheit.")

main()

#  5. Modfiy the convert.py program (Section 2.2) so that it computes and prints a table of Celsius temperatures and the
#     Fahrenheit equivalents every 10 degrees from 0 degress celsius to 100 degrees celsius.

#converstionchart.py
#     A program to compute and print a table of Celsius temperatures and the Fahrenheit equivalents every 10 degrees
#     from 0 degrees celsius to 100 degrees celsius

def main():
    print("Celisus Temperatures and")
    print("Their Fahrenheit Equivalents")
    print("{0:<14}{1:<14}".format("C", "F"))
    print("----------------------------")
    for i in range(11):
        celsius = 10 * i
        fahrenheit = int(9/5 * celsius + 32)
        print("{0:<14}{1:<14}".format(celsius, fahrenheit))
        
main()
        # celsius = celsius + 10

#  6. Modify the futval.py program (Section 2.7) so that the number of yaers for the investment is also a user
#     input. Make sure to change the final message to reflect the correct number of years.

# futval.py
#    A program to compute the future value of an investment
#    with number of years determined by the user

def main():
    print("This program calculates the future value")
    print("of a multi-year investment with
    print("non-compounding interest.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    years = eval(input("Enter the number of years for the investment: "))

    for i in range(years):
        principal = principal * (1 + apr)

    print("The value in ", years ,"years" "is:", principal)

main()


#  7. Suppose you have an investment plan where you invest a certain fixed amount every year. Modify futeval.py
#     to compute the total accumulation of your investment. The inputs to the program will be the amount to invest
#     each year, the interest rate, and the number of years for the investment.

#     inputs: principle
#             APR
#             fixed yearly investment
#             number of years
#     output: total accumulation

#     start with principal
#     for a given number of years, add fixed yearly investment to principal
#     to the resulting sum, calculate APR and add this to the sum
#     repeat for specified # of years
#     then


# futval.py
#    A program to compute the future value of an investment
#    with number of years determined by the user

def main():
    print("This program calculates the total future value")
    print("of a multi-year investment with")
    print("non-compounding interest and an additional")
    print("investment of a certain fixed amount each year.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    yearlyinvestment = eval(input("Enter the fixed yearly amount to invest: "))
    years = eval(input("Enter the number of years for the investment: "))
          
    for i in range(years):
          principal = principal + yearlyinvestment
          principal = principal * (1 + apr)

    print("The value in ", years ,"years is:", principal, sep=" ")

main()


#  8. As an alternative to APR, the interest accrued on an account is often described in terms of a nominal
#     rate and the number of compounding periods. For example, if the interest rate is 3% and the interest is
#     compounded quarterly, the account actually earns .75% interest every 3 months.
#
#     Modify the futval.py program to use this method of entering the interest rate. The program should prompt
#     the user for the yearly rate (rate) and the number of times that the interest is compounded each year
#     (periods). To compute the value in ten years, the program will loop 10 * periods times and accrue
#     rate/period interest on each iteration.

#     inputs: yearly rate
#             periods (number of times that the interest is compounded each year)
#             principal
#             fixed yearly investment
#             number of years
#     output: total accumulation

def main():
    print("This program calculates the total future value")
    print("of a multi-year investment with by describing")
    print("the interest accrued in terms of a nominal rate")
    print("and the number of compounding periods.")

    principal = eval(input("Enter the initial principal: "))
    interestrate = eval(input("Enter the interest rate: "))
    periods = eval(input("Enter the number of compounding periods per year: "))
    years = eval(input("Enter the number of years for the investment: "))

    nominalrate = interestrate / periods
          
    for i in range(periods * years):
          principal = principal * (1 + nominalrate)

    print("The value in ", years ,"years is:", principal, sep=" ")

          
#  9. Write a program that converts temperatures from Fahrenheit to Celsius.

# convert2.py
#     A program to convert Fahrenheit temps to Celsius
# by: Susan Computewell

def main():
    
    print("This program converts a temperature in Fahrenheit to a temperature in Celsius.")
    
    fahrenheit = eval(input("What is the Fahrenheit temperature? "))
    celsius = 9/5 * celsius + 32
    fahrenhet = (fahrenheit - 32) * 5/9
    
    print("The temperature is", fahrenheit, "degrees Fahrenheit.")
    input("Press the <Enter> key to quit.") # Why does this work?
main()

# 10. Write a program that converts distances measured in kilometers to miles. One kilometer is approximately
#     0.62 miles.

# convert3.py
#     A program to convert distances measured in kilometers to miles
# by: Susan Computewell

def main():
    
    print("This program converts distances measured in kilometers to miles.")
    
    kilometers = eval(input("What is the distance in kilometers?"))
    miles = kilometers * .62
    
    print("The distance is", kilometers, "kilometers.")
    input("Press the <Enter> key to quit.")
          
main()

# 11. Write a program to perform a unit conversion of your own choosing. Make sure that the program prints
#     an introduction that explains what it is.

#     gal US = L x 0.264172052

# convert3.py
#     A program to convert liters to gallons

def main():

    print("This program converts liters to gallons.")

    gallons = eval(input("How many gallons?")
    liters = gallons * .264172052

    print("The fluid volume in liters is", liters, "liters.")
    input("Press the <Enter> key to quit.")

# 12. Write an interactive Python calculator program. The program should allow the user to type a
#     mathematical expression, and then print the value of the expression. Include a loop so that the
#     user can perform many calculations (say, up to 100). Note: To quit early, the user can make the
#     program crash by typing a bad expression or simply closing the window that the calculator program
#     is running in. You'll learn better ways of terminating interactive programs in later chapters.

def main():

    print("This program is an interactive calculator. Enter your calculations below.")

    for i in range(100):
        expression = eval(input(""))
        print(expression)

main()
                   

