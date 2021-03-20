import cvxpy as cp

"""
1) MIN x1;x2;x3R => _x1 ** 3 + (_x2 - _x3) ** 2 + _x3 ** 3 + 2
this is a convexe problem but under constraints :
the Hessian matrix must be PSD  :
Df/Dx1 = 3*(x1**2)
Df/Dx2 = 2*(x2-x3)
Df/Dx3 = -2*x2 + 2*x3 + 2*x3**2

let H Hessian  :


H= [
    [6*x1, 0, 0],
    [0, 2, -2],
    [0, -2, 2+(4*x3)]
 ]

 Constraint :
 1=> 6x1 + 2 + 2 + 4x3 > 0 ==> 6x1+4+4x3 > 0  // Tr(H)>0
 2=>  (3x1 * 4x3) >=0   Det(H )>=0
"""


_x1 = cp.Variable()
_x2 = cp.Variable()
_x3 = cp.Variable()
f = _x1 ** 3 + (_x2 - _x3) ** 2 + _x3 ** 3 + 2
_constraints = [6*_x1+4*_x3 >= -5, 3*_x1 >= 0,
                8*_x3 >= 0]  # When i just add (3*x1 * 4*x3) >=0 that gives me and error
print(' The problem is Convex ander the following conditions :=> {}'.format(_constraints))
obj = cp.Minimize(f)
prob = cp.Problem(obj, _constraints)
prob.solve()
print(" Status:", prob.status)
value = prob.value
print("optimal value", round(value))
print("optimal variable", _x1.value, "and", _x2.value, "and", _x3.value)

"""
==> RESULTS
Status: optimal
optimal value 2.0
optimal variable 0.0002163889562683633 and 0.00036787086508168935 and 0.0003678708493824588
"""
