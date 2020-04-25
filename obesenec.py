# Hra obesenec

import random
import os

print("***********************************\n*           *Obesenec*            *\n***********************************\n*coded by: Jakub Krsak, Jan Krsak *\n*version: 1.0.1                   *\n***********************************\n\n\n\n\n\n\n\n")

#sibenica
sibenice = ["             ", "             ", "             ", "             ", "             ", "             ", "             ", "          _/ \_", 
"             ", "            |", "            |", "            |", "            |", "            |", "            |", "          _/ \_", 
"|-----------|", "            |", "            |", "            |", "            |", "            |", "            |", "          _/ \_", 
"|-----------|", "|           |", "            |", "            |", "            |", "            |", "            |", "          _/ \_", 
"|-----------|", "|_          |", "( )         |", "            |", "            |", "            |", "            |", "          _/ \_", 
"|-----------|", "|_          |", "( )         |", " |          |", "            |", "            |", "            |", "          _/ \_", 
"|-----------|", "|_          |", "( )         |", " |          |", "/|\         |", "            |", "            |", "          _/ \_", 
"|-----------|", "|_          |", "( )         |", " |          |", "/|\         |", " |          |", "            |", "          _/ \_",
"|-----------|", "|_          |", "( )         |", " |          |", "/|\         |", " |          |", "/ \         |", "          _/ \_"]

#random word from list

random_word = random.choice(["bobo", "pako", "cvok", "bobk", "gadzo", "macka", "strom", "hrad", "pelikan", "dedoles", "ikebana", "vajicko", "luga", "pipa", "mravciar", "uskatec"])
random_word_len = len(random_word)
zoznam_pis = []
x = 1
foo = []
integer1 = 0
integer2 = 8
badTry = 0

zoznam_pis += random_word

for i in range(random_word_len):
    foo.append("_")

print(foo)

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

def sibenica(integer1, integer2):
    for counter in sibenice[integer1:integer2]:
        print(counter)

while integer2 <= 72:
    pismeno = input("pismeno: ")
    cls()
    if len(pismeno) == 1:
        if pismeno in zoznam_pis:
            print("pismeno sa tam nachadza!!!")
            index = [z for z, y in enumerate(zoznam_pis) if y == pismeno]
            #print(index)
            for item in index: 
                #int_1 = index.pop(item)
                foo[item] = pismeno
            if badTry >= 1: sibenica(integer1 - 8,integer2 - 8)
            print(foo)
            if foo == zoznam_pis:
                print("UHADOL SI SLOVO:", random_word)
                quit()
        else:
            print("pismeno sa tam nenachadza!!!")
            sibenica(integer1, integer2)
            print(foo)
            integer1 += 8
            integer2 += 8
            badTry += 1
    else:
        print("Zadaj iba jedno pismeno!!!")
        x -= 1
    x += 1
else:
    print("NEUHADOL SI SLOVO:", random_word)
    quit()