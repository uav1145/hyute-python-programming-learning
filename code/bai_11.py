import numpy as np

t_c = np.array([20.0, 25.0, 30.0])
t_k = t_c + 273.15
A = np.array([[2.0, 1.0], [1.0, -1.0]])
b = np.array([5.0, 1.0])
x = np.linalg.solve(A, b)
phan_du = np.linalg.norm(A @ x - b)
print("K:", np.round(t_k, 2).tolist())
print("x:", np.round(x, 3).tolist())
print(f"||Ax-b|| = {phan_du:.2e}")
