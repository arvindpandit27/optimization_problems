from scipy.optimize import linprog
print("Example Problem - 1")

'''
Solve:
min (-20x - 30y)
such that, x + y <= 100;
           0.1x + 0.2y <= 14
'''


obj = [-20, -30]

lhs_ineq = [[1, 1], [0.1, 0.2]]
rhs_ineq = [100, 14]
bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="simplex")

print(f"Optimal values are {opt.x[0]} and {opt.x[1]}")