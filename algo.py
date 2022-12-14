import random
import time

def generateRand():
    while True:
        # generate a random number from 1 to 1000
        rand_num = random.randint(1, 1000)

        # print the random number
        return rand_num

        # wait for one second
        time.sleep(1)
