#!/usr/bin/env python
# _*_ coding: utf-8 _*_
"""Task 1 created"""

BASE = raw_input('''Which base color, "Seattle Gray", or "Manatee": ''')

if BASE == "Seattle Gray":
    ACCENT = raw_input('''Which accent color, "Ceramic Glaze", or "Cumulus
Nimbus": ''')
    if ACCENT == "Ceramic Glaze":
        HIGHLIGHT = raw_input('''Which highlight color, "Basically white", or
"White": ''')
    elif ACCENT == "Cumulus Nimbus":
        HIGHLIGHT = raw_input('''Which highlight color, "Off-White", or "Paper
White":''')

if BASE == "Manatee":
    ACCENT = raw_input('''Which accent color, "Platinum Mist" or "Spartan Sage":
''')
    if ACCENT == "Platinum Mist":
        HIGHLIGHT = raw_input('''Which highlight color, "Bone White", or "Just
White": ''')
    elif ACCENT == "Spartan Sage":
        HIGHLIGHT = raw_input('''Which highlight color, "Fractal White", or "Not
White": ''')


COLORS = 'Your selected colors are, {A}, {B}, {C}'.format(A=BASE, B=ACCENT,
                                                          C=HIGHLIGHT)

print COLORS
