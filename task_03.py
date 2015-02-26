#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 3"""


Name = raw_input('What is your name? ')
PRINCIPAL = raw_input('What is the amount of your principle? ')
PRINCIPAL = int(Principal)
YEARS = raw_input('For how many years is this loan being borrowed? ')
YEARS = int(Years)
PREQUALIFIED = raw_input('Are you pre-qualified for this loan? ')

import decimal

if 0 <= PRINCIPAL <= 199999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('3.63')
        elif PREQUALIED == No:
            RATE = decimal.Decimal('4.65')
    if YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('4.04')
        elif PREQUALIED == No:
            RATE = decimal.Decimal('4.98')
    if YEARS >=21 and YEARS <= 30:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('5.77')
        elif PREQUALIFIED == No:
            RATE = decimal.Decimal('6.39')

if 200000 <= Principal <= 999999:
    if YEARS >= 1 and YEARS <= 15:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('3.02')
        elif PREQUALIED == No:
            RATE = decimal.Decimal('3.98')
    if YEARS >= 16 and YEARS <= 20:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('3.27')
        elif PREQUALIED == No:
            RATE = decimal.Decimal('4.08')
    if YEARS >=21 and YEARS <= 30:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('4.66')

if Primcipal >= 1000000:
    if YEARS >=1 and YEARS <=15:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('2.05')
    if YEARS >= 16 and YEARS <=15:
        if PREQUALIFIED == Yes:
            RATE = decimal.Decimal('2.62')

print 'Loan report for: NAME'
A = '-' * 20

            


