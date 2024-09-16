from ortools.sat.python import cp_model

model = cp_model.CpModel()
solver = cp_model.CpSolver()

# Goal: no adjacent antenna share a frequency
# Define possible frequencies: 0: f1, 1: f2, 2: f3
frequencies = {0 : 'f1', 1: 'f2', 2: 'f3'}

# Define the variables for each antenna
ant1 = model.NewIntVar(0, 2, 'ant1')
ant2 = model.NewIntVar(0, 2, 'ant2')
ant3 = model.NewIntVar(0, 2, 'ant3')
ant4 = model.NewIntVar(0, 2, 'ant4')
ant5 = model.NewIntVar(0, 2, 'ant5')
ant6 = model.NewIntVar(0, 2, 'ant6')
ant7 = model.NewIntVar(0, 2, 'ant7')
ant8 = model.NewIntVar(0, 2, 'ant8')
ant9 = model.NewIntVar(0, 2, 'ant9')

# Add adjacency antennas share same frequencies
model.Add(ant1 != ant2)
model.Add(ant1 != ant3)
model.Add(ant1 != ant4)

model.Add(ant2 != ant1)
model.Add(ant2 != ant3)
model.Add(ant2 != ant5)
model.Add(ant2 != ant6)

model.Add(ant3 != ant1)
model.Add(ant3 != ant2)
model.Add(ant3 != ant6)
model.Add(ant3 != ant9)

model.Add(ant4 != ant1)
model.Add(ant4 != ant5)

model.Add(ant5 != ant2)
model.Add(ant5 != ant4)

model.Add(ant6 != ant2)
model.Add(ant6 != ant3)
model.Add(ant6 != ant7)
model.Add(ant6 != ant8)

model.Add(ant7 != ant6)
model.Add(ant7 != ant8)

model.Add(ant8 != ant7)
model.Add(ant8 != ant6)
model.Add(ant8 != ant9)

model.Add(ant9 != ant3)
model.Add(ant9 != ant8)

status = solver.Solve(model)

if status == cp_model.OPTIMAL or status == cp_model.FEASIBLE:
    print("antenna 1: frequency %s" % frequencies[solver.Value(ant1)])
    print("antenna 2: frequency %s" % frequencies[solver.Value(ant2)])
    print("antenna 3: frequency %s" % frequencies[solver.Value(ant3)])
    print("antenna 4: frequency %s" % frequencies[solver.Value(ant4)])
    print("antenna 5: frequency %s" % frequencies[solver.Value(ant5)])
    print("antenna 6: frequency %s" % frequencies[solver.Value(ant6)])
    print("antenna 7: frequency %s" % frequencies[solver.Value(ant7)])
    print("antenna 8: frequency %s" % frequencies[solver.Value(ant8)])
    print("antenna 9: frequency %s" % frequencies[solver.Value(ant9)])
else:
    print("No solution found.")

'''
    result:
        antenna 1: frequency f2
        antenna 2: frequency f3
        antenna 3: frequency f1
        antenna 4: frequency f1
        antenna 5: frequency f2
        antenna 6: frequency f2
        antenna 7: frequency f3
        antenna 8: frequency f1
        antenna 9: frequency f2

'''
