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
#     a) "The Knights who say, " + s2    The Knights who say ni!    | 'The Knights who say ni!'
#     b) 3 * s1 + 2 * s2                 spamspamspamni!ni!         | 'spamspamspamni!ni!'
#     c) s1[1]                           pam                        | 'p'      [Careless mistake]
#     d) s1[1:3]                         pam                        | 'pa'     [Careless mistake]
#     e) s1[2] + s2[:2]                  aspa                       | 'ani'    [Careless mistake]
#     f) s1 + s2[-1]                     spam!                      | 'spam!'
#     g) s1.upper()                      SPAM                       | 'SPAM'
#     h) s2.upper().ljust(4) * 3         NI! NI! NI!                | 'NI! NI! NI! '
#
#     [Note on single quotes that Python returns when evaluating string expressions:
#     The difference between string object and the actual printed output is that the string object
#     is not enclosed in any quotations when it is printed. The Python shell shows the vlaue of strings
#     qua strings by enclosing them in single quotes. See p.131]

#  2. Given the same initial statements as in the previous problem, show a Python expression that
#     that could construct each of the following results by performing string operations on s1 and s2.

#     a) "NI"                            s2.upper()                               | s2[0:2].upper()      
#     b) "ni!spamni!"                    s2 + s1 + s2                             | same
#     c) "Spam Ni! Spam Ni! Spam Ni!"    ((" "join.([s1, s2] ) * 3).capitalize()  | ?
#     d) "spam"                          s1                                       |
#     e) ["sp","m"]                      s1.split("a")                            | same
#     f) "spm"                           s1[0:2] + s1[-1]                         | correct

#     [The code above yieldes the results in single quotes. How would I change the code to produce
#     double quotes as the results which have double quotes?]

#  3. Show the output that would be generated by each of the following program fragments.

#     a) for ch in "aardvark":
#            print(ch)
#        Output:
#        Expected                                 |  Actual
#        a
#        a
#        r
#        d
#        v
#        a
#        r
#        k


#     b) for w in "Now is the winter of our discontent...".split():
#            print(w)
#        Output:
#        Expected                                 |
#        Nowisthewinterofourdiscontent...

#     c) for w in "Mississippi".split("i"):
#            print(w, end=" ")
#        Output:
#        Expected:                                 |
#        for w in [M, ss,ss, pp]
#            print(M, end=" ")
#            M
#            print(ss, end=" ")
#            M ss
#            print(ss, end=" ")
#            M ss ss
#            print(pp, end=" ")
#            M ss ss pp
#
#        M ss ss p
#
#     d) msg = ""
#        for s in "secret".split("e"):
#            msg = msg + s
#        print(msg)
#
#        Output:
#        Expected:
#        msg = ""
#        for s in [s, cr, t]:
#                = "" + s
#            msg = s + cr
#            msg = scr + t
#            msg = scrt
#       print(msg)
#       print(scrt)
#
#       scrt
#   
#     e) msg = ""
#        for ch in "secret":
#        msg = msg + chr(ord(ch)+1)
#        print(msg)
#        [I will not do step-by-step evaluation here.
#        It's clear that the fragment prints a string
#        by taking the Unicode value of each letter,
#        adding 1 to it, and then evaluating the int
#        to return the corresponding Unicode character,
#        thus altering the unicode of each character in
#        "secret" by +1, cocatenating the result in msg
#        each time the loop iterates.]
#        s = 115 + 1 = 116 = t
#        e = 101 + 1 = 102 = f
#        c = 99 + 1 = 100 = d
#        r = 114 + 1 = 115 = s
#        e = 101 + 1 = 102 = f
#        t = 116 + 1 = 117 = u
#
#        tfdsfu

#  4. Show the string that would result from each of the following string formatting operations. If the
#     operation is not legal, explain why:

#     a) "Looks like (1) and (0) for breakfast".format("eggs", "spam")
#        The operation is not legal. Curly braces are required around 1 and 0.

#     b) "There is {0} {1} {2} {3}".format(1, "spam", 4 "you")
#         'There is 1 spam 4 you.'

#     c) "Hello {0}".format("Susan", "Computewell")
#        'Hello Susan'

#     d) "{0:0.2f} {0:0.2f}".format(2.3, 2.3468)
#        '2.30 2.30'

#     e) "{7.5f} {7.5f}".format(2.3, 2.3468)
#        The operation is not legal. There is no index followed by : supplied in each of the curly braces.

#     f) "Time left {0:02}:{1:05.2f}".format(1, 37.374)
#        'Time left 1:37.37'

#     g) "{1:3}".format("14")
#        '14'

#  5. Explain why public key encryption is more useful for securing commmunications on the Internet than
#     private (shared) key encryption.
#     Private keys use the same key to both encrypt and decrypt communications before sending and after receiving.
#     This increases the probability of malicious use.
#     Public keys entail a public key to encrypt communciations before sending. However, the communications can
#     only be decrypted with another key that is specific to the recipient.


### PROGRAMMING EXERCISES

#  1. The example code files for Chapter 5 include a date conversion program, dateconvert2.py. This program could be
#     simplified with string formatting. Modify the program to use the string format method for its output.
#
# dateconvert2.py
#     Converts day month and year numbers into two date formats

def main():
    # get the day month and year as numbers
    day = int(input("Enter the day number: "))
    month = int(input("Enter the month number: "))
    year = int(input("Enter the year: "))

    date1 = str(month)+"/"+str(day)+"/"+str(year)

    months = ["January", "February", "March", "April", 
              "May", "June", "July", "August", 
              "September", "October", "November", "December"]
    monthStr = months[month-1]
    date2 = monthStr+" " + str(day) + ", " + str(year)

    print("The date is {0} or {1}.".format(date1, date2))

main()


#  2. A certain CS professor gives 5-point quizzes that are graded on the scale 5-A, 4-B, 3-C, 2-D, 1-F, 0-F. Write a
#     program that accepts a quiz score as an input and prints out the corresponding grade.
#
#     Input: quiz score defined as a a number from 1 to 5
#     Output: a letter grade defined as a string: A, B, C, D, F
#
#     Create a squence of grades as a string, where index/position corresponds to letter grade 
#     For a number supplied by user, convert to int and get the index, print the appropriate grade
#
# gradeconverter.py
#     Converts a quizscore from 1-5 to the corresponding grade

def main():
    # Create list of possible letter grades
    lettergradescale = "FFDCBA"
    # Prompt user for quiz grade
    quizgrade = int(input("Please enter the quiz grade on a scale from 0 to 5: "))
    lettergrade = lettergradescale[quizgrade]
    print("Your quiz grade of {0} corrsesponds to the letter grade of {1}.".format(quizgrade, lettergrade))

#  3. A certain CS professor gives 100-point exams that are graded on the scale 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F.
#     Write a program that accepts an exam score as input and prints out the corresponding grade.
#
#     Input: an exam score defined as an int from 0 t0 100
#     Output: a letter grade defined as one of 5 possible strings: A, B, C, D, F where 90-100:A, 80-89:B, 70-79:C, 60-69:D, <60:F
#
#     Define int ranges for each letter grade
#     For a number  grade entered by user, use if elif statements to determine letter grade
#
#     Note: Another possible solution, but much less efficient, would be to create a sequence as a string or list where each
#     list grade would be a list item indexed at its coresponding value, so in the indeces from 90 to 100, there would be an "A"
#
#     Since I don't feel like typing a lot, I will use the more efficient solution even if decision structures have not been
#     covered yet.
#
#     Then again, I will stick with the book's plan and write up the less efficient version.
#
# examgrade.py
#     Converts an exam grade to a letter grade

def main():
    lettergradescale = "FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFDDDDDDDDDDCCCCCCCCCCBBBBBBBBBBAAAAAAAAAAA"
    examgrade = int(input("Please enter the quiz grade on a scale from 0 to 100: "))
    lettergrade = lettergradescale[examgrade]
    print("Your grade of {0} corresponds to the letter grade of {1}.".format(examgrade, lettergrade))

main()
    
#  4. An acronym is a word formed by taking the first letters of the words in a phrase and making a word from them. For
#     example, RAM is an acronym for "random access memory." Write a program that allows the user to type in a phrase and
#     then outputs the acronym for that phrase. Note: The acronym should be all uppercase, even if the words in the phrase
#     are not capitalized.
#
#     Input: A string of words demarcated by spaces
#     Output: A string that is an acronym of the first letter of each word in the string
#
#     Get input from user as a string
#     Use split method to split string into its component words as demarcated by a space (" ")
#     Get first letter of each word using loop accumulator
#     Join first letter of each word into a new string
#     Capitalize new string
#     Print string for user
#
#
# acronym.py
#     A program that forms an acronym out of words

def main():
    userstring = str(input("Please enter the words, separated by a space, that will be used for the acronym: "))
    words = userstring.split()
    for i in range(len(words)):
        newacronym = []
        word = words[i]
        firstletter = word(0)
        newacronym.append(firstletter)
    print("The acronym is {0}".format(newacronym))

main()
# need to test this        
#

#  5. Numerologists claim to be able to determine a person's character traits based on the "numeric value" of a name. The value
#     of a name is determined by summing up the values of the letters of the name where "a" is 1, "b" is 2, "c" is 3, up to "z"
#     being 26. For example, the name "Zelle" would have the value 26 + 5 + 12 + 12 + 5 = 60 (which happens to be a very
#     auspicious number, by the way). Write a program that calculates the numeric value of a single name provided as input.
#
#  input: a last name defined as a string supplied by the suer
#  output: a numeric value defined as an int that is the sum of values assigned to the individual strings
#  User inputs a string, and the program outputs the sum of the values of the invidual strings where the values are
#  determined as follows, a = 1, b = 2, etc.

#  Create a sequence of characters as lookup table starting with an empty space at index 0 to align index with value of each letter
#  User supplies string as input
#  For each character in the input string, return where it occurs in the string, and add its index value to an accumulating sum
#  Print sum
#
# numerology.py
# A program that determines the numeric value of a name where a = 1, b = 2, etc.

def main():
    lookup = "0abcdefghijklmnopqrstuvwxyz"
    inputname = str(input("Please use letters only to enter your name."))
    formatinputname = inputname.lower()
    for i in range(len(name)):
        wordvalue = []
        letter = formatinputname[i]
        lettervalue = lookup.find(letter)
        wordvalue = wordvalue + lettervalue
    print("The numeric value of {0} is {1}.".format(inputname, wordvalue))

main()
#need to test

#  6. Expand your soluation to the previous problem to allow the calcualtion of a complete name such as "John Marvin Zelle" or
#     "John Jacob Jingleheimer Smith." The total value is just the sum of the numberic values of all the names.
#
#  Algorithm same as above, but need to use split method to make a list, then loop through each list element with above
#  process for determining numeric value

# numerology.py
# A program that determines the numeric value of a name where a = 1, b = 2, etc.

def main():
    lookup = "0abcdefghijklmnopqrstuvwxyz"
    inputnames = str(input("Please use letters only to enter your name."))
    joininputnames = inputnames.join()
    formatinputnames = formatinputnames.lowert()
    for i in range(len(formatinputnames)):
        totalvalue = []
        letter = formatinputname[i]
        lettervalue = lookup.find(letter)
        wordvalue = wordvalue + lettervalue
    print("The numeric value of {0} is {1}.".format(inputnames, totalvalue))

main()
#need to test


#  7. A Caesar cipher is a simple substitution sipher based on the diea of shifting each letter of the plaintext message a fixed
#     number (called the key) of positions in the alphabet. For example, if the key is 2, the word "Sourpuss" would be encoded as
#     "Uqwtrwuu." The original message can be recovered by "reencoding" it using the negative of the key.
#
#     Write a program that can enconde and decode Caesar ciphers. The input to the progrma will be a string of plaintext and the
#     value of the key. The output will be an encoded message where each character in the original message is replaced by shifting
#     it key characters in the Unicode character set. For exmaple, if ch is a character in the string and key is the amount to shift,
#     then the character that replaces ch can be calculated as: chr(ord(ch) + key).

#  8. One problem with the previous exercise is that it does not deal with the case when we "drop off the end" of the alphabet. A
#     true Caesar cipher does the shifting in a circular fashion where the next character after "z" is "a." Modify your solution
#     to the previous problem to make it circular. You may assume that the input consists only of letters and paces.
#     Hint: Make a string containing all the cahracters of your alphabet and use positions in this string as your code. You do not
#     have to shift "z" int "a"; jsut make sure that you use a circular shift over the entire sequence of characters in your alphabet
#     string.

#     Note to self: modular.

#  9. Write a program that counts the number of words in a sentence entered by the user.
#
#  Given a sentence, the program will count the number of words.
#  input = a sentence defined as a string
#  output = the number of words defined as an int
#
#  Prompt user for input.
#  Use split method to split string into list of words.
#  Print length of list.

def main():
    sentence = str(input("Please enter your sentence here: "))
    sentenceintowords = sentence.split()
    numberofwords = len(sentenceintowords)
    
    print("The number of words in", end = "/n")
    print(sentence, end = "/n")
    print("is", end = "/n")
    print(numberofwords, ".")

main()
#need to test
                
# 10. Write a program that calculates the average word length in a sentence entered by the user.
#     Same as above, but also count lenght of each words, add up all the numbers, divide by number of words.

def main():
    sentence = str(input("Please enter your sentence here: "))
    sentenceIntoWords = sentence.split()
    
    for i in (len(sentenceIntoWords)):
        wordLengthTotal = []
        wordLength = len(sentenceIntoWords(i))
        wordLengthTotal = wordLengthTotal + wordLength
    averageWordLength = wordLengthTotal / len(sentenceIntoWords)

    print("The average word length in the sentence", end = "/n")
    print(sentence, end = "/n")
    print("is", end = "/n")
    print(numberofwords, ".")
# need to test

 
# 11. Write an improved version of the chaos.py program from Chapter 1 that allows a user to input two initial values and the number of
#     of iterations, and then prints a nicely formatted table showing how the values change over time. For example, if the starting
#     values were .25 and .26 with 10 iterations, the table might look like this:

#     index    0.25         0.26
#     ----------------------------
#       1    0.731250     0.750360
#       2    0.766441     0.730547
#       3    0.698135     0.767707
#       4    0.821896     0.695499
#       5    0.570894     0.825942
#       6    0.955399     0.560671
#       7    0.166187     0.960644
#       8    0.540418     0.147447
#       9    0.968629     0.490255
#      10    0.118509     0.974630

def main():
     print("Ths program illustrates a chaotic function")
     x = float(input("Enter first numbers between 0 and 1: "))
     y = float(input("Enter second number between 0 and 1: "))
     z = "input"
     print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x,y,z))
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - y)
         print("{0:>14.6f}{1:>13.6f}".format(x, y))
     
main()

# 12. Write an improved version of the futval.py program from Chapter 2.
#     Your program will prompt the user for the amoutn of the investment, the annualized interest rate, and the number of years of the
#     investment. The program will then output a nicely formatted table that tracks the value of the investment year by year. Your
#     output might look something like this:
#
#     Year     Value
#     ----------------
#       0     $2000.00
#       1     $2200.00
#       2     $2420.00
#       3     $2662.00
#       4     $2928.20
#       5     $3221.02
#       6     $3542.12
#       7     $3897.43

# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: ", end="/n"))

    print("{0:<9}{1:<7}".format(Year, Value) #not right
    
    for i in range(10):
        principal = principal * (1 + apr)
        print("{0:>6}{$1:>8.2f}".format(i, principal)) #not right

    print("The value in 10 years is:", principal)

main()

# 13. Redo any of the previous programming exercises to make them batch-oriented (using text files for input and output).

# 14. Word Count. A common utility on Unix/Linux systems is a small program called "wc." This program analyzes a file to determine the
#     number of lines, words and characters contained therein. Write your own verison of wc. The program should accept a file name as
#     input and then print three numbers showing the count of lines, words, and characters in the file.

# 15. Write a program to plot a horizontal bar chart of student exam scores. Your program should get input from a file. The first line
#     of the file contains the count of the number of students in the file, and each subsequent line contains a student's last name
#     followed by a score in the range 0-100. Your program should draw a horizontal rectangle for each student where the length of the
#     bar represents the student's score. The bars should all line up on their left-hand edges.
#
#     Hint: Use the number of students to determine the size of the window and its coordinates. [Note to self: point of control.]
#     Bonus: label the bars at the left with the students' names.

# 16. Write a program to draw a quiz score histogram. Your program should read data from a file. Each line of the file contains a number
#     in the range 0-10. Your program must count the number of occurences of each score and then draw a vertical bar chart with a bar for
#     each possible score (0-10) with height corresponding to the count of that score. For example, if 15 students got an 8, then the
#     the height of the bar for 8 should be 15.
#     Hint: Use a list that stores the count for each possible score.

#     1. Problem analysis:
#        How to count number of occurences of possible test scores and represent the count on a vertical chart.
#
#     2. Specification:
#        Inputs: file with test scores
#        Output: histogram representing occurences of each score
#
#     3. Design (algorithm)
#        import graphics library
#        import dialog box for opening file
#        get the file name
#        open the file
#        read file
#        create empty list for scores
#        process each line of the input file
#        get each score
#        append each score to empty list in output file
#        count the number of occurences of each score
#        store each count in a new list
#        create graphical template for histogram using a loop
#        define one rectangle (bar) and use variable for height
#        define space between bars as equal to width of one bar
#        label each bar from 0 to 10 using loop count
#        use
#
#     4. Implement

# histogram.py
# Program to count the number of all possible grades from 0 to 10 and output a histogram

# import graphics library
from graphics import *

# import dialog box for opening file
from tkinter.filedialog import askopenfilename

def main():
    print("This program creates a histogram from a file of grades.")
    print("Please select the file containing the grades.")

    # get the file name
    infileName = askopenfilename()

    # create empty list to store scores
    scores = []
    # open and read file
    infile = open(infileName, "r")
    # process each line of the input file
    for line in infile:
        # get the score from line by converting it to int and appending to scores list
        scores.append(int(line[:-1])) #THIS LINE IS GIVING ME TROUBLE
    # close file
    infile.close()
   
    # create empty list to store score counts
    scorecounts = []
    # count the number of occurences of each score and store in a new list
    for score in range(11):
        scorecount = [scores].count(score)
        scorecounts.append(scorecount)
    
    # creates graphics window
    histogram = GraphWin("Histogram", 400, 200)
    histogram.setBackground("yellow")
    # sets coordinates to simplify drawing of images
    # note that yur is determined by number of scores + 10
    histogram.setCoords(0, 0, 115, (len(scores) + 10))

    # use loop to create graphical template for histogram
    for i in range(11):
        bar = Rectangle(Point((5 + (10 * i)), 5), Point((10 + (10 * i)), (scorecounts[i] + 5)))
        bar.setFill("red")
        bar.setWidth(3)
        bar.setOutline("blue")
        bar.draw(histogram)
        label = Text(Point((7 + (10 * i)), 2), str(i))
        label.draw(histogram)

    print("Histogram has been created.")
    print("Click anywhere on yellow window to close.")
    histogram.getMouse()
    histogram.close()


main()

#ERROR: FOR SOME REASONS I AM GETTING EMPTY SCORECOUNTS LIST


#     5. Test/Debug
#        create file with 50 different test scores
#        above version did not work
#        version below works

# histogram.py
# Program to count the number of all possible grades from 0 to 10 and output a histogram
# this version works

# import graphics library
from graphics import *

# import dialog box for opening file
from tkinter.filedialog import askopenfilename

def main():
    print("This program creates a histogram from a file of grades.")
    print("Please select the file containing the grades.")
    print()

    # get the file name
    infileName = askopenfilename()

    # create empty list to store scores
    scores = []
    # open and read file
    infile = open(infileName, "r")
    # process each line of the input file
    for line in infile:
        # get the score from line by removing newline character
        score = line[:-1]
        # store score by appending to scores list
        scores.append(score)
    # close file
    infile.close()

    # verify list of scores
    print("Verifying scores")
    verifyscores = " ".join(scores)
    print(verifyscores, end='\n')
    print()
   
    # create empty list to store score counts
    scorecounts = []
    # count the number of occurences of each score and store in a new list
    for i in range(11):
        scorecheck = str(i)
        scorecount = verifyscores.count(scorecheck)
        scorecounts.append(scorecount)
    # Question: Why does count() method not work when looping through the list of items
    # after they are converted from str to int? The scorecounts list ends up empty.

    # verify list of score counts
    print("Verifying score counts")
    strscorecounts = []
    for intscorecount in scorecounts:
        strscorecount = str(intscorecount)
        strscorecounts.append(strscorecount)
    verifyscorecounts = " ".join(strscorecounts)
    print("counts", verifyscorecounts, end='\n')
    print("scores", "0 1 2 3 4 5 6 7 8 9 10", end='\n')
    print()
    
    # creates graphics window
    histogram = GraphWin("Histogram", 400, 200)
    histogram.setBackground("yellow")
    # sets coordinates to simplify drawing of images
    # note that yur is determined by number of scores + 10
    histogram.setCoords(0, 0, 115, (len(scores) + 10))

    # use loop to create graphical template for histogram
    for j in range(11):
        bar = Rectangle(Point((5 + (10 * j)), 5), Point((10 + (10 * j)), (scorecounts[j] + 5)))
        bar.setFill("red")
        bar.setWidth(3)
        bar.setOutline("blue")
        bar.draw(histogram)
        label = Text(Point((7 + (10 * j)), 2), str(j))
        label.draw(histogram)

    print("Histogram has been created.")
    print("Click anywhere on yellow window to close.")
    histogram.getMouse()
    histogram.close()


main()

#   Note that when a text file created with native mac iOS text editor is used
#   Scores are verified erroneously:
##Verifying scores
##{\rtf1\ansi\ansicpg1252\cocoartf1404\cocoasubrtf470 {\fonttbl\f0\fswiss\fcharset0 Helvetica;} {\colortbl;\red255\green255\blue255;} \margl1440\margr1440\vieww10800\viewh8400\viewkind0 \pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0  \f0\fs24 \cf0 1\ 1\ 1\ 1\ 1\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 10\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5\ 5
##
##Verifying score counts
##counts 45 28 12 2 15 19 5 5 6 1 16
##scores 0 1 2 3 4 5 6 7 8 9 10

#   This program only works for text files created with IDLE.


                    
#     6. Maintain





