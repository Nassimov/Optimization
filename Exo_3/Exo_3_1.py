import cvxpy as cp
_reservoirquatity = cp.Variable()
_streamquatity = cp.Variable()

func = 100*_reservoirquatity + 50*_streamquatity  # Loss function

constraints = [_reservoirquatity + _streamquatity == 500, _streamquatity <=
               100, 50*_reservoirquatity + 250*_streamquatity <= 100*(50+250)]
obj = cp.Minimize(func)
prob = cp.Problem(obj, constraints)
prob.solve()
print("status:", prob.status)
print("Quantity from Reservoir : {}".format(round(
    _reservoirquatity.value * 1000)))
print("Quantity from Stream : {}".format(round(_streamquatity.value*1000)))
print("Total Quantity(L) : {}".format(round(
    (_reservoirquatity.value+_streamquatity.value)*1000)))
print("PPM Quantity :  {} ".format(round(
    (50/300)*_reservoirquatity.value+(250/300)*_streamquatity.value)))
"""
Results 
status: optimal
Quantity from Reservoir : 475000.0
Quantity from Stream : 25000.0
Total Quantity(L) : 500000.0
PPM Quantity :  100.0
"""
