from cs50 import get_float

dollars = get_float("Dollars: ")
coins = 0


while(dollars <= 0):
    dollars = get_float("Dollars: ")
    print(dollars)
    break

# change dollars to cents
changeOwed = dollars * 100
# changeOwed = round(dollars * 100)
if (changeOwed <=1):
    print("1st print ", changeOwed)
# else(changeOwed = round(dollars * 100))

while (changeOwed > 25):
    dollars = dollars % 25
    coins += 1
    changeOwed = changeOwed - 25
    # print(changeOwed)
    print("25 ", coins)
while (changeOwed > 10):
    dollars = dollars % 10
    coins += 1
    changeOwed = changeOwed - 10
    print(changeOwed)
    print("10 ", coins)
while (changeOwed > 5):
    dollars = dollars % 5
    coins += 1
    changeOwed = changeOwed - 5
    print(changeOwed)
    print("5 ", coins)
while (changeOwed > 1):
    dollars = dollars % 1
    coins += 1
    changeOwed = changeOwed - 1
    print(changeOwed)
    print("1 ", coins)
    print()
    break