from pathlib import Path
import numpy as np
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

T0, T_env, tau_h, dt_h = 40.0, 25.0, 1.5, 0.1
thoi_gian_h = np.arange(0.0, 10.0 + dt_h / 2, dt_h)
T_euler = np.empty_like(thoi_gian_h)
T_euler[0] = T0
for k in range(len(thoi_gian_h) - 1):
    T_euler[k+1] = T_euler[k] - dt_h * (T_euler[k]-T_env)/tau_h
T_exact = T_env + (T0 - T_env)*np.exp(-thoi_gian_h/tau_h)
sai_lech_c = float(np.max(np.abs(T_euler - T_exact)))
assert np.all(T_euler >= T_env) and np.all(np.diff(T_euler) <= 1e-12)
fig, ax = plt.subplots(figsize=(7,3.7))
ax.plot(thoi_gian_h,T_exact,label="Nghiệm giải tích")
ax.plot(thoi_gian_h,T_euler,"--",label="Euler")
ax.set(xlabel="Thời gian (h)",ylabel="Nhiệt độ (°C)")
ax.legend()
root = Path(__file__).resolve().parent.parent
out = root / "output" / "bai17_mo_phong.png"
out.parent.mkdir(exist_ok=True)
fig.savefig(out,dpi=140,bbox_inches="tight")
plt.close(fig)
print(f"Sai lech lon nhat = {sai_lech_c:.4f} °C")
