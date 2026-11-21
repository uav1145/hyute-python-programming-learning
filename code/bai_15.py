import numpy as np

v_train = np.array([0.50, 0.75, 1.00, 1.25, 1.50])
t_train = np.array([0.2, 24.9, 50.1, 75.2, 99.8])
a, b = np.polyfit(v_train, t_train, deg=1)
v_test = np.array([0.625, 1.375])
t_test = np.array([12.3, 87.6])
du_doan = a * v_test + b
mae = float(np.mean(np.abs(du_doan - t_test)))
print(f"a={a:.2f} °C/V, b={b:.2f} °C")
print(f"MAE={mae:.3f} °C")
assert v_test.min() >= v_train.min() and v_test.max() <= v_train.max()
