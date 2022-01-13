import numpy as np
import cvxpy as cp

data_dir = '../Data/Simple portfolio optimization/'
pbar = np.loadtxt(data_dir + 'pbar.txt', delimiter=',')
S = np.loadtxt(data_dir + 'S.txt', delimiter=',')


n = len(pbar)
uniform_w = np.ones(n)/n
uniform_ret = pbar.T @ uniform_w
print(uniform_ret)
print(np.std(pbar * uniform_w))
print("Risk of uniform portfolio", np.sqrt(uniform_w.T @ S @ uniform_w))

#### No additional constraint ####
w = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.quad_form(w, S)), [cp.sum(w) == 1,
             pbar.T @ w >= uniform_ret,
            ])
prob.solve()
print("\nThe optimal value is", prob.value)
print("The risk is ", np.sqrt(prob.value))
print("A solution x is")
print(w.value)

#### Long only ####
w = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.quad_form(w, S)), [cp.sum(w) == 1,
             pbar.T @ w >= uniform_ret,
            w>= 0])
prob.solve()
print("\nThe optimal value is", prob.value)
print("The risk is ", np.sqrt(prob.value))
print("A solution x is")
print(w.value)


#### Limit On short ####
w = cp.Variable(n)
prob = cp.Problem(cp.Minimize(cp.quad_form(w, S)), [cp.sum(w) == 1,
             pbar.T @ w >= uniform_ret,
            cp.sum(cp.neg(w)) <= 0.5])
prob.solve()
print("\nThe optimal value is", prob.value)
print("The risk is ", np.sqrt(prob.value))
print("A solution x is")
print(w.value)