"""Escreva um programa que solicite um numero entre 3 e 18 e calcule a propabilidade que esse numero tem de sair ao se jogar tres dados # noqa: E501
  ao mesmo tempo. A probabilidade e calculada por meio da seguinte formula:

  P = (n1 / n2) * 100.0

  em que n1 eh o numero no qual a soma dos dados eh igual ao numero de dado pelo usuario,
  e n2 eh o numero total de casos possiveis.
  Por exemplo, se o numero inserido for 6, o programa imprimira:

  "A probabilidade de sair 6 e de 4.63%" """

# flake8: noqa: E401, E501
n2 = 216  # Três dados (6 x 6 x 6)
soma_face = 0
counter = 0

while soma_face >= 3 or soma_face <= 18:
    soma_face = int(input("Digite a soma dos dados: "))

    n1 = 0

    for x in range(1, 7):
        for y in range(1, 7):
            for z in range(1, 7):
                if x + y + z == soma_face:
                    n1 += 1
                counter += 1

    prob = (n1 / n2) * 100.0

    print(f"\nA probabilidade de sair {soma_face} e de {prob:.2f}%")
    print(f"O loop 'for' foi executado {counter} vezes até alcançar a soma desejada.")
