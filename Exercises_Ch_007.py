#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 7: Decision Structures
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. A simple decision structure can be implemented with an if statement. TRUE
#     [Explanation: p.212: "Notice taht the body of the if either executes or not depending on the
#     condition. In either case, control then passes to the next statement after the if. This is a
#     one-way or simple decision."]

#  2. In python conditions, "is not equal to" is written as /=.
#     [Explanation: /= is actually an augmented assignment expression, for more info use help('/=') in
#     IDLE. See table on p.213: "is not equal to" is written as !=.

#  3. Strings are compared by lexicographic ordering.
#     [Explanation: p.214: "Conditions may compare either numbers or strings. When comparing strings,
#     the ordering is lexicographic. Basically, this means that strings are put in alphabetic order
#     according to the underlying Unicode values. So all uppercase values come before lowercase
#     equivalents (e.g., "Bbbb" comes before "aaaa," since "B" precedes "a").

#  4. A two-way decision is implemented using an if-elif statement. TRUE
#     [Explanation: p.218: "In Python, a two-way decision can be implemented by attaching an else clause
#     onto an if clause. The result is called an if-else statement." However, pp.222-3 indicate that this
#     is possible since "the else clause is optional."]

#  5. The math.sqrt function cannot compute the square root of a negative number. TRUE
#     [Explanation: p.217: As illustrated by the quadratic program, "it crashes when the coefficients of a
#     a quadratic equation have no real roots. The problem with this code is that when b^2 - 4ac is less
#     than 0, the program attempts to take the square root of a negative number. Since negative numbers do
#     not have real roots, the math library reports an error."]

#  6. A single try statement can catch multiple kinds of errors. FALSE
#     [Explanation: pp.223-7 It is not a "try" statement; it is a "try-except" statement.]

#  7. Multiple-way decisions must be handled by nesting multiple if-else statements. FALSE
#     [Explanation: pp.221-2: Nesting if-else statements is just one way of coding multiple-way decisions.
#     Another option is to use elif, which, by combining "an else followed immediately by an if into a single clause,"
#     "preserves the semantics of nested structures but gives it a more appealing look."

#  8. There is usually only one correct solution to a problem involving decision structures. FALSE
#     [Explanation: p.235: "Algorithms that incorporate decisions can become quite complicated as decision structures
#     are nested. Usually a number of solutions are possible, and careful thought should be given to produce a
#     correct, efficient, and understandable program."]

#  9. The condition x <= y <= z is allowed in Python. TRUE
#     [Explanation: p.228: "The condition x1 >= x2 >= x3 does not match the template for conditions shown above.
#     Most computer languages would not accept this as a valid expression. It turns out that Python does allow this
#     compound condition, and it behaves exactly like the mathematical relations x1 >= x2 >= x3.

# 10. Input validation means prompting a user when input is required. FALSE
#     [Explanation: p.262 (from Ch.8, section on post-test loop): "Suppose you are writing an input algorithm that is
#     supposed to get a non-negative number from a user. If the user types an incorrect input, the program asks for
#     another value. It continues to reprompt unitl the user enters a valid value. This process is called input
#     validation. Well-engineered programs validate inputs whenever possible."]

## Multiple Choice

#  1. A statement that controls the execution of other statements is called a
#     a) boss structure     b) super structure
#     c) control sructure   d) branch

#  2. The best structure for implementing a multi-way decision in Python is
#     a) if     b) if-else     c) if-elif-else     d) try

#  3. An expression that evalutes to either true or false is called [D]
#     a) operational     b) Booelan     c) simple     d) compound

#  4. When a program is being run directly (not imported), the value of __name__ is
#     a) script     b) main     c) __main__     d) True

#  5. The literals for type bool are
#     a) T, F     b) True, False     c) true, false     d) 1, 0

#  6. Placing a decision inside of another decision is an example of [C]
#     a) cloning     b) spooning     c) nesting     d) procrastination

#  7. In Python, the body of a decision is indicated by
#     a) indentation     b) parentheses     c) curly braces     d) a colon

#  8. A structure in which one decision leads to another set of decisions, which leads to another
#     set of decisions, etc. is called a decision [C]
#     a) network     b) web     c) tree     d) trap

#  9. Taking the square root of a negative value with math.sqrt produces a(n)
#     a) ValueError     b) imaginary number
#     c) program crash  d) stomachache

# 10. A multiple choice question is most similar to
#     a) simple decision     b) two-way decision
#     c) multi-way decisions d) an excpetion handler 

## Discussion

#  1.


### PROGRAMMING EXERCISES
