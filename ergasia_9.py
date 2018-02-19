#!/usr/bin/python3

def changer(x,data_pointer,registry_list,command_num):
    i = x
    command_num = command_num
    if i == ">" or i == "<":
        data_pointer = pointer(i,data_pointer)
        print ("currenly at: ",data_pointer)
    elif i == "+":
        if registry_list[data_pointer] <= 255:
            registry_list[data_pointer] = registry_list[data_pointer] + 1
    elif i == "-":
        if registry_list[data_pointer] > 0:
            registry_list[data_pointer] = registry_list[data_pointer] - 1
    elif i == ".":
        print (registry_list[data_pointer])
    elif i == ",":
        x = int(input())
        if x >= 0 or x <= 255:
            registry_list[data_pointer] = x
        else:
            print ("Error")
    elif i == "[":
        if registry_list[data_pointer] == 0:
            cur_command = command_num
            command_num1 = 0
            for z in program_list:
                command_num1= command_num1 + 1
                if command_num1 >= cur_command:
                    data_pointer = data_pointer + 1
                if z == "]":
                    data_pointer = data_pointer + 1
                    break
    elif i == "]":
        if registry_list[data_pointer] != 0:
            cur_command = command_num
            command_num1 = command_num
            for z in program_list:
                if command_num1 == 0:
                    break
                elif command_num1 <= cur_command:
                    data_pointer = data_pointer - 1
                elif z == "[":
                    data_pointer = data_pointer + 1

    else:
        print ('Not accepted char')
    return data_pointer

def pointer(chrctr,data_pointer):
    if chrctr == ">":
        data_pointer = data_pointer + 1
    elif chrctr == "<" :
        if data_pointer != 0:
            data_pointer = data_pointer - 1
    return data_pointer

def file_main():
    data_pointer=0
    registry_list=[0] * 30000
    program_list=[]
    char_counter = 0
    bf_file = input("Input brainfuck program: ")
    with open(bf_file, 'r') as file1:
        for line in file1:
            for chrctr in line:
                if chrctr != "\n":
                    program_list.append(chrctr)
        command_num=0
        for i in program_list:
            command_num = command_num + 1
            if i == ">" or i == "<":
                data_pointer = pointer(i,data_pointer)
            elif i == "+":
                if registry_list[data_pointer] <= 255:
                    registry_list[data_pointer] = registry_list[data_pointer] + 1
            elif i == "-":
                if registry_list[data_pointer] > 0:
                    registry_list[data_pointer] = registry_list[data_pointer] - 1
            elif i == ".":
                print (registry_list[data_pointer])
            elif i == ",":
                x = input()
                if x >= 0 or x <= 255:
                    registry_list[data_pointer] = x
                else:
                    print ("Error")
            elif i == "[":
                if registry_list[data_pointer] == 0:
                    cur_command = command_num
                    command_num1 = 0
                    for z in program_list:
                        command_num1= command_num1 + 1
                        if command_num1 >= cur_command:
                            data_pointer = data_pointer + 1
                        if z == "]":
                            data_pointer = data_pointer + 1
                            break
            elif i == "]":
                if registry_list[char_counter] != 0:
                    cur_command = command_num
                    command_num1 = command_num
                    for z in program_list:
                        if command_num1 == 0:
                            break
                        elif command_num1 <= cur_command:
                            data_pointer = data_pointer - 1
                        elif z == "[":
                            data_pointer = data_pointer + 1


            else:
                print ('Not accepted char')
        #print (registry_list) to apotelesma

#def Input_main():
    #data_pointer=0
    #registry_list=[0] * 30000
    #print("The brainfuck starts now!")
    #while True:
    #    i = input()
    #    if len(i) > 1:
    #        command_num = 0
    #        for x in i:
    #            command_num =  command_num + 1
    #            data_pointer = changer(x,data_pointer,registry_list,command_num)
    #    else:
    #        command_num = 0
    #        data_pointer = changer(i,data_pointer,registry_list,command_num)

#Η επιλογη Ι Λειτουργει για ολους του χαρακτηρες εκτος απο "[","]"
epilogi = input(" 'C' for Compiler file or 'I' for input() : ")
if epilogi == "C" or epilogi == "c":
    file_main()
elif epilogi == "I" or epilogi == "i":
    print("Look source code")
    #Input_main()
