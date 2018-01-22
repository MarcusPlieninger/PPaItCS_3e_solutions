#### "Python Programming: An Introduction to Computer Science, Third Edition" by John Zelle
#### Chapter 5: Sequnces: Strings, Lists, and Files
#### End-of-Chapter Exercises


### REVIEW QUESTIONS


## True/False

#  1. A Python string literal is always enclosed in double quotes. FALSE
#     [Explanation: p. 130 "In Chapter 2 you learned that a string literal is formed by enclosing some
#     characters in quotation marks. Python also allows strings to be delineated by single quotes
#     (apostrophes). There is no difference; just be sure to use a matching set."]

#  2. The last charcter of a string s is at position len(s) TRUE
#     [Explanation: p. 131 "Notice that in a string of n characters, the last character is at position
#     n -1, because the index starts at 0. "]

#  3. A string always contains a single line of text. FALSE
#     [Explanation: A string is a sequence of characters. This sequence can be of any length. In fact,
#     it is also possible to have an empty string, i.e. "".]

#  4. In Python, "4" + "5" is "45". TRUE
#     [Explanation: This is not a a case of using the addition operator on integers. Since the literals are
#     enclosed in double quotations, we know that we are dealing with values of the data type string. The
#     operator + thus indicates the string operation, concatenation.]

#  5. Python lists are mutable, but strings are not. TRUE
#     [Explanation: p.138 "While strings and lists are both sequences, there is an important difference
#     between the two. Lists are mutable. That means that the value of an item in a list can be modified
#     with an assignment statement. Strings, on the other hand, cannot be changed 'in place.'"]

#  6. ASCII is a standard from representing characters using numeric codes. TRUE
#     [Explanation: p.140 "To avoid this sort of problem, computer systems today use industry standard
#     encodings. One important standard is called ASCII (American Standard Code for Information Interchange).
#     ASCII uses the numbers 0 through 127 to represent characters typically found on an (American) computer
#     keyboard, as well as certain special values known as control codds that are used to coordinate the sending
#     and receiving of information.]

#  7. The split method breaks a string into a list of substrings, and join does the opposite. FALSE
#     [Explanation: p.144 "For our decoder, we will make use of the split method. This method splits a string into
#     a list of substrings. By default, it will split the string whever a space occurs. p. 148 see table.]

#  8. A substitution cipher is a good way to keep sensitive information secure. FALSE
#     [Explanation: p.150 "Our simple encoding/decoding programs use a very weak form of encryption known as a
#     substituation cipher....Since each letter is always encoded by the same symbol, a codebreaker coud use
#     statistical inofrmation about the frequency of various letters and some simple trial and error testing to
#     discover the original message."]

#  9. The add method can be used to add an item to the end of a list. FALSE
#     [Explanation: p.147 "The append method can be used to add an item at the end of a list. This is often used to
#     build a list an item at a time.]

# 10. The process of associating a file with an object in a program is called "reading" the file. FALSE
#     [Explanation: p.159 "We need some way to associate a file on disk with an object in a program. This process
#     is called opening a file. Once a file has been opened, its contents can be accessed through the associated
#     file object.]

## Multiple Choice

#  1. Accessing a single character out of a string is called: [D]
#     a) slicing     b) concatenation     c) assignment     d) indexing

#  2. Which of the following is the same as s[0:-1] [C]
#     a) s[-1]     b) s[:]     c) s[:len(s)-1]     d) s[0:1len(s)]

#  3. What function gives the Unicode value of a character? [A]
#     a) ord     b) ascii     c) chr     d) eval
#     [Explanation p.140 "Python provides a couple of built-in functions that allow us to switch back
#     and forth between characters and the numberic values used to represent them in strings. The ord
#     function returns the numeric ("ordinal") code of a single-character string, while chr goes the
#     other direction."]

#  4. Which of the following can not be used to convert a string of digits into a number? [D]
#     a) int     b) float     c) str     d) eval

#  5. A sucessor to ASCII that includes characters from (nearly) all written languages is [C]
#     a) TELLI     b) ASCII+ +     c) Unicode     d) ISO
#     [Explanation: p.140 "Most modern systems are moving to Unicode, a much larger standard that
#     aims to include the characters of nearly all written languages."]

#  6. Which string method converts all the characters of a string to upper case? [D]
#     a) capitalize     b) capwords     c) uppercase     d) upper
#     [Explanation: p.147 see example. p.148: see table.]

#  7. The string "slots that are filled in by the format method are marked by: [D]
#     a) %     b) $     c) []     d) {}
#     [Explanation: p.156 "Curly braces ({}) inside the template-string mark 'slots' into which the
#     provided values are inserted. The information inside the curly braces tells which value goes in
#     the slot and how the value should be formatted.]

#  8. Which of the following is not a file-reading method in Python? [C]
#     a) read     b) readline     c) readall     d) readlines
#     [Explanation: p.161 "Python provides three related operations for reading information from a
#     file [read, readline, readlines]."]

#  9. The term for a program that does its input and output with files is [C]
#     a) file-oriented     b) multi-line     c) batch     d) lame

# 10. Before reading or writing to a file, a file object must be created via
#     a) open     b) create     c) File     d) Folder


## Discussion

#  1. Given the initial statements:
#
#     s1 = "spam"
#     s2 = "ni!"
#
#     Show the result of evaluating each of the following string expressions.
#                                        Expected                   | Actual
#     a) "The Knights who say, " + s2    The Knights who say ni!    |
#     b) 3 * s1 + 2 * s2                 spamspamspamni!ni!         |
#     c) s1[1]                           pam                        |
#     d) s1[1:3]                         pam                        | 
#     e) s1[2] + s2[:2]                  aspa                       |
#     f) s1 + s2[-1]                     spam!                      |
#     g) s1.upper()                      SPAM                       | 
#     h) s2.upper().1just(4) * 3         ?

#  2. Given the same initial statements as in the previous problem, show a Python expression that
#     that could construct each of the following results by performing string operations on s1 and s2.

#     a) "NI"
#     b) "ni!spamni!"
#     c) "Spam Ni! Spam Ni! Spam Ni!"
#     d) "spam"
#     e) ["sp","m"]
#     f) "spm"

#  3. Show the output that would be generated by each of the following program fragments.

#     a) for ch in "aardvark":
#            print(ch)

#     b) for w in "Now is the winter of our discontent...".split():
#            print(w)

#     c) for w in "Mississippi".split("i"):
#            print(w, end=" ")

#     d) msg = ""
#        for s in "secret".split("e"):
#            msg = msg + s

#     e) msg = ""
#        for ch in "secret":
#        msg = msg + chr(ord(ch)+1)
#        print(msg)

#  4. Show the string that would result from each of the following string formatting operations. If the
#     operation is not legal, explain why:

#     a) "Looks like (1) and (0) for breakfast".format("eggs", "spam")

#     b) "There is {0} {1} {2} {3}".format(1, "spam", 4 "you")

#     c) "Hello {0}".format("Susan", "Computewell")

#     d) "{0:0.2f} {0:0.2f}".format(2.3, 2.3468)

#     e) "{7.5f} {7.5f}".format(2.3, 2.3468)

#     f) "Time left {0:02}:{1:05.2f}".format(1, 37.374)

#     g) "{1:3}".format("14")



#  5. Explain why public key encryption is more useful for securing commmunications on the Internet than
#     private (shared) key encryption.




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
