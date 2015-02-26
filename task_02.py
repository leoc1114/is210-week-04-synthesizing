#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2"""


DAY = raw_input('What day is it? ')
DAY = DAY.lower()

TIME = raw_input('What time is it? Please input it in 4 digits: ')
TIME = int(TIME)

SNOOZE = True if (DAY == 'Sat' or DAY == 'Sun') or TIME < 0600 else False
    
if SNOOZE is False:
    print 'BLEEP! ' * 5
    
