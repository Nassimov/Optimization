"""
In this exercice we use the algorithm described in the cours
"""
import sys
import cvxpy as cp
_eps = sys.float_info.epsilon
_x1 = cp.Variable()
_x2 = cp.Variable()
_m = 2
_u = 1.2
fi = -cp.log(_x1+_x2-4)
_t = 2
for i in range(10000):
    func = (_x1-2)**2 + 3*_x2 + (1/_t)*fi
    if((_m/_t) < _eps):
        break
    _t = _u*_t
print('t is equal to => {}:'.format(_t))
print('The problem is convex')
obj = cp.Minimize(func)
prob = cp.Problem(obj)
prob.solve()
print("status:", prob.status)
value = prob.value
print("optimal value", (value))
print("optimal variable", _x1.value, "and", _x2.value)
"""
The value of the Hyperparameter is equal to => 9876696341657764.0:
The problem is convex
status: optimal
optimal value 3.7500000488933236
optimal variable 3.5000041092948457 and 0.49999587108895677
"""
