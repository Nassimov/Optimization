import cvxpy as cp

recipe_A = cp.Variable()
recipe_B = cp.Variable()
recipe_C = cp.Variable()
data = {
    "price" : [2,2,6],
    "calories" : [800,1600,300],
    "time" : [25, 100, 5]
}

total_price = recipe_A * data['price'][0] + recipe_B * data['price'][1] + recipe_C * data['price'][2]
total_calories = recipe_A * data['calories'][0] + recipe_B * data['calories'][1] + recipe_C * data['calories'][2]           
total_time = recipe_A * data['time'][0] + recipe_B * data['time'][1] + recipe_C * data['time'][2]            

constraints = [ total_calories >= 2000, total_time <= 100 ]
prob = cp.Problem( cp.Minimize(total_price), constraints)
prob.solve()

cost = prob.value
print(" - Status:", prob.status)
print("ammount of portions to prepare of A" + str(recipe_A.value))
print("ammount of portions to prepare of B" + str(recipe_B.value))
print("ammount of portions to prepare of C" + str(recipe_C.value))