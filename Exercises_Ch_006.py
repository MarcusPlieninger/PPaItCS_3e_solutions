#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 6: Defining Functions
#### End-of-Chapter Exercises

### REVIEW QUESTIONS

## True/False

#  1. Programmers rarely define their own functions. FALSE
#     [Explanation: If this were true, programming would be boring. p.175: "[Programmers] design [their] own
#     own functions to make [their] programs easier to write and understand."

#  2. A function may only be called at one place in a program. FALSE
#     [Explanation: p.177: "The basic idea of a function is that we write a sequence of statements and give
#     that sequence a name. The instructions can then be executed at any point in the program by referring
#     to the function name. The part of the program that creates a function is called a function definition.
#     When a function is subsequently used in a program, we say that the definition is called or invoked. A
#     single function definition may be called at many different points of a program."]

#  3. Information can be passed into a function through parameters. TRUE
#     [Explanation: p.195: "...the formal parameters of a function only recevive the values of the actual
#     parameters."]

#  4. Every Python function returns some value. TRUE
#     [Explanation: p.192: "Technically, all functions in Python eturn a value, regardless of whether the
#     function actaully contains a return statement. Functions without a return always hand back a special
#     object, denoted None."]

#  5. In Python, some parameters are passed by reference. FALSE
#     [Explanation: p.195: "In programming language parlance, Python passes all parameters by value. ...
#     ...Python does not allow passing parameters by reference...".]

#  6. In Python, a function can return only one value. FALSE
#     [Explanation: p.192: "Sometimes a function needs to return more than one value. This can be done by simply
#     listing more than one expression in the return statement."]

#  7. Python functions can never modify parameters. FALSE
#     [Note: This is true of OOP languages in general, I think, as opposed to functional programming languages.
#     Explanation: p.193: "In some cases, functions can also communicate back to the calling program by making
#     changes to the function parameters."]

#  8. One reason to use functions is to reduce code duplication. TRUE
#     [Explanation: p.177 "Funcations can be used to reduce code duplication and to make programs more
#     understandable and easier to maintain."]

#  9. Variables defined in a function are local to that function. TRUE
#     [Explnation: p.183: "Scope refers to the places where a given variable may be referenced. Remember, each
#     function is its own little subprogram. The variables used inside on fuction are local to that function,
#     even if they happen to have the same name as variables that appear inside another function.
#     p.185: "Variables with identical names elsewhere in the program are distinc from the formal parameters
#     and variables inside the function body."]

# 10. It's a bad idea to define new functions if it makes a program longer. FALSE
#     [Explanation: p.199: "So far, we have been discussing functions as a mechanism for reducing code
#     duplication, thus shortening and simplifying our programs. Surprisingly, functions are often used even
#     when doing so actually makes a program longer. A second reason for using functions is to make programs
#     more modular."]

## Multiple Choice

#  1.  The part of a program that uses a function is called the [B]
#      a) user  b) caller  c) callee  d) statement
#      [Explanation:

#  2.  A Python function definition begins with [A]
#      a) def  b) define  c) function  d) defun

#  3.  A function can send output back tot the program with a(n) [A]
#      a) return  b) print  c) assignment  d) SASE

#  4.  Formal and actual parameters are matched up by [B]
#      a) name  b) position  c) ID  d) interests

#  5.  Which of the following is not a step in the function-calling process? [D]
#      a) The calling program suspends.
#      b) The formal parameters are assigned the value of the actual parameters.
#      c) The body of the function executes.
#      d) Control returns to the point just before the function was called.

#  6. In Python, actual parameters are passed to functions [A]
#     a) by value  b) by reference  c) at random  d) by networking

#  7. Which of the following is not a reason to use functions? [D]
#     a) to reduce code duplication
#     b) to make a program more modular
#     c) to make a program more self-documenting
#     d) to demosntrate intellectual superiority

#  8. If a function returns a value, it should generally be called from [A]
#     a) an expression  b) a different program
#     c) main           d) a cell phone

#  9. A function with no return statment returns [D]
#     a) nothing  b) its parameters  c) its variables  d) None

# 10. A function can modify the value of an actual parameter only if it's [A]
#     a) mutable  b) a list  c) passed by reference  d) a variable

## Discussion

#  1. In your own words, describe the two motivations for defining functions in your programs.

#  2. We have been thinking about computer programs as sequences of instructions where the computer methodically
#     executes on instruction and then moves on to the next one. Do programs that contain functions fit this model?
#     Explain your answer.

#  3. Parameters are an important concept in defining functions.
#     a) What is the purpose of parameters?
#     b) What is the difference between a formal parameter and an actual parameter?
#     c) In what ways are parameters similar to and different from ordinary variables?

#  4. Functions can be thought of as miniature (sub)programs inside other programs. Like any other programs, we can
#     think of functions as having input and output to communicate with the main program.
#     a) How does a program provide "input" to one of its functions?
#     b) How does a function provide "output" to the program?

#  5. Consider this very simple function:
#     def cube(x):
#         answer = x * x * x
#         return answer
#     a) What does this function do?
#     b) Show how a program could use this function to print the value of y^3, assuming y is a variable.
#     c) Here is a fragment of a program that uses this function:
#        answer  = 4
#        result = cube(3)
#        print(answer, result)
#        The output from this fragment is 4 27. Explain why the output is not 27 27, even though cube seems to change
#        the value of answer to 27.


### PROGRAMMING EXERCISES

#  1. Write a program to print the lyrics of the song "Old MacDonald." Your program should print the lyrics for five
#     different animals, similar to the example verse below.
#
#     Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!
#     And on that farm he had a cow, Ee-igh, Ee-igh, Oh!
#     With a moo, moo here and a moo, moo there.
#     Here a moo, there a moo, everywhere a moo, moo.
#     Old MacDonald had a farm, Ee-igh, Eeigh, Oh!

def refrain():
    print("Old MacDonald had a farm, Ee-igh, Ee-igh, Oh!")

def animal(kind, noise):
    refrain()
    print("And on that farm he had a " kind "Ee-igh, Ee-igh, Oh!")
    print("With a " noise", " noise " here and a " noise", " noise " there.")
    print("Here a " noise ", there a " noise ", everywhere a " noise ".")
    refrain()

def main:
    animal("pig", "oink")
    print()
    animal("duck", "quack")
    print()
    animal("sheep", "baah")
    print()
    animal("cow", "moo")
    print()
    animal("dog", "woof")

#  2. Write a program to print the lyrics for ten verses of "The Ants Go Marching." A couple of sample versus are given below.
#     You may choose your own activity for the "little one" in each verse, but be sure to choose something that makes the rhyme
#     work (or almost work).

#  3. Write definitions for these functions:

#  4.

#  5.

#  6.

#  7.

#  8.

#  9.

# 10.

# 11.

# 12.

# 13.

# 14.

# 15.

# 16.

# 17.

# 9.

#10.





    
    





    
