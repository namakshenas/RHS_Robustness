import numpy as np
from gurobipy import Model, GRB

# PARAMETERs (only here should be changed)
p_fix_cost = [120, 150, 135]
p_demand = [180, 170, 250, 200, 190]
p_transport_cost = [[10, 20, 15, 16, 17],
                    [5, 17, 18, 15, 15],
                    [13, 15, 18, 15, 16]]

# CONSTANTs
N_LOC = len(p_fix_cost)
N_MARKET = len(p_demand)

# SETs
s_loc = range(N_LOC)
s_market = range(N_MARKET)

# INSTANTIATE THE MODEL
model = Model()

# VARIABLEs
v_locate = model.addVars(N_LOC, vtype=GRB.BINARY)
v_transport = model.addVars(N_LOC, N_MARKET)

# ASSERT DIMENSIONAL CONSISTENCY
assert len(p_transport_cost) == N_LOC
assert len(p_transport_cost[0]) == N_MARKET

# OBJECTIVE
model.setObjective(
    sum(
        p_fix_cost[i]*v_locate[i]
        for i in s_loc
    )
    +
    sum(
        p_transport_cost[i][j]*v_transport[i][j]
        for i in s_loc for j in s_market
    ),
    sense=GRB.MINIMIZE
)

# CONSTRAINTs
for i in s_loc:
    model.addConstr(
        sum(
            v_transport[i][j]
            for j in s_market
        )
        <=
        v_locate[i]
    )

for j in s_market:
    model.addConstr(
        sum(
            v_transport[i][j]
            for i in s_loc
        )
        >=
        p_demand[j]
    )

# RUN!
model.optimize()





