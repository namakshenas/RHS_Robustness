import numpy as np
from gurobipy import Model, GRB

# CONSTANTS
N_LOC = 3
N_MARKET = 5

# SETS
s_loc = range(N_LOC)
s_market = range(N_MARKET)