import numpy as np
import cvxpy as cp

data_dir = '../Data/Heuristic suboptimal solution for Boolean LP/'

A = np.loadtxt(data_dir + 'A.txt', delimiter=',')
b = np.loadtxt(data_dir + 'b.txt', delimiter=',')
c = np.loadtxt(data_dir + 'c.txt', delimiter=',')

print(A.shape, b.shape, c.shape)
x = cp.Variable(len(c))

prob = cp.Problem(cp.Minimize(c.T @ x),
                  [A @ x <= b, 0 <= x, x <= 1])
prob.solve()
# Print result.
L = prob.value
print("\nThe optimal value is", L)
print("A solution x is")
print(x.value)

object_val_ls = []
for t in np.linspace(0, 1, 100):
    x_hat = np.array([1 if x_i >= t else 0 for x_i in x.value]).reshape(x.shape)

    if (A @ x_hat <= b).all():
        object_val_ls.append(c.T @ x_hat)
U = min(object_val_ls)
print('U is', U)

print('U-L=', U - L)
