import random
Best_Money= 0
best_Turn = 0
money = 15
turns = 0
while money > 0:

    if Best_Money < money:
        Best_Money = money
        best_Turn = turns

    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    print("The first dice is %d" % dice1)
    print("The second dice is %d" % dice2)
    total = dice1 + dice2
    print("the amount of dots is %d" % total)

    if total == 7:
        money += 4
        turns += 1
    else:
        money -= 1
        turns += 1
    print("the money you have left is %d" % money)
    print(" the total after each roll is %d" % total)
    print(turns)
print("it took you %s turns to run out of money." % turns)
print("On turn %s you had the most money %s" % (best_Turn, Best_Money))