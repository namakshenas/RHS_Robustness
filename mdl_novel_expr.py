import numpy as np
from gurobipy import Model, GRB
import pandas as pd
import plotly.express as px

# PARAMETERs (only here should be changed)
p_fix_cost = [120, 150, 135]
p_demand = [50, 20, 40, 70, 10]
p_transport_cost = [[10, 20, 15, 16, 17],
                    [5, 17, 18, 15, 15],
                    [13, 15, 18, 15, 16]]

# CONSTANTs
N_LOC = len(p_fix_cost)
N_MARKET = len(p_demand)
N_BIGM = 100000

# SETs
s_loc = range(N_LOC)
s_market = range(N_MARKET)

# PARAMETERs SUPPORT
p_demand_lower = [p_demand[j] * 0.8 for j in s_market]
p_demand_upper = [p_demand[j] * 1.2 for j in s_market]

# LOG
N_ITER = 50
log_obj = np.zeros(N_ITER)
p_gamma = np.linspace(0, N_MARKET, N_ITER)

for iteration in range(N_ITER):
    # INSTANTIATE THE MODEL
    model = Model()

    # VARIABLEs
    v_locate = model.addVars(s_loc, vtype=GRB.BINARY)
    v_transport = model.addVars(s_loc, s_market)
    v_max_lower = model.addVars(s_market)
    v_max_upper = model.addVars(s_market)

    # ASSERT DIMENSIONAL CONSISTENCY
    assert len(p_transport_cost) == N_LOC
    assert len(p_transport_cost[0]) == N_MARKET

    # OBJECTIVE
    model.setObjective(
        sum(
            p_fix_cost[i] * v_locate[i]
            for i in s_loc
        )
        +
        sum(
            p_transport_cost[i][j] * v_transport[i, j]
            for i in s_loc
            for j in s_market
        ),
        sense=GRB.MINIMIZE
    )

    # CONSTRAINTs
    for i in s_loc:
        model.addConstr(
            sum(
                v_transport[i, j]
                for j in s_market
            )
            <=
            N_BIGM * v_locate[i]
        )

    for j in s_market:
        model.addConstr(
            sum(
                v_transport[i, j]
                for i in s_loc
            )
            >=
            p_demand[j]
        )

    # CONSTRAINTs ROBUST
    model.addConstr(
        sum(
            (
                    v_max_upper[j]
                    +
                    v_max_lower[j]
            )
            for j in s_market
        )
        <= (sum(p_demand[j] for j in s_market) * (N_MARKET - p_gamma[iteration])) / N_MARKET ** 2
    )

    for j in s_market:
        model.addConstr(
            p_demand_lower[j]
            -
            sum(
                v_transport[i, j]
                for i in s_loc
            )
            <=
            v_max_lower[j]
        )

    for j in s_market:
        model.addConstr(
            p_demand_upper[j]
            -
            sum(
                v_transport[i, j]
                for i in s_loc
            )
            <=
            v_max_upper[j]
        )

    # RUN!
    model.optimize()

    # DISPLAY
    if model.status == GRB.OPTIMAL:
        value_v_locate = np.array(
            [
                v_locate[i].X
                for i in s_loc
            ],
            dtype=int
        )
        value_v_transport = np.array(
            [
                v_transport[i, j].X
                for i in s_loc
                for j in s_market
            ],
            dtype=int
        )
        obj = np.round(model.objVal, 2)
        log_obj[iteration] = obj

# PLOT
df = pd.DataFrame(
    {'gamma': p_gamma,
     'obj_val': log_obj
     }
)
fig = px.line(df, x="gamma", y="obj_val")

fig.update_layout(
    legend_title=None,
    margin=dict(
        l=40,
        r=40,
        b=40,
        t=40
    ),
    yaxis={
        # 'title': None,
        'linecolor': "#D3D3D3",
        # 'showgrid': False,
        'gridcolor': 'LightPink'
    },
    xaxis={
        # 'title': None,
        'linecolor': "#D3D3D3",
        # 'showgrid': False,
        'gridcolor': 'LightPink'
    },
    plot_bgcolor='rgba(0,0,0,0)',
    paper_bgcolor='rgba(0,0,0,0)',
    hoverlabel=dict(
        bgcolor='rgba(0,0,0,.9)',
        font_size=16,
    )
)

fig.show()
