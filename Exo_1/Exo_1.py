import cvxpy as cp
_x1 = cp.Variable()
constraints = [_x1 >= 0]
obj = cp.Minimize(2 * (_x1-1)**2)

prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("optimal value", prob.value)
print("optimal var", _x1.value)
