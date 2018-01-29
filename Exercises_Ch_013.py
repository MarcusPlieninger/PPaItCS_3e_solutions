#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 13: Algorithm Design and Recursion
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. Linear search requires a number of steps proportional to the size of the list being searched. TRUE
#     [Explanation: p. 464 "Let's consider linear search first. If we have a list of ten items, the most
#     work our algorithm might have to do is to look at each item in turn. The loop will iterate at most
#     ten times. Suppose the list is twice as big. Then it might have to look at twice as many items. If
#     the list is three times as large, it will take three times as long, etc. In general, the amount of
#     time required is linearly related to the size of the list n. This is what computer scientists call
#     a linear time algorithm. Now you really know why it's called a linear search."]

#  2. The python operator in performs a binary search. FALSE
#     [Explanation: p. 461 "The Python in and index operations both implement linear searching algorithms."]

#  3. Binary search is an n log n algorithm. FALSE
#     [Explanation: p. 464 "If the binary search loops i times, it can find a single value in a list size
#     of 2^i. Each time through the loop, it looks at one value (the middle) in the list. To see how many
#     are examined in a list of size n, we need to solve this relationship: n = 2^i for i. In this formula,
#     i is just an exponent with a base of 2. Using the appropriate logarithm gives us this relationship:
#     i = log2n [note 2 is subscript]. If you are not comfortable with logarithms, just remember that this
#     value is the number of times that a colleciton of size n can be cut in half."]

#  4. The number of times n can be divided by 2 is exp(n). FALSE
#     [Explanation: See above. The number of times n can be divided by 2 is log2n [note 2 is subscript].]

#  5. All proper recursive definitions must have exactly one non-recursive base case. FALSE
#     [Explanation: p.467 "There are one or more base cases for which no recursion is required."
#     Note that a "base case" refers to a case that "doesn't require another application of the definition,"
#     i.e. "when the recursion bottoms out" and "we get a closed expression that can be directly computed."]

#  6. A sequence can be viewed as a recursive data collection. TRUE

#  7. A word of length n has n! anagrams. TRUE
#     [Explanation: p. 472 "The number of anagrams of a word is the factorial of the length of the word."]

#  8. Loops are more general than recursion. FALSE [Note: still don't understand this]
#     [Explanation: p.474 "In fact, recursive functions are a generalization of loops. Anything that can be
#     with a loop can be done by a simple kind of recursive function."] 

#  9. Merge sort is an example of n log n algorithm.
#     [Explanation: p.483 "Therefore, the total work required to sort n items is n log 2 n [Note: 2 is subscript].
#     Computer scientists call this an n log n algorithm."]

# 10. Exponential algorithms are generally considered intractable. TRUE
#     [Explanation: p.489 "Computer scientists call this an exponential time algorithm, since the measure of
#     the size of the problem, n, appears in the exponent of this formula. Exponential algorithms blow up
#     very quickly and can only be practically solved for relatively small sizes, even on the fastest
#     computers....Even though the algorithm for Tower of Hanoi is easy to express, it belongs to a class
#     known as intractable problems. These are problems that require too much computing power (either time
#     or memory) to be solved in practice, except for the simplest cases."]


## Multiple Choice

#  1. Which algorithm requires time directly proportional to the size of the input? [A]
#     a) linear search     b) binary search
#     c) merge sort        d) selection sort

#  2. Approximately how many iterations will binary search need to fin a value in a list of 512 items? [C]
#     a) 512     b) 256     c) 9     d) 3

#  3. Recursions on sequences often use this as a base case: [a]
#     a) 0     b) 1     c) 9     d) 3

#  4. An infinite recursion will result in
#     a) a program that "hangs"
#     b) a broken computer
#     c) a reboot
#     d) a run-time exception

#  5. The recursive Fibonnaci sequences is inefficient because [A]
#     a) It does not many repeated computations
#     b) recursion is inherently inefficient compared to iteration
#     c) calculating Fibonacci numbers is intractable
#     d) fibbing is morally wrong

#  6. Which is a quadratic time algorithm?
#     a) linear search     b) binary search
#     c) Tower of Hanoi    d) selection sort

#  7. The process of combining two sorted sequences is called [D]
#     a) sorting     b) shuffling     c) dovetailing     d) merging

#  8. Recursion is related to the mathematical technique called [B]
#     a) looping     b) sequencing     c) induction     d) contradiction

#  9. How many steps would be needed to solve the Tower of Hanoi for a tower of size 5? [D]
#     a) 5     b) 10     c) 25     d) 31

# 10. Which of the following is not true of the halting problem? [B]
#     a) It was studied by Alan Turing.
#     b) It is harder than intractable.
#     c) Someday a clever algorithm may be found to solve it.
#     d) It involves a program that analyzes other programs.


## Discussion

#  1. Places these algorithm classes in order from fastest to slowest:
#   n log n, n, n^2, log n, 2^n.

#  2. In your own words, explain the two rules that a proper recursive definition or function must follow.

#  3. What is the exact result of anagram("foo")?

#  4. Trace recPower(3,6) and figure out exactly how many multiplications it performs.

#  5. Why are divide-and-conquer algorithms often very efficient?


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












        




