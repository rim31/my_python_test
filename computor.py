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
    disc = b * b - 4 * a * c
    print disc
    print str(a) + " * X^2 + " + str(b) + " * X^1 + " + str(c) +" * X^0 = 0 "
    if a == 0 & b == 0 & c == 0:
        print "infinite de solution "
    elif a == 0:
        print "equation du 1er degre "
        print "soution X = " + str(-c/b)
    elif disc > 0:
        print "discriminant > 0 :  2 resultats "
        res1 = (-b - math.sqrt(disc))/ ( 2 * a)
        res2 = (-b + math.sqrt(disc))/ ( 2 * a)
        print "X1 = " + str(res1)
        print "X2 = " + str(res2)
    elif disc == 0:
        print "discriminant = 0 :  1 resultat"
        res1 = -b / ( 2 * a)
    else:
        print "discriminant < 0 :  2 resultats imaginaires ou pas de resultat"
        res1 = -b / (2*a)
        res1i = math.sqrt(math.fabs(disc)) / (2*a)
        print "X1 : " + str(res1) + " + i" + str(res1)
        res2 = -b / (2*a)
        res2i = -math.sqrt(math.fabs(disc)) / (2*a)
        print "X1 : " + str(res2) + " + i" + str(res2)


def parse(lhs, rhs):
    print lhs + ", " + rhs

    # eqtest = re.findall(r'([+-]*([\-\+]?[\ +-]?[0-9]*(\.[0-9]+)?)\ \* X\^\d+.\d+)', av)
    coef1 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', lhs)
    coef2 = re.findall(r'((?<!\^)[+-]?\ ?(\d)+\.?(\d?)+)', rhs)

#ax2 +bx +c = 0
    c = float(coef1[0][0].replace(" ","")) - float(coef2[0][0].replace(" ",""))
    b = float(coef1[1][0].replace(" ",""))
    a = float(coef1[2][0].replace(" ",""))
    # if coef1[3][0]:
    #     print "erreur equation du 3nd degre"
    # else:
    #     discriminant(a, b, c)

    discriminant(a, b, c)


#======================MAIN=========================
if len(sys.argv) == 2:
    # print "argv[1]: c * X^0 + b * X^1 - a * X^2 = d * X^0" , str(sys.argv[1])
    parse(getRhs(sys.argv[1]), getLhs(sys.argv[1]))
