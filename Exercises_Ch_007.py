# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 7: Decision Structures
# End-of-Chapter Exercises
#
# REVIEW QUESTIONS
#
# True/False3
#
#  1. T
#  2. F
#  3. T
#  4. T
#  5. T
#  6. F
#  7. F
#  8. F
#  9. T
# 10. F
#
# Multiple Choice
#
#  1. C
#  2. C
#  3. B
#  4. B
#  5. C
#  6. C
#  7. A
#  8. C
#  9. A
# 10. C
#
# Discussion
#
# 1.  The sequences of statements ins a simple decision excecutes when
#     the condition true. If it is false, cthe statements are skipped.
#     A two-way decision is a simple decision with two parts. If the
#     condition is true, the statements are executed. If it is false,
#     a different set of statements is excecuted.
#     Multi-way decisions specifiy different conditions, which, if true,
#     lead to different sets of statements being executd.
# 2.  Exception-handling is conditional, similar to if statements. If an
#     error occurs in the body of the try statement, Python looks for an
#     except clause with a matching error and excecute the handler
#     code if an appropriate except is found.
# 3. a. Trees
#       Larch
#       Done
#    b. Trees
#       Chestnut
#       Done
#    c. Spam Please!
#       Cheese Shoppe
#       Cheddar
#       Gouda
#       Done
#    d. Cheese Shoppe
#       Cheddar
#       Done
#    e. It's a late parrot!
#       Trees
#       Larch
#       Done
#    f. Cheese Shoppe
#       Cheddar
#       Done
#
# PROGRAMMING EXERCISES

# c07ex1.py
#    overtime pay


def main():
    print("Weekly pay calculator \n")
    hours = float(input("Enter hours worked: "))
    rate = float(input("hourly wage: "))
    if hours <= 40:
        pay = hours * wage
    else:
        pay = 40 * wage + (hours-40) * 1.5 * wage

    print("Your week's pay is ${0:0.2f}.".format(pay))

if __name__ == '__main__':
    main()
       
# c07ex2.py
#    quiz grade


def main():
    print("Quiz grade calculator \n")
    score = int(input("Enter quiz score: "))
    if score == 5:
        grade = "A"
    elif score == 4:
        grade = "B"
    elif score == 3
        grade = "C"
    elif score == 2
        grade = "D"
    else:
        grade = "F"

    print("The grade is ", grade".")

if __name__ == '__main__':
    main()

# c07ex3.py
#  exam grade


def main():
    print("Exam grade calculator \n")
    score = int(input("Enter exam score: "))
    if score >= 90:
        grade = A
    elif score >= 80:
        grade = B
    elif score >= 70:
        grade = C
    elif score >= 60:
        grade = D
    else:
        grade = F
        
    print("The grade is ", grade".")

if __name__ == '__main__':
    main()

# c07ex4.py
#    class standing

def main():
    print("Class standing calculator\n")
    credits = int(input("Enter number of credits: "))
    if credits >= 26:
        standing = "senior"
    elif credits >= 16:
        standing = "junior"
    elif credits >= 7:
        standing = "sophomore"
    else:
        standing = "freshman"

    print("The class standing is", standing".")

if __name__ == '__main__':
    main()

# c07ex5.py
#    body mass index

def main():
    print("BMI calculator \n")
    weight = float(input("Enter weight: "))
    height = float(input("Enter height: "))
    bmi = weight * 720 / height
    print = ("Your BMI is ", bmi".")
    if bmi < 19:
        print("You are below the healthy range.")
    elif bmi <= 25:
        print("You are in the healthy range.")
    else:
        print("You are above the healthy range.")

if __name__ == '__main__':
    main()

# c07ex6.py
#    speeding fine

def main():
    print("Speeding fine calculator \n")
    speedlimit = int(input("Enter speed limit: "))
    clockedspeed = int(input("Enter clocked speed: "))
    if clockedspeed <= speedlimit:
        print("The speed is legal.")
    else:
        print("The speed is illegal.")
        if clockedspeed > 90:
            fine = 5 * (clockedspeed - speedlimit) + 50 + 200
        else
            fine = 5 * (clockedspeed - speedlimit) + 50
        print("The fine is ${0:02f}."format(fine))

if __name__ == '__main__':
    main()

# c07ex7.py
#    babysitting bill

def main():
    print("Babysitting bill calculator \n")
    



    


