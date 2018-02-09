# "Python Programming: An Introduction to Computer Science"
# by John Zelle, 3rd Ed.
# Chapter 1: Computers and Programs
# End-of-Chapter Exercises
#
# REVIEW QUESTIONS
#
# True/False
#
#  1. F [CORRECT]
#  2. T [CORRECT]
#  3. F [CORRECT]
#  4. T [CORRECT]
#  5. F [CORRECT]
#  6. T [CORRECT]
#  7. F [CORRECT]
#  8. T [CORRECT]
#  9. F [CORRECT]
# 10. T [INCORRECT]
#        ANS: F: "it can be computed, but the result may not be useful"
#
# Multiple Choice
#
#  1. B [CORRECT]
#  2. D [CORRECT]
#  3. D [CORRECT]
#  4. A [CORRECT]
#  5. B [CORRECT]
#  6. B [CORRECT]
#  7. C [CORRECT]
#  8. B [CORRECT]
#  9. A [CORRECT]
# 10. D [CORRECT]
#
# Discussion
#
#  1. Compare and contrast.
#     a) Hardware is the body, software is the soul.
#        [CORRECT: "Hardware is the physical components while software
#        is the programs."]
#     b) An algorithm is a recipe to solve a problem. A program is an
#        implementation of an algoirithm.
#        [CORRECT: "Both may be thought of as a sequence of steps to
#        solve a problem. A program is a specific implmentation of
#        some algorithm that can be executed by a computer."]
#     c) Programming languages are precise and are used for computers.
#        Natural languages are used for humans and can be ambiguous.
#        [CORRECT: "Programming languages used to write instructions for
#        computers are precise. Natural languages used for human
#        communication are ambiguous."
#     d) A high-level language is meant to be understood by humans. A
#        machine language is understood by the computer.
#        [CORRECT: "High-level languages are intended to be easier for
#        humans and must be translated into the machine language that
#        hardware of a particular computer understands."]
#     e) An interpreter translates code into machine language line-by-line.
#        A compiler does so in one shot.
#        [SEMI-CORRECT: "A compiler provides a one-shot translation,
#        while an interpreter simulates a machine that understands a
#        high-levellanguage."
#     f) Syntax vs. Symantics
#        Syntax is form. Symantics is meaning.
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
#     [CORRECT: "See discussion of Figure 1.1, pp.5-6."
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
#     
#   # Prepare bread
#   preparebread(bread)
#       pick up plastic bag on table
#       open plastic bag containing bread
#       take out 2 slices of bread that are not the end slices
#       put the 2 slices on the plate, side by side
#       close the plasic bag
#       put the plastic bag containing the bread back in the fridge
#
#   pick up knife and hold knife on the non-cutting end

#   # Define spread function
#   spread(jar, jar contents)      
#       while holding knife dip the cutting end into the jar
#       using knife scoop out some jar contents
#       hold knife so that side that has scooped jar contents is facing up
#       bring the knife an inch away from the ceneter of the bread
#       rotate knife so that the jar contents side is now facing down
#       touch the jar contents side of the knife to the slice of bread at its center
#       push the jar contents gently around on the bread until it is evenly spread across the whole slice
#       repeat these steps until you have the desired consitency on your bread
#   
#   # Apply spread function
#   spread(peanut butter jar, peanut butter)
#   spread(jelly jar, jelly)
#
#   # Close the sandwich
#   take second slice of bread in your hand
#   place it in top of the slice with the peanut butter and jelly so that the corners of both slices align
#   press gently on the top slice
#
#   # Clean up jars
#   cleanup(jar)
#       take jar cap for jar in your hand
#       put it on top of jar
#       while holding the jar cap on top of the jar twist it clockwise until it is tight and you can no longer twist
#       open the fridge
#       return the jar to its original place in the fridge
#       close the fridge
#
#   cleanup(peanut butter)
#   cleanup(jelly)
#
#   # Clean knife
#   clean(knife)
#       pick up knife by its handle
#       get a piece of paper towel
#       wipe off any jelly or peanut butter using the paper towel
#       throw out paper towel
#       put knife in dishwasher
#
#     [CORRECT: "Students will have varying degrees of success with this problem.
#     Strictly speaking it is not really well specified, as we don't have an agreed upon
#     vocabulary for expressing the steps of an algorithm. This question can be used to
#     illustrate some of the difficulties of using natural language to describe processes
#     in detail."]


#  4. As you will learn in a later chapter, many of the numbers stored in a computer are not exact values, but rather close
#     approximations. For example, the value 0.1 might be stored as 0.10000000000000000555. Usually, such small differences are not
#     a problem; however, given what you have learned about chaotic behavior in Chapter 1, you should realize the need for caution in
#     certain situations. Can you think of exmaples where this might be a problem? Explain.
#
#     [CORRECT: "If a float is used to represent a quantity in a chaotic function,
#     then a very small rounding error can lead to results that are ultimately quite
#     inaccurate and therefore not useful."]
#
#     Any situation where you are using large numbers, small differences matter greatly:
#
#     (1) For example, a savings account with millions of dollars will accrue much more
#         interest if values are stored as close approximations.
#
#     (2) Another example would be in scientifc computing, say when measuring extremely
#         small quantities, say on the atomic/subatomic level.
#
#     (3) Another example would be measuring on a large scale, say the distance between planets or solar systems. An approximation of
#         the actual measurement could impact the accuracy of any calculation.


#  5. Trace through the chaos program from Section 1.6 by hand using 0.15 as the input value. Show the sequence of output that results.
##
def main():
         print("This program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range(10):
             x = 3.9 * x * (1 - x)
             print(x)
##
##main()
##
##x = .15
##                                                      # output sequence
##for 0 in range(10):                                   # 0.49725                 
##    x = 3.9 * .15 * (1 - .15)                         # 0.97497050625
##    print(0.49725)                                    # 0.09517177095122
##                                                      # 0.3358450093644
##for 1 in range(10):                                   # 0.86990724229278
##    x = 3.9 * 0.49725 * (1 - 0.49725)                 # 0.44135766518747
##    print(0.97497050625)                              # 0.96158819861419
##                                                      # 0.14405170611043
##for 2 in range(10):                                   # 0.48087316710069
##    x = 3.9 * 0.97497050625 * (1 - 0.97497050625)     # 0.97357324062664
##    print(0.09517177095122)
##    
##for 3 in range(10):                    
##    x = 3.9 * 0.09517177095122 * (1 - 0.09517177095122)
##    print(0.3358450093644)
##
##for 4 in range(10):                    
##    x = 3.9 * 0.3358450093644 * (1 - 0.3358450093644)
##    print(0.86990724229278)
##
##for 5 in range(10):                    
##    x = 3.9 * 0.86990724229278 * (1 - 0.86990724229278)
##    print(0.44135766518747)
##
##for 6 in range(10):                    
##    x = 3.9 * 0.44135766518747 * (1 - 0.44135766518747)
##    print(0.96158819861419)
##
##for 7 in range(10):                    
##    x = 3.9 * 0.96158819861419 * (1 - 0.96158819861419)
##    print(0.14405170611043)
##
##for 8 in range(10):                    
##    x = 3.9 * .0.14405170611043 * (1 - .0.14405170611043)
##    print(0.48087316710069)
##
##for 9 in range(10):                    
##    x = 3.9 * 0.48087316710069 * (1 - 0.48087316710069)
##    print(0.97357324062664)

# Here is the output sequence as a result of the trace
# next to the output sequence as a result of the program.

# Trace output sequence       Program output sequence
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

# [Note: Answer key has this:
# 0.49725 
# 0.97497050625 
# 0.0951717709512 
# 0.335845009364 
# 0.869907242293 
# 0.441357665188 
# 0.961588198614 
# 0.14405170611 
# 0.4808731671 
# 0.973573240627]

# What explains the differences?

# I used a calculator app for the trace. The calculator produced accurate values, the program produced approximations as result
# of how these values are stored (i.e., stored as float data type).

### PROGRAMMING EXERCISES

# 1. Start up an interactive Python session and try typing in each of the following commands. Write down the results you see there.
#                                  Expected        | Actual
#    a) print("Hello, world!")     'Hello, world!' | Hello, world! [See p.33 for explanation.]
#    b) print("Hello", "world!")   'Hello' 'world!'| Hello world!  [See p.33 for explanation.]   
#    c) print(3)                   3               | 3
#    d) print(3,0)                 '3,0'           | 3 0 [Explanation: Without "", , is separator.]
#    e) print(2 + 3)               5               | 5
#    f) print(2.0 + 3.0)           5.0             | 5.0
#    g) print("2" + "3")           23              | 23
#    h) print("2 + 3 =", 2 + 3)    2 + 3 = 5       | 2 + 3 = 5
#    i) print(2 * 3)               6               | 6
#    j) print(2 ** 3)              8               | 8
#    k) print(7 / 3)               2.3333333333335 | 2.3333333333333335 [Question: What determines length of mantissa?]
#    l) print(7 // 3)              2               | 2

# 2. Enter and run the chaos program from Section 1.6. Try it out with various values of input to see that it functions as described
#    in the chapter.
#
#    INPUT:  .1          INPUT: .2           INPUT: .3           INPUT: .9243        INPUT: .00001         INPUT: .000011
#    OUTPUT:             OUTPUT:             OUTPUT:             OUTPUT:             OUPUT:                OUTPUT:
#    0.35100000000000003 0.6240000000000001  0.819               0.27288108899999997 3.899961e-05          4.28995281e-05 
#    0.8884161           0.9150335999999998  0.5781321000000001  0.7738263010380788  0.0001520925472186374 0.0001673009821489063
#    0.3866184397170808  0.30321373239705673 0.951191962303401   0.6825747117532334  0.0005930707187953    0.0006523646708680855
#    0.9248640249724619  0.8239731430433209  0.18106067129594494 0.8449992510500727  0.00231160404507945   0.0025425624556967255
#    0.2710131851083772  0.5656614700878645  0.5782830479626462  0.5108045154220668  0.008994416074091065  0.009890781544236867
#    0.7705036505625796  0.9581854282490118  0.9510998811665442  0.9745447235413278  0.034762714558951066  0.0381925205402561
#    0.6896283226260395  0.1562578420270518  0.18138469912496583 0.09674849090043053 0.13086164611823145   0.14326202246864903
#    0.8347602871063352  0.5141811824451928  0.5790887311884146  0.34081405959478733 0.443573815204487     0.4786782600086812
#    0.5379486456882877  0.9742156868513789  0.950605393136126   0.8761733618715016  0.9625827341107481    0.9732269952745961
#    0.9693836111326567  0.09796598114189214 0.1831236407388855  0.42312504709133986 0.1404671350002371    0.10161922267917184

# 3. Modify the chaos program using 2.0 in place of 3.9 as the multiplier in the logistic function. Your modified line of code should
#    look like this:
#
#    x = 2.0 * x * (1 - x)
#    Run the program for various input values and compare the results to those obtained from the original program. Write a short paragraph
#    describing any differences that you notices in the behavior of the two versions.
#
#
#    INPUT:  .1          INPUT: .2           INPUT: .3           INPUT: .9243        INPUT: .00001          INPUT: .000011
#    OUTPUT:             OUTPUT:             OUTPUT:             OUTPUT:             OUPUT:                 OUTPUT:
#    0.18000000000000002 0.32000000000000006 0.42                0.13993901999999997 1.99998e-05            2.1999758e-05
#    0.2952              0.43520000000000003 0.4872              0.24071218136287917 3.9998800015999924e-05 4.3998548021295886e-05
#    0.41611392          0.49160192          0.49967231999999995 0.36553965421280704 7.99944002239944ee-05  8.79932242981358e-05
#    0.4859262511644672  0.4998589445046272  0.4999997852516352  0.46384083082157695 0.00015997600223985442 0.00017597096298122686
#    0.49960385918742867 0.49999996020669446 0.4999999999999078  0.4973850289686524  0.00031990081983712356 0.0003518799944028286
#    0.49999968614491325 0.49999999999999684 0.49999999999999994 0.4999863238530105  0.0006395969666051822  0.0007035123497447354
#    0.49999999999980305 0.49999999999999994 0.49999999999999994 0.49999999962592606 0.0012783757646509832  0.0014060348402369842
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.0025534830401106722  0.002808115812530048
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.005093925528949078   0.005600460596226933
#    0.5                 0.49999999999999994 0.49999999999999994 0.49999999999999994 0.010135954903309199   0.011138190874674084

#    Observation: In general, when the multiplier is 2, the logistic function appears to behave in a "less random" fashion insofar as it
#    returns values that have less variance. In fact, even when the input values are close together, the output values are very similar.
#    So, it is less "choatic" in its output both for one given input as well as across differnt inputs, especially if they are close together.


# 4. Modify the chaos program so that it prints out 20 values instead of 10.
#    Solution:
     # File: chaos.py
     #A simple program illustrating chaotic behavior.
     def main():
         print("This program illustrates a chaotic function")
         x = eval(input("Enter a number between 0 and 1: "))
         for i in range(20):
             x = 3.9 * x * (1 - x)
             print(x)
        
# 5. [CORRECT]
#
# File: c01ex5.py
# Chaos program that prints a variable number of terms

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    n = eval(input("How many numbers should I print? "))
    for i in range(n):
        x = 3.9 * x * (1 - x)
        print(x)
        
main()
#         
# 6. The calculation performed in the chaos program can be written in a number of ways that are algebraically equivalent. Write a version of
#    the program for each of the following ways of doing the computation. Have your modified programs print out 100 iterations of the calculation
#    and compare the results when run on the same input.
#
#    Chaos programs:
#
#    a) 3.9 * x * (1 - x)                                                                   
#    def main():                                             
#        print("Ths program illustrates a chaotic function")
#        x = eval(input("Enter a number between 0 and 1: "))     
#        for i in range(100):                                    
#            x = 3.9 * x * (1 - x)
#            print(x)
#
#    b) 3.9 * x (x - x * x)
#     def main():
#         print("Ths program illustrates a chaotic function")
#         x = eval(input("Enter a number between 0 and 1: "))
#         for i in range (100):
#             x = 3.9 * (x - x * x)
#             print(x)
#             
#    c) 3.9 * x - 3.9 * x * x
#     def main():
#         print("Ths program illustrates a chaotic function")
#         x = eval(input("Enter a number between 0 and 1: "))
#         for i in range (100):
#             x = 3.9 * x - 3.9 * x * x
#             print(x)
#
#   Combined above in the following to produce easily transferable output:
##    >>> def chaotic(x):
##            a = x
##            b = x
##            c = x
##            for i in range(100):
##                    a = 3.9 * a * (1 - a)
##                    b = 3.9 * b * (b - b * b)
##                    c = 3.9 * c - 3.9 * c * c
##                    print("{0:<30.20}{1:<30.20}{2:<30.20}".format(a, b, c))
##
##                          
##    >>> chaotic(.23)
#
#     OUTPUT COMPARISON
#
# 3.9 * x * (1 - x)      3.9 * x (x - x * x)    3.9 * x - 3.9 * x * x
#
# 0.69069000000000002615 0.15885870000000001934 0.69069000000000002615        
# 0.83318556320999992426 0.082785747177030397093 0.83318556320999981324        
# 0.54205078382689708683 0.024515826965849165514 0.54205078382689730887        
# 0.96810375316021990422 0.0022865353991825096598 0.96810375316021990422        
# 0.12042761748153206491 2.0343529309084740176e-05 0.12042761748153196777        
# 0.41310674507409000933 1.6140179850332268054e-09 0.41310674507408973177        
# 0.94555329276868527177 1.0159710802043842996e-17 0.94555329276868493871        
# 0.2007808268816306807 4.0255692196654873797e-34 0.20078082688163201297        
# 0.62582475710960139281 6.3200309415040985005e-67 0.62582475710960450144        
# 0.9132557089434082398 1.5577688529611981437e-132 0.9132557089434052422         
# 0.30895690420015609057 9.4639108170985837432e-264 0.30895690420016563849        
# 0.83265988863412543353 0.0                           0.83265988863413964438        
# 0.54341585412633197638 0.0                           0.54341585412629500595        
# 0.96764874808087597557 0.0                           0.96764874808088863212        
# 0.12208812883171865638 0.0                           0.12208812883167263763        
# 0.41801220875734446114 0.0                           0.41801220875720879189        
# 0.94878420813988784133 0.0                           0.94878420813980102189        
# 0.18951166464458990557 0.0                           0.18951166464489377361        
# 0.59902827507208289415 0.0                           0.59902827507281886099        
# 0.93675426287136676073 0.0                           0.93675426287079832655        
# 0.23105828406838732625 0.0                           0.23105828407032369398        
# 0.69291437838386304993        0.0                           0.69291437838792502291        
# 0.82985776618979412156        0.0                           0.82985776618368189972        
# 0.55065603092868853352        0.0                           0.55065603094441462062        
# 0.96499246946915184786        0.0                           0.96499246946293815164        
# 0.13174981301422153401        0.0                           0.13174981303675847855        
# 0.44612801916126287871        0.0                           0.44612801922599687465        
# 0.96368145775399194353        0.0                           0.96368145778119318479        
# 0.13649807236701863578        0.0                           0.13649807226863952536        
# 0.45967875956771647727        0.0                           0.45967875928878065839        
# 0.96865937052300765675        0.0                           0.96865937043528071992        
# 0.11839773824181505646        0.0                           0.11839773856250479511        
# 0.40708088390204699714        0.0                           0.40708088485657922817        
# 0.94132754766794302093        0.0                           0.94132754835975851471        
# 0.2153969831106579691         0.0                           0.21539698072918334049        
# 0.65910437883219108457        0.0                           0.65910437354554707312        
# 0.87627460688204827921        0.0                           0.87627461344284807154        
# 0.42282793884146407937        0.0                           0.4228279195858974937         
# 0.95177344460851842634        0.0                           0.95177343301778127849        
# 0.17901294351156032958        0.0                           0.17901298435538048892        
# 0.57317250731086022419        0.0                           0.57317260957148707945        
# 0.95411855827798419671        0.0                           0.95411849991314512387        
# 0.17072770660734779002        0.0                           0.17072791334287584775        
# 0.55216105153537831107        0.0                           0.552161582499006931          
# 0.96438897634062192843        0.0                           0.96438876031367715136        
# 0.13393722674790622951        0.0                           0.1339380092478719142         
# 0.45239237955204608665        0.0                           0.45239461381369661108        
# 0.96616070645360574431        0.0                           0.96616153610360633319        
# 0.12750736345883334488        0.0                           0.12750434680435196455        
# 0.43387201931818025757        0.0                           0.43386325456635527198        
# 0.95794565166668510514        0.0                           0.95794113052343654591        
# 0.15711454246634290466        0.0                           0.15713069180217553722        
# 0.51647529574654504891        0.0                           0.51651848623418650241        
# 0.97394140205724921699        0.0                           0.97393584448887082772        
# 0.098980234922434504052       0.0                           0.099000779703621422101       
# 0.34781427726682334622        0.0                           0.34787853875461616227        
# 0.88467407260510455558        0.0                           0.88475033801141989009        
# 0.39790084567507066904        0.0                           0.39767199186038260095        
# 0.93434547447592353198        0.0                           0.93416301712569571603        
# 0.23924163432891096259        0.0                           0.23985965078521997995        
# 0.70981979145691609379        0.0                           0.71107529497060795176        
# 0.8033050549406072216         0.0                           0.80124415742697618903        
# 0.6162235702251533942         0.0                           0.62108263470283375796        
##    0.92231911872406346919        0.0                           0.91782208273633836271        
##    0.27942159164450847131        0.0                           0.29415635799368677894        
##    0.7852461464926963064         0.0                           0.80975074067774932551        
##    0.65767508005316221986        0.0                           0.60081246673338428721        
##    0.87804041960789269705        0.0                           0.93536370154940806643        
##    0.41763322045648482161        0.0                           0.2357879447554718233         
##    0.94854128314775687514        0.0                           0.70274876046750334169        
##    0.19036179751743878552        0.0                           0.81468246650267484021        
##    0.60108431589713684495        0.0                           0.58880228657559241512        
##    0.9351496482104705299         0.0                           0.94424520020589075564        
##    0.23651465628298459776        0.0                           0.20532018816670927208        
##    0.70424434722067241754        0.0                           0.6363388531417957239         
##    0.81230856185076549814        0.0                           0.90250569678352143832        
##    0.59460711255935561059        0.0                           0.34315773982156638766        
##    0.94009302758740753703        0.0                           0.87906197114627004918        
##    0.21964069556890244983        0.0                           0.41461688591974699136        
##    0.66845477563375355068        0.0                           0.94656792293683811312        
##    0.86432965540810879901        0.0                           0.19725065179512490943        
##    0.45732921854181390886        0.0                           0.61753704542994081184        
##    0.96789889719801613932        0.0                           0.92112166751124013864        
##    0.12117542580343326764        0.0                           0.28336051049495480925        
##    0.41531857374068065214        0.0                           0.79196259318927442195        
##    0.94703331858208117389        0.0                           0.64255559229495773366        
##    0.19562872710221693162        0.0                           0.89574382211119174535        
##    0.61369670011487476025        0.0                           0.36420862631721906411        
##    0.92458493549365405872        0.0                           0.90308674105003905463        
##    0.27193776695221349993        0.0                           0.34133220883966908232        
##    0.77215170964330281933        0.0                           0.87681567498837631458        
##    0.6861404430590868353         0.0                           0.42123879362391214443        
##    0.83987176828529064299        0.0                           0.95080702224371482778        
##    0.52450000637825577865        0.0                           0.18241481191344366408        
##    0.97265902378111512849        0.0                           0.58164462840130382038        
##    0.10371444422930464757        0.0                           0.94900320314753083828        
##    0.36253525732129326942        0.0                           0.18874488189670302063        
##    0.90130343362908016402        0.0                           0.59716898067256030114        
##    0.34692666121429072135        0.0                           0.93817693786071676421        
##    0.883617356516682384          0.0                           0.22620378739532176482 

#    Explain the results of this experiment. Hint: See discussion question number 4, above.
#
#    The results for 3.9 * x (x - x * x)  are easy to explain. Since x is a number between 0 and 1, the square of x will always
#    be smaller than x. In fact, x will approach closer and closer to 0 with each iteration. Eventually, the result exceeds
#    the range of a float, and then 0.0 is returned.
#
#    The results for 3.9 * x * (1 - x) and 3.9 * x - 3.9 * x * x are similar up to a point, but not exactly similar. This should be intuitively
#    apparent because, while the results would be exactly the same for integers, for the float data type it is not. This is because the result of each
#    operation will return only an approximation. Over time, the small disparities will snowball into larger ones.
#
#    Algebraic equivalence does not guarantee equivalent results for a floating point data type. Because all results are approximations, changing
#    the operations to something algebraicaly equivalent will produce unequivalent results. The intermediate values are inexact and will be stored differently.

# 7. (Advanced) Modify the chaos program so that it accepts two inputs and then prints a table with two columns similar to the one shown in Section
#    1.8. (Note: You will probably not be able to get the columns to line up as nicely as those in the example. Chapter 5 discusses how to print
#    numbers with a fixed number of decimal places).

#    Basic version with bad formatting.

def main():
     print("Ths program illustrates a chaotic function")
     x, y = eval(input("Enter 2 numbers between 0 and 1 separated by a comma: "))
     print("input   ", x, "         ", y, " ")
     print("---------------------------")
     for i in range (10):
         x = 3.9 * x * (1 - x)
         y = 3.9 * y * (1 - x)
         print(x, "   ", y)
     
main()

#    More secure version with bad formatting.
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

#    More secure version with good formatting.

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




