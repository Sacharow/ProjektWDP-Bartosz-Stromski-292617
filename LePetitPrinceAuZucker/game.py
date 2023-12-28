import random

def sum_of_number(k,decision):
    sumas=0
    for i in range(5):
        if k[i]==decision:
            sumas+=decision
    print(sumas)
    f = open("wynik.txt", "r")
    lines=f.readlines()
    f.close()
    f = open("wynik.txt", "w")
    for i in range(14):
        if i==decision-1:
            f.writelines(str(sumas)+'\n')
        else:
            f.write(lines[i])
    f.close()

def reading_numbers():
    print("#####################################") #Przerywnik
    f = open("wynik.txt", "r")
    lines=f.readlines()
    for i in range(14):
        print(i+1," : ", lines[i], end='')
    f.close()

k=[0,0,0,0,0]

for kolejka in range(2):
    print("#####################################") #Przerywnik
    print("WYNIKI RZUTU")
    k[0]=random.randint(1,6)
    k[1]=random.randint(1,6)
    k[2]=random.randint(1,6)
    k[3]=random.randint(1,6)
    k[4]=random.randint(1,6)
    for i in range(5):
        print(k[i])
    reading_numbers()
    print("#####################################") #Przerywnik
    print("Wybierz Sposób Punktacji")
    print("Dla przerzutu wybierz 0")
    decision=int(input())
    if decision>0 and decision<7:
        sum_of_number(k,decision)
    print("#####################################") #Przerywnik
    print("#####################################") #Przerywnik
    print("#####################################") #Przerywnik
reading_numbers()