# https://realpython.com/linear-programming-python/
from pulp import LpMaximize, LpProblem, LpStatus, lpSum, LpVariable

# Create the model
model = LpProblem(name="desk_or_tables_to_produce", sense=LpMaximize)

# Initialize the decision variables
x1 = LpVariable(name="x1", lowBound=0, cat='Integer')
x2 = LpVariable(name="x2", lowBound=0, cat='Integer')

# Add the objective function to the model
model += lpSum([700 * x1, 900 * x2])

# Add the constraints to the model
model += (3 * x1 + 5 * x2 <= 3600, "wood constraint")
model += (x1 + 2 * x2 <= 1600, "labour constraint")
model += (50 * x1 + 20 * x2 <= 48000, "machine constraint")

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