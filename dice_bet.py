import random

import pandas as pd

# Load the CSV file into a pandas DataFrame
df = pd.read_csv("dices.csv")

# Prompt the user for their bet
bet = int(input("Enter your bet: "))

num_rolls = 0
found = False

while not found:
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    b = dice1 + dice2 + dice3
    num_rolls += 1

    if b == bet:
        found = True
        probability = df.loc[df["Sum"] == b, "Prob."].values.item()
        print(f"Sum: {b}, Probability: {probability:.1%}")
        print(f"Number of rolls: {num_rolls}")
