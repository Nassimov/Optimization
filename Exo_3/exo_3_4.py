import cvxpy as cp
from math import ceil
recipe_A = cp.Variable()
recipe_B = cp.Variable()
data = {
    "price": [8, 1],
    "calories": [90, 900],
    "time": [3, 50]
}

total_price = recipe_A * data['price'][0] + recipe_B * \
    data['price'][1]
total_calories = recipe_A * data['calories'][0] + recipe_B * \
    data['calories'][1]
total_time = recipe_A * data['time'][0] + recipe_B * \
    data['time'][1]

constraints = [recipe_A >= 0, recipe_B >= 0,
               total_calories >= 2000, total_time <= 100]
prob = cp.Problem(cp.Minimize(total_price), constraints)
prob.solve()

cost = prob.value
print(" - Status:", prob.status)
print("ammount of portions to prepare of A " + str(ceil(recipe_A.value)))
print("ammount of portions to prepare of B " + str(ceil(recipe_B.value)))
"""
Results:::
 - Status: optimal
ammount of portions to prepare of A 6
ammount of portions to prepare of B 2

"""
