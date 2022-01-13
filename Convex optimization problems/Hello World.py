import cvxpy as cp
import numpy as np

## Problem 1
m = 4
n = 2
x = cp.Variable(n)
c = np.array([1, 1])

A = np.array([[2, 1],
     [1, 3],
     [1, 0],
     [0, 1]])
b = np.array([1, 1, 0, 0])


prob = cp.Problem(cp.Minimize(c.T@x),
                  [A @ x >= b])
prob.solve()
# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)


P = np.array([[1, 0],
              [0, 9]])
prob = cp.Problem(cp.Minimize(cp.QuadForm(x, P)),
                  [A @ x >= b])
prob.solve()
# Print result.
print("\nThe optimal value is", prob.value)
print("A solution x is")
print(x.value)