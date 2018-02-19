#!/usr/bin/python3

import re
import sys


week = ['Mo', 'Tu', 'We', 'Th', 'Fr', 'Sa', 'Su']
def disektos(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

#Φτιαχνέι το αρχειο Cale
def make_calendar(year, start_day):
    calender = [('January', range(1, 31 + 1)),
                ('Feburary', range(1, 28 + 1)),
                ('March', range(1, 31 + 1)),
                ('April', range(1, 30 + 1)),
                ('May', range(1, 31 + 1)),
                ('June', range(1, 30 + 1)),
                ('July', range(1, 31 + 1)),
                ('August', range(1, 31 + 1)),
                ('September', range(1, 30 + 1)),
                ('October', range(1, 31 + 1)),
                ('November', range(1, 30 + 1)),
                ('December', range(1, 31 + 1))]

    start_pos = week.index(start_day)

    if disektos(year):
        calender[1] = ('Feburary', range(1, 29 + 1))

    for month, days in calender:
        calen.write('{0} {1}'.format(month, year).center(20, ' '))
        calen.write('\n')

        calen.write(''.join(['{0:<3}'.format(w) for w in week]))
        calen.write('\n')

        calen.write('{0:<3}'.format('')*start_pos)

        for day in days:
            calen.write('{0:<3}'.format(day))
            start_pos += 1
            if start_pos == 7:
                calen.write("\n")
                start_pos = 0
        calen.write('\n')


#Ψάχνεις τις δευτερες μεσα στο αρχειο
def check():
    cale = open("Cale","r")
    spastiras = []
    i=0
    for line in cale:
        spastiras = line.split()
        if not spastiras:
            pass
        elif spastiras[0] == "8":
            i = i + 1
    print ("Deuteres 8 tou mina sta epomena 10 xronia: ", i)



epilogi = input("If you want to make a calendar file press 'C' else press Enter \n")
if (epilogi == "C" or epilogi =="c"):
    calen = open("Cale","w+")
    firstdays = ["Mo", "Tu" , "We" , "Fr" , "Sa" , "Su" , "Mo" , "We" , "Th" , "Fr" , "Sa" ]
    for year, firstday in zip(range(2018,2029) , firstdays):
        make_calendar(year,firstday)
    print ("Rerun the programm")
else:
    check()
