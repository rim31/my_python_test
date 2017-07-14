#!/usr/bin/python

import sys
import re
# import math

#===========REGEX=========
# "(?<!\^)[+-]?\ ?(\d)+\.?(\d?)+"
# "^[^=]*" -> recupere la partie de gauche
# "=(.*)" -> recupere la partie de droite avec le =

def sqrt(nb):
    i = 0
    if nb < 0:
        nb *= -1
    while i * i < nb:
        i += 0.00001
    # print str(i)
    return i

def sqrt3(nb):
    i = 0
    if nb < 0:
        nb *= -1
    while i * i * i< nb:
        i += 0.00001
    return i

def getRhs(str):
    rhs = re.findall(r'^[^=]*', str)
    return rhs[0]

def getLhs(str):
    lhs = re.findall(r'=(.*)', str)
    return lhs[0]

#===========================================================================

def discriminant(a, b, c):#ax2 +bx +c = 0

    string = "\033[1;31mresolution de :\033[0m "

    if c != 0:
        string += str(c) + " * X^0"
    if b != 0:
        if c != 0:
            string += (" + " + str(b) if b > 0 else " - " + str(-b)) + " * X^1"
        # string += str(sqrt(b*b)) + " * X^1"
    if a != 0:
        if b != 0 or c != 0:
            string += (" + " + str(a) if a > 0 else " - " + str(-a)) + " * X^2"
        # string += str(sqrt(a*a)) + " * X^2"

    if a == 0 and b == 0 and c == 0:
        print string + "0 = 0\ninfinite de solutions "
    elif a == 0 and b == 0 and c != 0:
        print string + " = 0"
        print "impossible ??"
    elif a == 0:
        print string + " = 0"
        print "Polynomial degree: 1"
        print "soution X = " + str((-c/b))

    if a != 0:
        disc = b * b - 4 * a * c
        print string + " = 0"
        print " etape intermediaire => Polynomial degree: 2"
        print "discriminant : b^2 - 4ac : " + str(disc)
        if disc > 0:
            print "discriminant > 0 :  2 resultats "
            res1 = round((-b - sqrt(disc))/ ( 2 * a),4)
            res2 = round((-b + sqrt(disc))/ ( 2 * a),4)
            print "solution : X1/2 = (-b +/- sqrt(discriminant) )/ 2a"
            print "X1 = " + str(res1)
            print "X2 = " + str(res2)
        elif disc == 0:
            print "discriminant = 0 :  1 resultat"
            print "solution : X1/2 = -b / 2a"
            print "X : " + str(-b / ( 2 * a))
        else:
            print "discriminant < 0 :  2 resultats imaginaires ou pas de resultat"
            print "solution : X1/2 = (-b +/- sqrt(discriminant)i )/ 2a"
            res1 = round(-b / (2*a), 4)
            # res1i = sqrt(sqrt(disc*disc)) / (2*a)
            res1i = round(sqrt(disc if disc > 0 else -disc), 4)
            print "X1 : " + str(res1) + (" + " if res1i > 0 else " - ") + str(sqrt(res1i*res1i)) + "i"
            res2 = round(-b / (2*a), 4)
            res2i = round(-sqrt(disc if disc > 0 else -disc),4)
            print "X2 : " + str(res2) + (" + " if res2i > 0 else " - ") + str(sqrt(res2i*res2i)) + "i"


#===========================================================================

def reduce3(tabCoeff):#ax^n +bx^n-1 +c...
    string = "Reduced form : "
    debut = 0
    for i in range(0, len(tabCoeff)):
        if i > 0:
            string += (" + " if tabCoeff[i] >= 0 else " ")
        string += str(tabCoeff[i]) + " * X^" + str(i)
    print string + " = 0"
    print "\033[1;36mPolynomial degree: \033[0m" + str(len(tabCoeff) - 1)
#resoution equarion du 3 degree : https://www.lucaswillems.com/fr/articles/58/equations-troisieme-degre?cache=update
    # print (tabCoeff)
    if len(tabCoeff) == 4:
        d = tabCoeff[0]
        c = tabCoeff[1]
        b = tabCoeff[2]
        a = tabCoeff[3]
        print "resolution de l'equation de degree 3 : Bonus cache ;-), \nsoit sympa\n"
        p = (3*a*c-b*b)/(3*a*a)
        q = (2*b*b*b-9*a*b*c+27*a*a*d)/(27*a*a*a)
        delta = q*q + (4*p*p*p)/27

        if delta < 0:
            print "solution trop complique"
        else:
            x1 = sqrt3(((-q-sqrt(delta if delta > 0 else -delta))/2)) + sqrt3(((-q+sqrt((delta if delta > 0 else -delta)))/2))
            # x1 = math.pow(((-q-math.sqrt(delta))/2), 1.0/3.0) + math.pow(((-q+math.sqrt(delta))/2), 1.0/3.0)
            print "X1 = " + str(x1)
    #changement de variable
            delta2 = (b+a*x1)*(b+a*x1) - 4*a*(c+(b+a*x1)*x1)
            if delta2 > 0:
                print "X2 = " + str((-b-a*x1-sqrt(delta2))/(2*a))
                print "X3 = " + str((-b-a*x1+sqrt(delta2))/(2*a))
            else:
                res3i = (sqrt(delta2 if delta2 > 0 else -delta2))/(2*a)
                print "X2 = " + str((-b-a*x1)/(2*a)) + (" + " if res3i > 0 else " - ") + str(res3i if res3i > 0 else -res3i) + "i"
                print "X3 = " + str((-b-a*x1)/(2*a)) + (" - " if res3i > 0 else " + ") + str(res3i if res3i > 0 else -res3i) + "i"
                # print "X3 = " + str((-b-a*x1)/(2*a)) + (" - " if res3i > 0 else " + ") + str(math.fabs(res3i)) + "i"
            print "methode de Tschirnhaus"
            print "recherche de X1, ensuite on fait un changement de variable en factorisant avec (x-X1)(aX^+bX+c)"
            print "on recharche alors le nouveau discriminant delta2"

    if len(tabCoeff) <= 3:
        discriminant(tabCoeff[2], tabCoeff[1], tabCoeff[0])


def parse(lhs, rhs):
    # print lhs + ", " + rhs
    coef1 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', lhs)
    coef2 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', rhs)

#ax2 +bx +c = 0
 # print (len(coef1)) # print (len(coef2))

    tabC = []
    tabC2 = []
    tabCoeff = [0, 0, 0]
    lenC = len(coef1)
    lenC2 = len(coef2)

    maxLen = lenC if lenC > lenC2 else lenC2

    for i in range(0, maxLen):
        if i < lenC:
            tabC.append(float(coef1[i][0].replace(" ","")))
        else:
            tabC.append(0)
        if i < lenC2:
            tabC2.append(float(coef2[i][0].replace(" ","")))
        else:
            tabC2.append(0)
        if i > 2:
            tabCoeff.append(tabC[i] - tabC2[i])
        else:
            tabCoeff[i] = tabC[i] - tabC2[i]

    if maxLen > 2:
        reduce3(tabCoeff)
    else:
        discriminant(tabCoeff[2], tabCoeff[1], tabCoeff[0])


#======================MAIN=========================
if len(sys.argv) == 2:
    # print "argv[1]: c * X^0 + b * X^1 - a * X^2 = d * X^0" , str(sys.argv[1])
    if sys.argv[1].find("=") != -1:
        parse(getRhs(sys.argv[1]), getLhs(sys.argv[1]))
elif len(sys.argv) == 1:
    equation = raw_input("Entrez une equation bien formatee : \"A * X^0 + B * X^1 + C * X^2 = 0\" \nau bon format please \n")
    if equation.find("=") != -1:
        parse(getRhs(equation), getLhs(equation))
    else:
        print "please enter an equation like : \"A * X^0 + B * X^1 + C * X^2 = D * X^0\"\nau bon format please \n"
else:
    print "please enter an equation like : \"A * X^0 + B * X^1 + C * X^2 = D * X^0\"\nau bon format please \n"
