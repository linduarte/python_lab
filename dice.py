import random

import pandas as pd

eventos = 1  # playing x times

# Carregar o csv via pandas
df = pd.read_csv("dices.csv")  # type: ignore

for i in range(eventos):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    dice3 = random.randint(1, 6)
    b = dice1 + dice2 + dice3

    # Encontrar o valor correspondente 'Prob' para o valor sum 'b'
    probability = df.loc[df["Sum"] == b, "Prob."].values.item()  # type: ignore

    print(f"Sum: {b}, Probability: {probability:.1%}")
