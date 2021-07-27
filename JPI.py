'''
This is an improved, new version of the tzoker project.
It has (imo) cleaner code, and uses the pyinputplus module for proper inpu validation.
There are probably improvements that can be made but I will take care of that the next time I am bored :P

--TODO--
-Add more statistics stuff (Amount of money lost and won, how long it would take for the actual Tzoker to run all these draws, and more random stuff
-Add comments explaining what the hell the code is doing, for my future self :p
-Thats all for now
'''



import random
import pyinputplus as pyip
import time


def FindDuplicates(List):
    if len(List) != len(set(List)):
        print("This number already exists!")
        return True


def getRandomNumbers():
    RandomNumbers = random.sample(range(1, 46), 5)  # Makes a list with 5 numbers between 1 and 45
    RandomNumbers.sort()  # Then sorts the list
    RandomNumbers.append(random.randint(1, 21))  # and adds a number between 1 and 20 at the end
    return RandomNumbers


def getUserNumbers():
    print("Enter 5 numbers between 1 and 45")
    n1 = pyip.inputInt(min=1, max=45)
    n2 = pyip.inputInt(min=1, max=45)
    while FindDuplicates([n1, n2]):
        n2 = pyip.inputInt(min=1, max=45)
    n3 = pyip.inputInt(min=1, max=45)
    while FindDuplicates([n1, n2, n3]):
        n3 = pyip.inputInt(min=1, max=45)
    n4 = pyip.inputInt(min=1, max=45)
    while FindDuplicates([n1, n2, n3, n4]):
        n4 = pyip.inputInt(min=1, max=45)
    n5 = pyip.inputInt(min=1, max=45)
    while FindDuplicates([n1, n2, n3, n4, n5]):
        n5 = pyip.inputInt(min=1, max=45)
    print("Enter Tzoker number")
    n6 = pyip.inputInt(min=1, max=20)
    List = [n1, n2, n3, n4, n5]
    List.sort
    List.append(n6)
    return List


def NumCheck(RandomNumbers, UserNumbers):
    NumberOfSameValues = 0
    for i in UserNumbers:
        if i in RandomNumbers:
            NumberOfSameValues += 1
    return NumberOfSameValues


"""START"""
NormalNumberList = getUserNumbers()
Tzoker = NormalNumberList[5]
NormalNumberList.pop(5)

stats = {"1p1": 0, "2p1": 0, "3p0": 0, "3p1": 0, "4p0": 0, "4p1": 0, "5p0": 0, "5p1": 0}

print("How many times will you try?")
AmountOfAttempts = pyip.inputInt(min=1)
start = time.time()
for i in range(1, AmountOfAttempts + 1):
    RandomNumberList = getRandomNumbers()
    RandTzoker = RandomNumberList[5]
    RandomNumberList.pop(5)

    if NumCheck(RandomNumberList, NormalNumberList) == 5 and Tzoker == RandTzoker:
        stats["5p1"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 5:
        stats["5p0"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 4 and Tzoker == RandTzoker:
        stats["4p1"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 4:
        stats["4p0"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 3 and Tzoker == RandTzoker:
        stats["3p1"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 3:
        stats["3p0"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 2 and Tzoker == RandTzoker:
        stats["2p1"] += 1

    elif NumCheck(RandomNumberList, NormalNumberList) == 1 and Tzoker == RandTzoker:
        stats["1p1"] += 1

print(stats)
print("Elapsed time:",time.time() - start,"seconds")
