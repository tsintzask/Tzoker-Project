'''
This program is simulating as many τζοκερ (greek lotto-like luck based game) as the user wants
and prints the amount of times you won.. Maybe there are logical errors in there, I didn't really
test this a lot

This is my first "project" that has over 100 lines of code... I am sure the code can be improved
but I am a student still learning so pls don't mind the bad code.. Let me know if you spot any mistakes in the code
that can be fixed to make the program better :)

TO DO LIST (ETA: Never)
-Show the amount of money you would have won (and maybe the money you lost)
-Add more input validation at the point the user enters the numbers

'''


import random

ERROR = [
"This number already exists!",
"Invalid value!"
]

possible_normal_numbers = [] # Contains integers 1-45
for i in range(1,46):
    possible_normal_numbers.append(i)

user_number_list = []
random_number_list = []

def RandGen():
    global random_number_list
    random_number_list = random.sample(possible_normal_numbers,5)
    random_number_list.sort()
    random_number_list.append(random.randint(1,20))
    # This function generates 5 random normal numbers
    # and one "tzoker" number for the "random_number_list"

def AskUser():
    global user_number_list
    print('Enter the 5 normal numbers (1-45)')
    n1 = int(input())
    while n1 < 1 or n1 > 45:
        print(ERROR[1])
        n1 = int(input())


    n2 = int(input())
    while n2 == n1:
        print(ERROR[0])
        n2 = int(input())
    while n2 < 1 or n2 > 45:
        print(ERROR[1])
        n2 = int(input())
        while n2 == n1:
            print(ERROR[0])
            n2 = int(input())


    n3 = int(input())
    while n3 == n1 or n3 == n2:
        print(ERROR[0])
        n3 = int(input())
    while n3 < 1 or n3 > 45:
        print(ERROR[1])
        n3 = int(input())
        while n3 == n1 or n3 == n2:
            print(ERROR[0])
            n3 = int(input())

    n4 = int(input())
    while n4 == n1 or n4 == n2 or n4 == n3:
        print(ERROR[0])
        n4 = int(input())
    while n4 < 1 or n4 > 45:
        print(ERROR[1])
        n4 = int(input())
        while n4 == n1 or n4 == n2 or n4 == n3:
            print(ERROR[0])
            n4 = int(input())


    n5 = int(input())
    while n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
        print(ERROR[0])
        n5 = int(input())
    while n5 < 1 or n5 > 45:
        print(ERROR[1])
        n5 = int(input())
        while n5 == n1 or n5 == n2 or n5 == n3 or n5 == n4:
            print(ERROR[0])
            n5 = int(input())

    print('Type tzoker number (1-20)')
    n6 = int(input())
    while n6 < 1 or n6 > 20:
        print(ERROR[1])
        n6 = int(input())

    for i in [n1,n2,n3,n4,n5]:
        user_number_list.append(i)
    user_number_list.sort()
    user_number_list.append(n6)
    usertzoker = user_number_list[5]


def NumCheck():
    NOSN = 0
    for i in user_number_list:
        if i in random_number_list:
            NOSN += 1
    return NOSN



stats = {
'1p1':0,
'2p1':0,
'3p0':0,
'3p1':0,
'4p0':0,
'4p1':0,
'5p0':0,
'5p1':0
}


# start of program

AskUser()
print('How many times will you try?')
x = int(input())
for i in range(0,x):
    RandGen()
    usertzoker = user_number_list[5]
    randtzoker = random_number_list[5]
    random_number_list.pop(5)

    if NumCheck() == 5 and usertzoker == randtzoker:
        stats['5p1'] += 1

    elif NumCheck() == 5:
        stats['5p0'] += 1

    elif NumCheck() == 4 and usertzoker == randtzoker:
        stats['4p1'] += 1

    elif NumCheck() == 4:
        stats['4p0'] += 1

    elif NumCheck() == 3 and usertzoker == randtzoker:
        stats['3p1'] += 1

    elif NumCheck() == 3:
        stats['3p0'] += 1

    elif usertzoker == randtzoker and NumCheck() == 2:
        stats['2p1'] += 1

    elif NumCheck() == 1 and usertzoker == randtzoker:
        stats['1p1'] += 1

print(stats)
