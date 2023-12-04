As a pseudocode a description of the problem.

Prompt the user to enter a number between 3 and 18
Read and store the user's input as soma_face

Set n2 to 216  // Three dice (6 x 6 x 6)
Set counter to 0
Set n1 to 0

Repeat while soma_face is equal to or greater than 3 and less than or equal to 18:
    Prompt the user to enter a valid sum of dice
    Read and store the user's input as soma_face

    Reset n1 to 0

    For each value x from 1 to 6:
        For each value y from 1 to 6:
            For each value z from 1 to 6:
                If the sum of x, y, and z is equal to soma_face:
                    Increment n1 by 1

                Increment the counter by 1

    Calculate the probability as (n1 / n2) * 100.0

    Print "A probabilidade de sair ", soma_face, "é de", probability, "%"
    Print "O loop 'for' foi executado", counter, "vezes até alcançar a soma desejada"

Technical Description:
The program prompts the user to enter a number between 3 and 18, representing the desired sum when rolling three dice simultaneously. The probability of obtaining that sum is calculated using the formula P = (n1 / n2) * 100.0, where n1 is the number of occurrences where the sum of the dice equals the user's input, and n2 is the total number of possible outcomes (216 in this case, as each die has 6 faces).

To calculate n1, nested for loops iterate over all possible combinations of the three dice values (ranging from 1 to 6). If the sum of the three dice matches the user's input, n1 is incremented. Additionally, a counter variable keeps track of the total number of iterations in the loops.

Finally, the probability is computed by dividing n1 by n2, multiplying by 100.0 for the percentage representation. The result is then printed along with a message indicating the desired sum and the number of iterations performed in the loops.
