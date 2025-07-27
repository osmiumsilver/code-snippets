from random import randint
from collections import Counter

def roll_dice(*dice, num_of_trials=1000000):
    counts = Counter()
    for _ in range(num_of_trials):
        counts[sum(randint(1, sides)for sides in dice )] += 1
    print ('')
    for outcome in range(len(dice),sum(dice)+1):
        print (f"{outcome}\t {counts[outcome]*100/ num_of_trials :0.2f}%")

roll_dice(4,6)