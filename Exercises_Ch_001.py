# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 1: Computers and Programs
# End-of-Chapter Exercises
#
# REVIEW QUESTIONS
#
# True/False
#
#  1. F
#  2. T
#  3. F
#  4. T
#  5. F
#  6. T
#  7. F
#  8. T
#  9. F
# 10. F: "it can be computed, but the result may not be useful"
#
# Multiple Choice
#
#  1. B
#  2. D
#  3. D
#  4. A
#  5. B
#  6. B
#  7. C
#  8. B
#  9. A
# 10. D
#
# Discussion
#
#  1. Compare and contrast.
#     a) Hardware is the body, software is the soul.
#     b) An algorithm is a recipe to solve a problem. A program is an
#        implementation of an algorothm/s.
#     c) Programming languages are precise and are used for computers.
#        Natural languages are used for humans and can be ambiguous.
#     d) A high-level language is meant to be understood by humans. A
#        machine language is understood by the computer.
#     e) An interpreter translates code into machine language line-by-line.
#        A compiler does so in one shot.
#     f) Syntax is form. Symantics is meaning.
#
#  2. The central processing unit or CPU is the brain of the computer.
#     It performs all the basic operations. Main memory stores programs
#     and data, but this memory is not permanent. The information is
#     lost when the computer is turned off. Secondary memory provides
#     more permanent storage. Humans interact with computers via input
#     and output devices. Input devices allow the computer to receive
#     information about the world. After it is processed by the
#     computer, output devices take the new information and return it to
#     the world for humans to absorb.
#
#  3. Buy the peanut butter, jelly and bread at the store. Bring the
#     items home.
#
#     Before putting the peanut butter jar in the fridge, open the
#     peanut butter by twisting the cap in a counter-clockwise
#     direction. Stir the peanut butter with a spoon. Make sure not to
#     spill any oil or peanut butter outside of the jar. Stir until
#     the contents of the jar are of a uniform consistency. Put the
#     peanut butter jar, the jelly jar, and the bread in the fridge.
#
#     Open the fridge door. Take out the peanut butter jar by grasping
#     it with your hand. Put the jar you are holding in your and gently
#     on a flat surface such as a table. Repeat this process for the
#     jelly jar and the bread. Close the fridge door.
#
#     Open the cupboard, and get a plate by grabbing it with your hand.
#     Remove the plate from the cupboard and close the cuboard door. Put
#     the plate on the table gently. Open the drawer where the utensils
#     are. Pick up a knife with your hand. Close the drawer. Put the
#     knife on the table.
#
#     It is time to open jars. Grip the peanut butter jar, holding it
#     firmly in your left hand if you are right-handed. Twist the jar
#     cap with your right hand in a counter-clockwise direction until
#     the jar cap is completely separated from the jar.
#
#     If the jar cap does not open, go to the kitchen sink with the jar.
#     Turn the knob for the hot water. Wait until the water is hot.
#     Place the jar jar cap under the running hot water. Let hot water
#     run over the jar cap for 5 minutes. Twist the jar cap with your
#     right hand in a counter-clockwise direction until the jar cap is
#     completely seapareted from the jar. Repeat the process you used
#     for the peanut butter jar also for the jelly jar.
#
#     The bread that you put on the table is most likely enclosed in a
#     plastic bag. Pick up the bread and open the plastic bag. Take out
#     2 slices of bread that are not the end slices. Put the slices on
#     on the plate, side-by-side. Close the plastic bag. Put the plastic
#     bag containing the bread back where you found it in the fridge.
#
#     Pick up the knife and hold it by the non-cutting end. While
#     holding the knife, dip its cutting end into the open jar of peanut
#     butter. Use the knife to scoop out some jar contents so that some
#     of the peanut butter is on the cutting end of the knife. Hold the
#     knife so that the jar contents is facing up and bring the knife to
#     about an inch away from one of the two slices of bread that you
#     prepared. Now rotate the knife so that the side with the jar
#     jar contents on it is now facing down instead of facing up. Touch
#     the face down side of the knife to the center of the bread and
#     gently spread across the whole slice so that the layer is even.
#     Repeat this until you have the desired consistency of peanut
#     butter on the slice of bread. Close the jar of peanut butter. By
#     taking its cap, putting it on top of the jar, and twisting the cap
#     in a clockwise direciton. Put the jar back in the fridge where you
#     found it.
#
#     Repeat the entire process in the previous paragraph for the jar of
#     jelly, transferring the jelly to the slice that now has peanut
#     butter on it. You will spread the jelly on top of the peanut
#     butter. When you are done with the jelly, close the jar in the
#     same way that you closed the jar of peanut butter. Put the jar
#     back in the fridge where you found it.
#     
#     Take the slice that has nothing on it and put it on top of the
#     slice with the peanut butter and jelly gently, do not squeeze the
#     slices together too hard. Make sure that all the corners on both
#     slices are lined up. The edges of the slices should be flush. The
#     slices themselves now be parallel to each other and have peanut
#     butter and jelly between them.
#
#     Make sure to clean up after yourself.
#
#     Note that the problem is not well-specified because there is no
#     set vocabulary for defining the steps of the algorithm. In other
#     words, natural language is inefficient for describing processes
#     reliably, and even moreso for computational processses.
#
#
#  4. In any circumstance where the result of a computation must be
#     100% accurate in order to be usable, it is unwise to use the float
#     data type. Examples of such situations:
#     - calculating a measurement, esp. on a large or small scale
#     - calculating financial values, esp. over time (e.g., interest
#       accrued)
#     Since rounding errors always occur, the result will be inaccurate.
#     Rounding errors compound and will increase the inaccuracy if the
#     calculations are repeated in some way as in the chaotic function.
#
# 5.
# chaos.py
# This program illustrates a chaotic function
def main():
         print("This program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range(10):
             x = 3.9 * x * (1 - x)
             print(x)

# x = .15
#                                                      
# for 0 in range(10):                                                  
#     x = 3.9 * .15 * (1 - .15)                        
#     print(0.49725)                                   
#                                                       
# for 1 in range(10):                                  
#     x = 3.9 * 0.49725 * (1 - 0.49725)                 
#     print(0.97497050625)                             
#                                                       
# for 2 in range(10):                                  
#     x = 3.9 * 0.97497050625 * (1 - 0.97497050625)    
#     print(0.09517177095122)
#     
# for 3 in range(10):                    
#     x = 3.9 * 0.09517177095122 * (1 - 0.09517177095122)
#     print(0.3358450093644)
# 
# for 4 in range(10):                    
#     x = 3.9 * 0.3358450093644 * (1 - 0.3358450093644)
#     print(0.86990724229278)
# 
# for 5 in range(10):                    
#     x = 3.9 * 0.86990724229278 * (1 - 0.86990724229278)
#     print(0.44135766518747)
# 
# for 6 in range(10):                    
#     x = 3.9 * 0.44135766518747 * (1 - 0.44135766518747)
#     print(0.96158819861419)
# 
# for 7 in range(10):                    
#     x = 3.9 * 0.96158819861419 * (1 - 0.96158819861419)
#     print(0.14405170611043)
# 
# for 8 in range(10):                    
#     x = 3.9 * .0.14405170611043 * (1 - .0.14405170611043)
#     print(0.48087316710069)
# 
# for 9 in range(10):                    
#     x = 3.9 * 0.48087316710069 * (1 - 0.48087316710069)
#     print(0.97357324062664)
#
#
# Trace output sequence       Output sequence when program is run:
# 0.49725                     0.49724999999999997 
# 0.97497050625               0.97497050625
# 0.09517177095122            0.09517177095121285
# 0.3358450093644             0.3358450093643686
# 0.86990724229278            0.8699072422927216
# 0.44135766518747            0.4413576651876355
# 0.96158819861419            0.9615881986142427
# 0.14405170611043            0.14405170611022783
# 0.48087316710069            0.48087316710014555
# 0.97357324062664            0.9735732406265619
#
# Note: Answer key has this:
# 0.49725 
# 0.97497050625 
# 0.0951717709512 
# 0.335845009364 
# 0.869907242293 
# 0.441357665188 
# 0.961588198614 
# 0.14405170611 
# 0.4808731671 
# 0.973573240627

# What explains the differences?

# I used a calculator app for the trace. The calculator produced
# accurate values, the program produced approximations as result of how
# these values are stored (i.e., stored as float data type).

# But, why is the answer key different?

# PROGRAMMING EXERCISES

# 1. a) Hello, world!
#    b) Hello world!
#    c) 3
#    d) 3 0
#    e) 5
#    f) 5.0
#    g) 23
#    h) 2 + 3 = 5
#    i) 6
#    j) 8
#    k) 2.3333333333333335
#    l) 2
#
# 2. 
#    INPUT:  .1          INPUT: .2           INPUT: .3
#    OUTPUT:             OUTPUT:             OUTPUT:             
#    0.35100000000000003 0.6240000000000001  0.819                
#    0.8884161           0.9150335999999998  0.5781321000000001  
#    0.3866184397170808  0.30321373239705673 0.951191962303401   
#    0.9248640249724619  0.8239731430433209  0.18106067129594494 
#    0.2710131851083772  0.5656614700878645  0.5782830479626462  
#    0.7705036505625796  0.9581854282490118  0.9510998811665442  
#    0.6896283226260395  0.1562578420270518  0.18138469912496583 
#    0.8347602871063352  0.5141811824451928  0.5790887311884146  
#    0.5379486456882877  0.9742156868513789  0.950605393136126   
#    0.9693836111326567  0.09796598114189214 0.1831236407388855  
#
#   INPUT: .9243        INPUT: .00001         INPUT: .000011
#   OUTPUT:             OUPUT:                OUTPUT:
#   0.27288108899999997 3.899961e-05          4.28995281e-05
#   0.7738263010380788  0.0001520925472186374 0.0001673009821489063
#   0.6825747117532334  0.0005930707187953    0.0006523646708680855
#   0.8449992510500727  0.00231160404507945   0.0025425624556967255
#   0.5108045154220668  0.008994416074091065  0.009890781544236867
#   0.9745447235413278  0.034762714558951066  0.0381925205402561
#   0.09674849090043053 0.13086164611823145   0.14326202246864903
#   0.34081405959478733 0.443573815204487     0.4786782600086812
#   0.8761733618715016  0.9625827341107481    0.9732269952745961
#   0.42312504709133986 0.1404671350002371    0.10161922267917184
#
# 3. 
#    INPUT:  .1          INPUT: .2           INPUT: .3           
#    OUTPUT:             OUTPUT:             OUTPUT:             
#    0.18000000000000002 0.32000000000000006 0.42                
#    0.2952              0.43520000000000003 0.4872              
#    0.41611392          0.49160192          0.49967231999999995 
#    0.4859262511644672  0.4998589445046272  0.4999997852516352  
#    0.49960385918742867 0.49999996020669446 0.4999999999999078  
#    0.49999968614491325 0.49999999999999684 0.49999999999999994 
#    0.49999999999980305 0.49999999999999994 0.49999999999999994 
#    0.5                 0.49999999999999994 0.49999999999999994 
#    0.5                 0.49999999999999994 0.49999999999999994 
#    0.5                 0.49999999999999994 0.49999999999999994 
#
#    INPUT: .9243        INPUT: .00001          INPUT: .000011
#    OUTPUT:             OUPUT:                 OUTPUT:
#    0.13993901999999997 1.99998e-05            2.1999758e-05
#    0.24071218136287917 3.9998800015999924e-05 4.3998548021295886e-05
#    0.36553965421280704 7.99944002239944ee-05  8.79932242981358e-05
#    0.46384083082157695 0.00015997600223985442 0.00017597096298122686
#    0.4973850289686524  0.00031990081983712356 0.0003518799944028286
#    0.4999863238530105  0.0006395969666051822  0.0007035123497447354
#    0.49999999962592606 0.0012783757646509832  0.0014060348402369842
#    0.49999999999999994 0.0025534830401106722  0.002808115812530048
#    0.49999999999999994 0.005093925528949078   0.005600460596226933
#    0.49999999999999994 0.010135954903309199   0.011138190874674084
#
#    When the multiplier is 2, the logistic function appears to behave
#    in a "less random" fashion. What is it about 3.9?

# c1ex04.py 
# Chaos program amended to produce output sequence of 20 terms
def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(20):
        x = 3.9 * x * (1 - x)
        print(x)

# c01ex5.py
# Chaos program that prints a variable number of terms

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
        
main()

# c01ex6.py
# Chaos program with 3 algebraically equivalent expressions

def main ():
    print("This program is an experiment.")
    x = eval(input("Enter a number between 0 and 1: "))
    a = x
    b = x
    c = x
    for i in range(100):
        a = 3.9 * a * (1 - a)
        b = 3.9 * b * (b - b * b)
        c = 3.9 * c - 3.9 * c * c
        print("{0:<30.20}{1:<30.20}{2:<30.20}".format(a, b, c))

main()

# Output comparison for .23 shows that algebraically equivalent
# expressions do not return the same outputs when the input values are a
# floating-point data type. This is because of rounding errors implicit
# in floats.

# c01ex7.py
# Chaos program to print values in chart form side-by-side
# This is ugly and not secure

def main():
     print("Ths program illustrates a chaotic function")
     x, y = eval(input(
             "Enter 2 numbers between 0 and 1 separated by a comma: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print(x, "   ", y)
     
main()

# c01ex7v1.py
# More secure version with bad formatting

def main():
    print("Ths program illustrates a chaotic function")
    x = float(input("Enter first number between 0 and 1: "))
    y = float(input("Enter second number between 0 and 1: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print(x, "   ", y)
     
main()

# c01ex7v1.py
# More secure version with good formatting

def main():
     print("Ths program illustrates a chaotic function")
     x = float(input("Enter first number between 0 and 1: "))
     y = float(input("Enter second number between 0 and 1: "))
     z = "input"
     print("{2:<8}{0:<13.2f}{1:<6.2f}".format(x,y,z))
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print("{0:>14.6f}{1:>13.6f}".format(x, y))
     
main()




