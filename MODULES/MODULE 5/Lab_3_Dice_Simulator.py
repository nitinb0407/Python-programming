# MODULE 5 - LAB EXERCISE 3
# Dice simulator using the random module.

import random

rolls = int(input("How many times should the dice be rolled? "))
for roll in range(1, rolls + 1):
    print(f"Roll {roll}: {random.randint(1, 6)}")

# SAMPLE INPUT
# How many times should the dice be rolled? 3
# SAMPLE OUTPUT (random; your results may differ)
# Roll 1: 4
# Roll 2: 1
# Roll 3: 6
