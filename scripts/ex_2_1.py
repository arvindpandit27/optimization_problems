from scipy.optimize import linprog
print("Exercise Problem - 2")

'''
Solve:
min (x1 -2x2)
such that, -x1 - x2 <= -2;
           x1 - x2 <= -1;
           x2 <= 3
'''


obj = [1, -2]

lhs_ineq = [[-1, -1], [1, -1], [0, 1]]
rhs_ineq = [-2, -1, 3]
bnd = [(0, float("inf")), (0, float("inf"))]

opt = linprog(c=obj, A_ub=lhs_ineq, b_ub=rhs_ineq, bounds=bnd, method="simplex")

print(f"Optimal values are {opt.x[0]} and {opt.x[1]}!")