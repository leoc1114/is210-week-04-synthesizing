#!usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 2"""


DAY = raw_input('What day is it? ')
DAY = DAY.lower()

TIME = raw_input('What time is it? Please input it in 4 digits: ')
TIME = int(TIME)

if DAY != 'Sat' or 'Sun' or TIME > 0600:
    SNOOZE = False
    print 'Beep! '*5
else:
    SNOOZE = True
