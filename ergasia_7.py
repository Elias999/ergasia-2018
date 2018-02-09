import calendar
import sys

#Φτίαχνει το αρχειό με τις ημερομηνιες για τα επομενα 10 χρόνια
def makeCale():
    c = calendar.TextCalendar(calendar.MONDAY)
    #c_1 = calendar.weekday(2018,1,11)
    calen = open("Cale","w+")
    for x in range(2018,2029):
        for i in range(1,13):
            str = c.formatmonth(x,i)
            calen.write(str)
    calen.close()

#Ψάχνεις τις δευτερες μεσα στο αρχειο
def check():
    cale = open("Cale","r")
    spastiras = []
    i=0
    for line in cale:
        spastiras=line.split(' ')
        try:
            if spastiras[1]=="8":
                i = i+1
        except Exception:
            pass
    print(i)

#Κύρια συνάρτηση
def main():
    epilogi = input("If you want to make a calendar file press 'C' else press Enter \n")
    if (epilogi == "C" or epilogi =="c"):
        makeCale()
        main()
    else:
        check()
        sys.exit("You're welcome")


main()
