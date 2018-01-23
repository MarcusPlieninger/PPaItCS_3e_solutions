#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 10: Defining Classes
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. New objects are created by invoking a constructor. TRUE
#     [Explanation: p.314: "New objects are created from a class by invoking a constructor."]

#  2. Functions that live in objects are called instance variables. FALSE
#     [Explanation: p.518: "instance variable: a piece of data stored inside an object."
#     p.314: "The operations, called methods, are functions that 'live' inside the object."]

#  3. The first parameter of a Python method definition is called this. FALSE
#     [Explanation: p.323: "Let's look at the three methods defined in this class. You'll notice that each
#     method has a first parameter named self. The first parameter of a method is special--it always contains
#     a reference to the object on which the method is acting. As usaul, you can use any name you want for this
#     parameter, but the traditional name is self, so that is what I will always use." There is an additional
#     explanation as to why on this page.]

#  4. An object may have only one instance variable. FALSE
#     [Explanation: There is no set number of instance variables an object may have. This is illustrated
#     throughout the book.]

#  5. In data processing, a collection of information about a person or thing is called a file. FALSE
#     [Explanation: p.327: "A grouping of information of this sort is called a record."]

#  6. In a Python class, the constructor is called __init__. TRUE
#     [Explanation: p.324: "Certain methods in a class have special meaning to Python. These methods have
#     names that begin and end with two underscores. The special method __init__ is the object constructor."]

#  7. A docstring is the same thing as a comment. FALSE
#     [Explanation: p.333-4 "The advantage of docstrings is that, while ordinary comments are simply ignored by
#     Python, docstrings are actually carried along during execution in a special attribute called __doc__. These
#     strings can be examined dynamically. ... Most of the Python library modules have extensive docstrings that you
#     can use to get help on using the module or its contents. ... Docstrings are alos used by the Python online
#     help system by a utility called pydoc that automatically builds documentation for Python modules."]

#  8. Instance variables go away once a method terminates. FALSE
#     [Explanation: This statement is true only of local function variables.
#     p.324: "The power of instance variables is that we can use them to remember the state of a particular object,
#     and this information then gets passed around the program as part the object. The values of instance variables
#     can be referred to again in other methods or even in successive calls to the same method. This is different
#     from regular local function variables, whose values disappear once the function terminates."]

#  9. Method names should always begin with one or two underscores. FALSE
#     [Explanation: See question 6. However, method names could begin with one underscore since this is part of the
#     convention for identifiers.]

# 10. It is considered bad style to directly access an instance variable outside of a class definition. TRUE
#     [Explanation: p.332: "Accessing the instance variables of an object is very handy for testing purposes, but
#     it is generally considered poor practice to do this in programs. One of the main reasons for using objects
#     is to hide the internal complexities of those objects from the programs that use them. References to instance
#     variables should generally remain inside the class definition with the rest of the implementation details.
#     From outside the class, all interaction with an object should generally be done using the interface provided
#     by its methods. However, this is not a hard-and-fast rule, and Python program designers often specify that
#     certain instance variables are accessible as part of the interface. In fact, Python provides an interesting
#     mechanism called 'properties' that makes providing access to instance variables safe and elegant." See Python
#     documentation.]

## Multiple Choice

#  1.

## Discussion

#  1.


### PROGRAMMING EXERCISES
