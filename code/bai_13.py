from pathlib import Path
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "nhiet_do_mau.csv")
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["temp_c"] = pd.to_numeric(df["temp_c"], errors="coerce")
df = df.dropna(subset=["timestamp", "temp_c"]).sort_values("timestamp")
assert len(df) > 0, "Khong co du lieu hop le"
fig, ax = plt.subplots(figsize=(7, 3.6))
ax.plot(df["timestamp"], df["temp_c"], marker="o", label="Nhiệt độ")
ax.axhline(30, linestyle="--", label="Ngưỡng giả định: 30 °C")
ax.set(xlabel="Thời gian đo", ylabel="Nhiệt độ (°C)", title="Dữ liệu nhiệt độ mô phỏng")
ax.legend()
fig.autofmt_xdate()
dich = root / "output" / "bai13_do_thi.png"
dich.parent.mkdir(exist_ok=True)
fig.savefig(dich, dpi=140, bbox_inches="tight")
plt.close(fig)
print("So diem:", len(df), "| Da luu:", dich.name)
