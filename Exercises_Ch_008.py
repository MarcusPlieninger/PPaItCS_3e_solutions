# Chapter 8 Exercises
##### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
##### Chapter 8: Loop Structures and Booleans
##### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. A Python while implements a definite loop. FALSE
#     [Explanation: p.245 "An indefinite [or conditional] loop keeps iterating until certain
#     conditions are met. There is no guarantee ahead of time regarding how many times the loop
#     will go around. In Python, an indefinite loop is implemented using a while statement."
#     p. 245: "...the for loop (in its usual form) is a definite loop, and that means the number
#     of iterations is determined when the loop starts."]

#  2. The counted loop pattern uses a definite loop. TRUE
#     [Explanation: p.45 (Ch.2, Section 2.6): "[the counted loop pattern]...is a very common way to
#     to use definite loops. When you want to do something in your program a certain number of times
#     use a for loop with a suitable range."]

#  3. A sentinel loop asks the user whether to continue on each iteration. FALSE
#     [Explanation: See question 4 below for explanation of sentinel loop. p.247-8: "One good use
#     of the indefinite loop is to write interactive loops. The idea behind an interactive loop is
#     that it allows the user to repeat certain portions of a program on demand."]

#  4. A sentinel loop should not actually process the sentinel value. TRUE
#     [Explanation: p.249: A sentinel loop continues to process data until reaching a special value
#     that signals the end. The special value is called the sentinel. Any value may be chosen for
#     for the sentinel. The only restriction is that it be distinguishable from actual data values.
#     The sentinel is not processed as part of the daa."]

#  5. The easiest way to iterate through the lines of a file in Python is to use a while loop. ?

#  6. A while is a post-test loop. FALSE [not sure]
#     [Explanation: p.263: "Unlike some other languages, Python does not have a statement that directly
#     implements a post-test loop." p.245: "In Python, an indefinite loop is implemented using a while
#     statement."]

#  7. The Boolean operator or returns True when both of its operands are true. TRUE
#     [Explanation: p.261: See truth table. Or returns true when either of its operands are true,
#     as well.]

#  8. a and (b or c) == (a and b) or (a and c) TRUE
#     [Note: I am assuming that parentheses are not needed to enclose each statement.
#     Explanation: p.260 "Both and and or distribute over each other. See truth table below.]
#     a  b  c  (b or c)   (a and (b or c)   (a and b)   (a and c)   ((a and b) or (a and c))
#     T  T  T      T              T              T           T                  T
#     F  T  T      T              F              F           F                  F
#     T  F  T      T              T              F           T                  T
#     T  T  F      T              T              T           F                  T
#     F  F  T      T              F              F           F                  F
#     T  F  F      F              F              F           F                  F
#     F  T  F      T              F              F           F                  F
#     F  F  F      F              F              F           F                  F
    

#  9. not(a or b) == (not a) or not(b) FALSE
#     [Note: I am assuming there is no differnece between (not a) and not(a).
#     Explanation: See truth table below. p.261: This identity dceptively alters DeMorgan's Laws.
#     It would be true if the disjunctive in the first statement would be replaced by the conjunctive.]
#     a     b     a or b     not(a or b)     (not a)     not(b)     (not a) or not(b)
#     T     T       T             F             F          F                F
#     T     F       T             F             F          T                T
#     F     T       T             F             T          F                T
#     F     F       F             T             T          T                T                       

# 10. True or False TRUE
#     [Explanation: p.257: "The or of two expressions is true when either expression is true."
#     Accoridng to boolean algebra, this statement evaluates to true.]

## Multiple Choice

#  1. A loop pattern that asks the user whether to continue on each iteration is called a(n) [A]
#     a) interactive loop     b) end-of-file loop
#     c) sentinel loop        d) infinite loop

#  2. A loop pattern that continues until a special value is input is called a(n) [?]
#     a) interactive loop     b) end-of-file loop
#     c) sentinel loop        d) infinite loop

#  3. A loop structure that tests the loop condition after executing the loop body is called a [D]
#     a) pre-test loop        b) loop and a half
#     c) sentinel loop        d) post-test loop

#  4. A priming read is part of the pattern for a(n) [?]
#     a) interactive loop     b) end-of-file loop
#     c) sentinel loop        d) infinite loop

#  5. What statement can be executed in the body of a loop to cause it to terminate? [C]
#     a) if     b) input     c) break     d) exit

#  6. Which of the following is not a valid rule of Boolean algebra? [A]
#     a) (True or x) == True
#     b) (False and x) == False
#     c) not (a and b) == not(a) and not(b)
#     d) (True or False) == True

#  7. A loop that never terminates is called [D]
#     a) busy   b) indefinite c) tight d) infinite

#  8. Whic line would not be found in a truth table for and? [B}
#     a) TTT b) TFT c) FTF d) FFF

#  9. Which line would not be found in a truth table for or [C]
#     a) TTT b) TFT c) FTF d) FFF

# 10. The term for an operator that may not evaluate one of its subexpressions is [?]
#     a) short-circuit b) faulty c) exclusive d) indefinite

## Discusion

#  1. Compare and contrast the following pairs of terms:
#     a) definite loop vs. indefinite loop
#     b) for loop vs. while loop
#     c) interactive loop vs. sentinel loop
#     d) sentinel loop vs. end-of-file loop

#  2. Give a truth table that shows the Boolean value of each of the following Boolean expressions, for every possible
#     of "input" values. Hint: Including columns for intermediate expressions is helpful.
#     a) not (P and Q)
#
#     P | Q | P and Q | not (P and Q) |
#     ---------------------------------
#     T | T |    T    |       F       |
#     T | F |    F    |       T       |
#     F | T |    F    |       T       |
#     F | F |    F    |       T       |

#     b) (not P) and Q
#
#     P | Q |  not P  | (not P) and Q |
#     ---------------------------------
#     T | T |    F    |       F       |
#     T | F |    F    |       F       |
#     F | T |    T    |       T       |
#     F | F |    T    |       F       |

#     c) (not P) or (not Q)
#
#     P | Q |  not P  |     not Q     |  (not P) or (not Q) |
#     -------------------------------------------------------
#     T | T |    F    |       F       |          F
#     T | F |    F    |       T       |          T
#     F | T |    T    |       F       |          T
#     F | F |    T    |       T       |          T

#     d) (P and Q) or R ?

#     P | Q | (P and Q) | R |
#     -------------------------------------------------------
#     T | T |     T     | F
#     T | F |     F     | T
#     F | T |     F     |
#     F | F |     F     |
#     

#     e) (P or Q) and (Q or R)

#  3. Write a while loop fragment that calculates the following values:
#     a) Sum of the first n counting numbers: 1 + 2 + 3 + ... + n
#     b) Sum of the first n odd numbers: 1 + 3 + 5 + ... + 2n - 1
#     c) Sum of a series of numbers entered by the user until the value 999 is entered. Note: 999 should not be part of the sum.
#     d) The number of times a whole number n can be divided by 2 (using integer division) before reaching 1 (i.e., log2n).


## Programming Exercises

# 1. The Fibonaccis sequence starts 1, 1, 2, 3, 5, 8 ... . Each number in the sequence (after the first two) is the sum of the
#    previous two. Write a program that computes and outputs the nth Fibonnaci number, where n is a value entered by the user.
     # Solution:
     # fibonnaci.py
     # a program that outputs the nth fibonnaci number where n is supplied by user
     define main():
         print("This program computes a Fibonacci number.") 
         n=int(input("Please enter what term in the Fibonnaci sequence you would like to know."))
         for i in range (n):
             (i + (i - 1))
             
             
