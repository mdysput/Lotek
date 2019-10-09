import random
import time

myNumbers = []
compNumbers = []
playing = True

while playing:
    for i in range(6):
        myNumbers.append(int(input("Enter " + str(i + 1) + " number: ")))
        compNumbers.append(random.randint(1, 40))
    trafione = 0
    for z in myNumbers:
        for y in compNumbers:
            if z == y:
                trafione += 1
    print("You got "+str(trafione))
    print("Numbers were: ")
    for w in compNumbers:
        print(w)
    time.sleep(2)
    myNumbers.clear()
    compNumbers.clear()
    doYouWantToPlay = input("Do you want to play again (if not press 'n', or 'no')?")
    if doYouWantToPlay == 'n' or doYouWantToPlay == 'no':
        print("byebye")
        playing = False
    else:
        print("So start again")
        time.sleep(1)

