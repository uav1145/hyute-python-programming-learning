import numpy as np

t_h = np.array([0.0, 1.0, 2.0])
p_kw = np.array([1.0, 2.0, 2.0])
dien_nang_kwh = float(np.trapezoid(p_kw, t_h))
t_c, moi_truong_c, tau_h = 30.0, 20.0, 2.0
dt_h = 0.5
for _ in range(4):
    toc_do_c_moi_h = -(t_c - moi_truong_c) / tau_h
    t_c += dt_h * toc_do_c_moi_h
print(f"E = {dien_nang_kwh:.3f} kWh")
print(f"T(2 h) Euler = {t_c:.3f} °C")
