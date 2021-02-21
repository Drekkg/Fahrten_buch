import random

kilometer = int(input("Kilometer stand: "))
# kilometer_driven_daily = random.randint(20, 45)
day = 1
while True:
    kilometer_driven_daily = random.randint(52, 89)  # random number of average driven kilometers
    kilometer = kilometer + kilometer_driven_daily
    day += 1
    print("Neue Kilometer Stand ist {}:  Kilometer gefahren {}".format(kilometer, kilometer_driven_daily))
    print(day)
    input()
