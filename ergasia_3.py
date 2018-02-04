import os, sys
alphabet = ["A", "B", "C", "D" ,"E" ,"F" , "G", "H", "I", "J","K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
rot13 = []
numbers = ['1','2','3','4','5','6','7','8','9']
def allagi():
        for thesi,x in enumerate(alphabet):
            if letter == x:
                if thesi <=12:
                    thesi = thesi + 13
                else:
                    thesi = thesi - 13
                rot13.append(alphabet[thesi])
while True:
    os.system('clear')
    epilogi = input("Give 'I' to type a text or 'F' for insert a text file or 'X' for exit: \n")
    if epilogi == "I" or epilogi == "i":
        keimeno = input("Give the text for encode it to ROT13: \n")
        keimeno_kefalaia = keimeno.upper()
        for letter in keimeno_kefalaia:
            if letter in numbers or letter == ' ':
                rot13.append(letter)
            else:
                allagi()


        kalo = ''.join(rot13)
        print (kalo)
        sys.exit("You're welcome")
    elif epilogi == "F" or epilogi == "f":
        onoma = input("Give the file's name: \n")
        keimeno = open(onoma,'r')
        text = keimeno.read()
        keimeno.close()
        keimeno_kefalaia = text.upper()
        for letter in keimeno_kefalaia:
            if letter in numbers or letter == ' ':
                rot13.append(letter)
            else:
                allagi()
        kalo = ''.join(rot13)
        print (kalo)
        sys.exit("You're welcome")
    elif epilogi == "X" or epilogi =="x":
        sys.exit("Bye")
