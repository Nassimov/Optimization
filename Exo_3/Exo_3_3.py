import cvxpy as cp
_ruralx = cp.Variable()
_urbanx = cp.Variable()
_ruralb = 7000*cp.log(1+_ruralx)
_urbanb = 5000*cp.log(1+_urbanx)
_optfunction = _ruralb + _urbanb - _ruralx - _urbanx
constraints = [_ruralx + _urbanx == 200, _ruralx >= 0, _urbanx >= 0]
obj = cp.Maximize(_optfunction)
prob = cp.Problem(obj, constraints)
prob.solve()
cost = prob.value
print(" - Status:", prob.status)
print("Cost optimal value =>  {}".format(round(cost)))
print("[Benefit] :")
print("Rural benefit cost is => {} ".format(round(_ruralb.value * 1)))
print("Urban benefit cost is => {} ".format(round(_urbanb.value*1)))
print("[Costs]")
print("Rural cost is => {}".format(round(_ruralx.value * 1)))
print("Urban cost is => {}".format(round(_urbanx.value*1)))
"""
Results :::: 
 - Status: optimal
Cost optimal value =>  55349.0
[Benefit] :
Rural benefit cost is => 33385.0
Urban benefit cost is => 22164.0
[Costs]
Rural cost is => 117.0
Urban cost is => 83.0
"""
