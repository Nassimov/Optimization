import cvxpy as cp
_blend1 = cp.Variable()
_blend2 = cp.Variable()
_blend3 = cp.Variable()
_blend4 = cp.Variable()

_optfunction = 55*_blend1 + 65*_blend2 + 35*_blend3 + 85*_blend4
l1 = 30*_blend1 + 20*_blend2 + 40*_blend3 + 20*_blend4
l2 = 35*_blend1 + 60*_blend2 + 35*_blend3 + 40*_blend4
l3 = 20*_blend1 + 15*_blend2 + 5*_blend3 + 30*_blend4
l4 = 15*_blend1 + 5*_blend2 + 20*_blend3 + 10*_blend4

constraints = [5 <= _blend2, _blend2 <= 20,
               _blend3 >= 30, 10 <= _blend1,
               _blend1 <= 25,
               _blend4 >= 0,
               l1 <= 35*110,  # rose final %
               l2 <= 50*170,  # bergamot orange % content in the perfum must be <= 50%
               l3 >= 19*70,  # Lily of the valley % content has to be >= 19%
               l4 >= 8*50, l4 <= 25 * \
               50,  # Thymus content % =>  13% >=P>= 8%
               ]

obj = cp.Minimize(_optfunction)
prob = cp.Problem(obj, constraints)
prob.solve()
cost = prob.value/100
print("status:", prob.status)
print("Cost Optimal value is : {}".format(round(cost)))
print("Blend 1 : {}".format(round(_blend1.value * 1)))
print("Blend 2 : {}".format(round(_blend2.value * 1)))
print("Blend 3 : {}".format(round(_blend3.value * 1)))
print("Blend 4 : {}".format(round(_blend4.value*1)))
"""
Result ===> 
status: optimal
Cost Optimal value is : 45.0
Blend 1 : 25.0
Blend 2 : 5.0
Blend 3 : 30.0
Blend 4 : 20.0
"""
