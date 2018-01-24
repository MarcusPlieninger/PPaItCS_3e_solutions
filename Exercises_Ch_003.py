#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 3: Computing with Numbers
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. Information that is stored and manipulated by computers is called data. TRUE
#     [Explanation: p.57 "The information that is stored an amnipulated by computer program is
#     gneerically rferred to as data. Different kinds of data will be stored and manipulated in
#     different ways."

#  2. Since floating-point numbers are extremely accurate, they generally be used instead of ints. FALSE
#     [Explanation: p.59 "Another difference between ints and floats is hat the float type can only
#     represent approximations of real numbers. As we will see, there is a limit to the precision, or
#     accuracy of the stored values. Since float values are not exact, while ints always are, your general
#     rule of thumb should be: If you don't need fractional values, use an int.]

#  3. Operations like addition and subtraction are defined in the math library. FALSE
#     [Explanaiton: p.60, see table of built-in numeric operations in Python. These include addition,
#     subtraction, multiplication, float division, exponentiation, absolute value, integer division,
#     and remainder.]

#  4. The number of possible arrangements of n items is equalt to n!. TRUE
#     [Explanation: p.68 With 6 items, there are 720 different ways of ordering them, i.e. 6!.

#  5. The sqrt function computes the squirt of a number. FALSE
#     [Explanation: The sqrt function computes the square root of a number.]

#  6. The float data type is identical to the mathematical concept of a real number. FALSE
#     [Explanation: Floats are approximations of real numbers. See p.59: "Another difference between ints
#     and floats is that the float type can only represent approximations to real numbers." This has to
#     do with how floats are stored. See p.74 for explanation. Be able to explain this in-depth and simply.]

#  7. Computers represent numbers using base-2 (binary) representations. TRUE
#     [Explanation: p.72-3 "Computer memory is composed of electrical 'switches,' each of which can be
#     in one of two possible states, basically on or off. Each switch represents a binary digit or bit
#     of information. One bit can encode two possibilities, usually represented with the numberals 0 (for off)
#     and 1 (for on)."

#  8. A hardware float can represent a larger range of values than a hardware int. TRUE
#     [Explanation: p.74 "Using a float allows us to represent a much larger range of values than a 32-bit
#     int, but the amoutn of precision is still fixed."]

#  9. Type conversion functions such as float are a safe alternative to eval for getting a number
#     as user input. TRUE
#     [Explanation: p. 65 "Using int instead of eval in the input statements ensures that a user may
#     only enter valid whole numbers. Any illegal (non-int) inputs will cause the program to crash with
#     an erro message, thus avoiding the risk of a code injection attack...."]

# 10. In Python, 4+5 produces the same result type as 4.0+5.0. FALSE
#     [Explanation: p.60 "Python chooses the appropriate underlyng operation (int or float) based on the
#     operands."]

## Multiple Choice

#  1. Which of these is not a built-in Python data type? [C]
#     a) int     b) float     c) rational     d) string
#     [Explanation: 

#  2. Which of the following is not a built-in operation? [D]
#     a) +     b) %     c) abs()     d) sqrt()
#     [Explnaation: sqrt() "lives" in the math library. See p.

#  3. In order to use functions in the math library, a program must include [D]
#     a) a comment     b) a loop     c) an operator     d) an import statement
#     [Explanation

#  4. The value of 4! is [B]
#     a) 9     b) 24     c) 41     d) 129
#     [Explanation: 4 * 3 * 2 * 1 = 24

#  5. The most appropriate data type for storing the value of pi is [B]
#     a) int     b) float     c) irrational     d) string
#     [Explanation:

#  6. The number of distinct values that can be represented using 5 bits is [C]
#     a) 5     b) 10     c) 32     d) 50
#     [Explanation: p.73: "In general, n bits can represent 2^n different values."]

#  7. In a mixed-type expression involving ints and floats, Python will convert [C]
#     a) floats to ints                    b) ints to strings
#     b) both floats and intos to strings  c) ints to floats
#     [Explanation: p.62-3: "In general, converating a float to an int is a dangerous step, because
#     some information (the fractional part) will be lost. On the other hand, an int can be safely
#     tunred into a float just by adding a fractional part of .0. So in mixed-type expressions, Python
#     will automatically convert ints to floats and perform floating-point operations to produce
#     a float result."]

#  8. Which of the following is not a Python type-conversion function? [B]
#     a) float     b) round     c) int     d) abs
#     [Explanation: p.60: abs is a built-in numberic operator that returns the absolute value. This is not
#     type-conversion. p.75: "Programs may explicitly convert one data type into another using the functions
#     float(), int(), and round()."]

#  9. The pattern used to compute factorials is [A]
#     a) accumulator         b) input, process, output
#     c) breaks the computer d) uses more memory
#     [Explanation: p.69: "Now let's try to think to think about the algorithm [to take a factorial of a number]
#     more generally. What is actually goin on here? We are doing repeated multipliations, and as we go along,
#     we keep track of the running product. This is a very common algorithmic pattern called an accumulator. We
#     build up, or accumulate, a final value piece by pice. To accomplish this in a program, we will use an
#     accumulator variable and a loop structure."]

# 10. In modern Python, an int value that grows larger than the underlying hardware int [D]
#     a) causes an overflow     b) converts to float
#     c) breaks the computer    d) uses more memory
#     [Explanation: p.74-5: A Python int is not a fixed size, but expands to accomodate whatever value it holds. The
#     only limit is the amount of memory the computer has available to it. When the value is small, Python can just use
#     the computer's underlying int representation and operations. When the value gets larger, Python automatically converts
#     to a represetnation using more bits. Of course, in order to perform operations on larger numbers, Python has to break
#     down the operations into smaller units that the computer hardware is able to handle--similar to the way you might do
#     long division by hand. These operations will not be as efficient (they requrie more steps), but they allow our Python
#     ints to grow to arbitrary size."]

## Discussion

#  1.

#  2.

#  3.

#  4.

#  5.

#  6.


### PROGRAMMING EXERCISES

#  1.

#  2.

#  3.

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


