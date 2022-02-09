from pulp import LpProblem, LpStatus, lpSum, LpVariable, LpMaximize

# Create the model
model = LpProblem(name="personell_scheduler", sense=LpMaximize)

# Initialize the decision variables
x1 = LpVariable(name="x1", lowBound=0)
x2 = LpVariable(name="x2", upBound=0)

# Add the objective function to the model
model += lpSum([2*x1, -x2])

# Add the constraints to the model
model += (8 * x1 - 4 * x2 <= 16, 'const 1')
model += (3* x1 - 4* x2 <= 12, "const 2")

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