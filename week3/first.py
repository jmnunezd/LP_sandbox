from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMaximize, LpMinimize

# ----- Create the model ----- #
model = LpProblem(name="factory_location", sense=LpMinimize)

# ----- decision variables ----- #
# Posible factory locations:

x = [LpVariable(name=f"x{i}", cat='Binary') for i in range(1, 6)]

# yij is the number of book shipped from distribution center j to i
y1j = [LpVariable(name=f"y{1}{j}", lowBound=0) for j in range(1, 6)]
y2j = [LpVariable(name=f"y{2}{j}", lowBound=0) for j in range(1, 6)]
y3j = [LpVariable(name=f"y{3}{j}", lowBound=0) for j in range(1, 6)]
y4j = [LpVariable(name=f"y{4}{j}", lowBound=0) for j in range(1, 6)]
y5j = [LpVariable(name=f"y{5}{j}", lowBound=0) for j in range(1, 6)]

y = [y1j, y2j, y3j, y4j, y5j]

# ----- parameters ----- #
# shipping cost per book from j to i
OP = [40_000, 30_000, 25_000, 40_000, 30_000]  # operation cost per facility

Kj = [20_000, 20_000, 15_000, 25_000, 15_000]  # capacity of each facility

Di = [8_000, 12_000, 9_000, 14_000, 17_000]    # demand for each region

# shiping cost
Cij = [[2.4, 3.25, 4.05, 5.25, 6.95],  # to nortwest
       [3.5, 2.3, 3.25, 6.05, 5.85],   # to southwest
       [4.8, 3.4, 2.85, 4.3, 4.8],     # to midwest
       [6.8, 5.25, 4.3, 3.25, 2.1],     # to southeast
       [5.75, 6, 4.75, 2.75, 3.5]      # to northeast
]

# ----- Objective functions ----- #
model += lpSum([op * xi for op, xi in zip(OP, x)]) \
        +lpSum([Cij[0][i] * y[0][i] for i in range(5)]) \
        +lpSum([Cij[1][i] * y[1][i] for i in range(5)]) \
        +lpSum([Cij[2][i] * y[2][i] for i in range(5)]) \
        +lpSum([Cij[3][i] * y[3][i] for i in range(5)]) \
        +lpSum([Cij[4][i] * y[4][i] for i in range(5)])
        

# ----- Constraints ----- #
# capacity
model += (lpSum([y1j[0], y2j[0], y3j[0], y4j[0], y5j[0]]) <= Kj[0] * x[0])
model += (lpSum([y1j[1], y2j[1], y3j[1], y4j[1], y5j[1]]) <= Kj[1] * x[1])
model += (lpSum([y1j[2], y2j[2], y3j[2], y4j[2], y5j[2]]) <= Kj[2] * x[2])
model += (lpSum([y1j[3], y2j[3], y3j[3], y4j[3], y5j[3]]) <= Kj[3] * x[3])
model += (lpSum([y1j[4], y2j[4], y3j[4], y4j[4], y5j[4]]) <= Kj[4] * x[4])

# demand
model += (lpSum(y1j) >= Di[0])
model += (lpSum(y2j) >= Di[1])
model += (lpSum(y3j) >= Di[2])
model += (lpSum(y4j) >= Di[3])
model += (lpSum(y5j) >= Di[4])

print(model)

model.solve()

# ----- Results ----- #
print(f"status: {model.status}, {LpStatus[model.status]}")
print(f"objective: {model.objective.value()}")

for var in model.variables():
    print(f"{var.name}: {var.value()}")

print('\n')

for name, constraint in model.constraints.items():
    print(f"{name}: {constraint.value()}")

print('\n')