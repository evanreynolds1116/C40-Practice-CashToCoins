#  Convert the dollar amount into the coins that make up that dollar amount. The final result is an object with the correct number of quarters, dimes, nickels, and pennies.

dollarAmount = 8.69

piggyBank = {
    "pennies": 0,
    "nickels": 0,
    "dimes": 0,
    "quarters": 0
}

def coin_totals(cash):
    piggyBank['quarters'] += cash // 0.25
    cash = cash % 0.25
    piggyBank['dimes'] += cash // 0.10
    cash = cash % 0.10
    piggyBank['nickels'] += cash // 0.05
    cash = cash % 0.05
    piggyBank['pennies'] += cash // 0.01

    print(piggyBank)

coin_totals(8.69)