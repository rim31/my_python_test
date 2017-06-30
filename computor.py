#!/usr/bin/python

import sys
import re
import math


# "(?<!\^)[+-]?\ ?(\d)+\.?(\d?)+"
# "^[^=]*" -> recupere la partie de gauche
# "=(.*)" -> recupere la partie de droite avec le =

def getRhs(str):
    rhs = re.findall(r'^[^=]*', str)
    return rhs[0]

def getLhs(str):
    lhs = re.findall(r'=(.*)', str)
    return lhs[0]

def discriminant(a, b, c):#ax2 +bx +c = 0

    string = "Reduced form : "

    if c != 0:
        string += str(c) + " * X^0"
    if b != 0:
        if c != 0:
            string += (" + " if b > 0 else " - ")
        string += str(math.fabs(b)) + " * X^1"
    if a != 0:
        if b != 0 or c != 0:
            string += (" + " if a > 0 else " - ")
        string += str(math.fabs(a)) + " * X^2"

    if a == 0 and b == 0 and c == 0:
        print string + "0 = 0\ninfinite de solutions "
    elif a == 0 and b == 0 and c != 0:
        print string + " = 0"
        print "impossible ??"
    elif a == 0:
    # if a == 0:
        print string + " = 0"
        print "Polynomial degree: 1"
        print "soution X = " + str(-c/b)

    if a != 0:
        disc = b * b - 4 * a * c
        print string + " = 0"
        print "Polynomial degree: 2"
        if disc > 0:
            print "discriminant > 0 :  2 resultats "
            res1 = (-b - math.sqrt(disc))/ ( 2 * a)
            res2 = (-b + math.sqrt(disc))/ ( 2 * a)
            print "X1 = " + str(res1)
            print "X2 = " + str(res2)
        elif disc == 0:
            print "discriminant = 0 :  1 resultat"
            print "X : " + str(-b / ( 2 * a))
        else:
            print "discriminant < 0 :  2 resultats imaginaires ou pas de resultat"
            res1 = -b / (2*a)
            res1i = math.sqrt(math.fabs(disc)) / (2*a)
            print "X1 : " + str(res1) + (" + " if res1i > 0 else " - ") + str(math.fabs(res1i)) + "i"
            res2 = -b / (2*a)
            res2i = -math.sqrt(math.fabs(disc)) / (2*a)
            print "X2 : " + str(res2) + (" + " if res2i > 0 else " - ") + str(math.fabs(res2i)) + "i"


def parse(lhs, rhs):
    # print lhs + ", " + rhs

    # eqtest = re.findall(r'([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+.\d+)', av)
    coef1 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', lhs)
    coef2 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', rhs)

#ax2 +bx +c = 0

    # print (len(coef1))
    # print (len(coef2))

    lenC = len(coef1)
    lenC2 = len(coef2)

    tabC = []
    tabC2 = []

    tabCoeff = [0, 0, 0]

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

    # print tabC
    # print tabC2
    # print tabCoeff

    discriminant(tabCoeff[2], tabCoeff[1], tabCoeff[0])

    # while ()

    # if lenC > 3:

    # if lenC > 0:
    #     a = 0
    #     b = 0
    #     c = float(coef1[0][0].replace(" ","")) - float(coef2[0][0].replace(" ",""))
    #     if lenC > 1:
    #         b = float(coef1[1][0].replace(" ",""))
    #     if len(coef2) > 1:
    #         b -= float(coef2[1][0].replace(" ",""))
    #     if lenC > 2:
    #         a = float(coef1[2][0].replace(" ",""))
    #     if len(coef2) > 2:
    #         a -= float(coef2[2][0].replace(" ",""))
    #     discriminant(a, b, c)

    # if coef1[3][0]:
    #     print "erreur equation du 3nd degre"
    # else:
    #     discriminant(a, b, c)
    #
    # discriminant(a, b, c)


#======================MAIN=========================
if len(sys.argv) == 2:
    # print "argv[1]: c * X^0 + b * X^1 - a * X^2 = d * X^0" , str(sys.argv[1])
    parse(getRhs(sys.argv[1]), getLhs(sys.argv[1]))
