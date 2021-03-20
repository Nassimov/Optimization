
import cvxpy as cp
_x1 = cp.Variable()
_x2 = cp.Variable()
obj = cp.Minimize((_x1 - 4)**2 + 7*(_x2-4)**2 + 4*_x2)
prob = cp.Problem(obj)
prob.solve()
value = prob.value
print("opt val", round(value))
print("optimal var", _x1.value, _x2.value)

"""
stat optimal
The Optimal value is =>  15.0
The optimal variable is =>  4.0 3.7142857142857144
"""
