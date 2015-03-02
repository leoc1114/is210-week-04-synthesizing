#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3"""


NAME = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount of your principle? ')
PRINCIPAL = int(PRINCIPLE)
YEARS = raw_input('For how many years is this loan being borrowed? ')
YEARS = int(YEARS)
PREQUALIFIED = raw_input('Are you pre-qualified for this loan? ')
PREQUALIFIED == True if 'Y' else False
RATE = None
RATE = R
COMPOUNDS = 12
TOTAL = None

import decimal

if 0 <= PRINCIPAL <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('3.63')
        elif PREQUALIED == N:
            R = decimal.Decimal('4.65')
    if YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('4.04')
        elif PREQUALIED == No:
            R = decimal.Decimal('4.98')
    if YEARS >=21 and YEARS <= 30:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('5.77')
        elif PREQUALIFIED == N:
            R = decimal.Decimal('6.39')

if 200000 <= PRINCIPAL <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('3.02')
        elif PREQUALIED == N:
            R = decimal.Decimal('3.98')
    if YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('3.27')
        elif PREQUALIED == N:
            R = decimal.Decimal('4.08')
    if YEARS >=21 and YEARS <= 30:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('4.66')

if PRINCIPAL >= 1000000:
    if YEARS >=1 and YEARS <=15:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('2.05')
    if YEARS >= 16 and YEARS <=20:
        if PREQUALIFIED == Y:
            R = decimal.Decimal('2.62')            

TOTAL = PRINCIPAL * ((1 + R / COMPOUND)**(COMPOUND * YEARS))
        
