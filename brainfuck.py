#/usr/bin/ python3

def pointer(chrctr,data_pointer):
    if chrctr == ">":
        data_pointer = data_pointer + 1
    elif chrctr == "<" :
        if data_pointer != 0:
            data_pointer = data_pointer - 1
    return data_pointer


bf_file = input("Input brainfuck program: ")
data_pointer=0
registry_list=[0] * 30001
program_list=[]
with open(bf_file, 'r') as file1:
    for line in file1:
        for chrctr in line:
            if chrctr != "\n":
                program_list.append(chrctr)
#all_char = (len(program_list))
char_counter = 0

for i in program_list:
    if i == ">" or i == "<":
        data_pointer = pointer(i,data_pointer)
    elif i == "+":
        if registry_list[char_counter] <= 255:
            registry_list[char_counter] = registry_list[char_counter] + 1
    elif i == "-":
        if registry_list[char_counter] > 0:
            registry_list[char_counter] = registry_list[char_counter] - 1
    elif i == ".":
        print (registry_list[char_counter])
    elif i == ",":
        x = int(input())
        if x >= 0 or x <= 255:
            registry_list[char_counter] = x
        else:
            print ("Error")
#edw emeina     elif i == "[":
        if registry_list[char_counter] == 0:
            while True:
                if char_counter < 30000:
                    char_counter = char_counter + 1
                if registry_list[char_counter] == "]":
                    char_counter = char_counter + 1
                    break
    elif i == "]":
        if registry_list[char_counter] == 1:
            while True:
                if char_counter > 0:
                    char_counter = char_counter - 1
                if
