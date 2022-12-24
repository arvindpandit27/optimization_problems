from scipy.optimize import linprog
print("Exercise Problem - 2")

'''
Solve:
min (-15x1 -17x2)
such that, x1 - x2 <= 8;
           x2 - x1 <= 6;
           x1 + x2 <= 40
'''


obj = [-15, -17]

lhs_ineq = [[1, -1], [-1, 1], [1, 1]]
rhs_ineq = [8, 6, 40]
bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="simplex")

print(f"Optimal values are {opt.x[0]} and {opt.x[1]}!")
print(15*opt.x[0] + 17*opt.x[1])