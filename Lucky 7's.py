import random
dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
print(dice1)
print(dice2)
money = 15
total = dice1 + dice2
print(dice1 + dice2)

if total == 7:
    money += 4
else:
    money -= 1
print(money)
