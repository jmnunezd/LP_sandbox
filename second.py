# https://realpython.com/linear-programming-python/
from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMinimize

# Create the model
model = LpProblem(name="personell_scheduler", sense=LpMinimize)

# Initialize the decision variables
x2 = LpVariable(name="x2", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x1 = LpVariable(name="x1", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x3 = LpVariable(name="x3", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x4 = LpVariable(name="x4", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x5 = LpVariable(name="x5", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x6 = LpVariable(name="x6", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem
x7 = LpVariable(name="x7", lowBound=0, cat='Integer')  # cat Integer is optional but useful for this problem

# Add the objective function to the model
model += lpSum([x1, x2, x3, x4, x5, x6, x7])

# Add the constraints to the model
model += (x1 + x4 + x5 + x6 + x7 >= 110, "tue-wed free")
model += (x1 + x2 + x5 + x6 + x7 >= 80, "wed-th free")
model += (x1 + x2 + x3 + x6 + x7 >= 150, "th-fri free")
model += (x1 + x2 + x3 + x4 + x7 >= 30, "fri-sat free")
model += (x1 + x2 + x3 + x4 + x5 >= 70, "sat-sun free")
model += (x2 + x3 + x4 + x5 + x6 >= 160, "sun-mon free")
model += (x3 + x4 + x5 + x6 + x7 >= 120, "mon-tue free")


# solving:
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