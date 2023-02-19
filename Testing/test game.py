import random


for i in range(20):

    # The line below will roll a random number 0-4.
    # If we roll a '0' then print that we encountered a dragon.
    if random.randrange(5) == 0:
        print("DRAGON!!!")
    else:
        print("No dragon.")