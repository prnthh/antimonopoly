from random import randint
import time
import datetime

print('How many players?')
y = input('>')
player = [None] * y

turn = 0
while True:
    print("Random number: ", randint(1,6), randint(1,6))
    print("Turn number:" , turn)
    print("Player:", (turn%y))
    turn+=1
    print(datetime.datetime.now())
    print("-------------------")
    z = raw_input('next turn>')
