import csv
from datetime import datetime
from pathlib import Path

raw = [
    "2026-11-20T08:00:00,25.2,1.1",
    "2026-11-20T08:01:00,25.5,1.2",
    "2026-11-20T08:02:00,LOI,1.3",
]
hop_le, so_loi = [], 0
for dong in raw:
    truong = dong.split(",")
    try:
        if len(truong) != 3:
            raise ValueError("Khac 3 truong")
        datetime.fromisoformat(truong[0])
        t_c, i_a = float(truong[1]), float(truong[2])
    except ValueError:
        so_loi += 1
        continue
    hop_le.append({"timestamp": truong[0], "temp_c": t_c, "current_a": i_a})
root = Path(__file__).resolve().parent.parent
out = root / "output" / "nhat_ky_bai18.csv"
out.parent.mkdir(exist_ok=True)
with out.open("w", encoding="utf-8", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=["timestamp","temp_c","current_a"])
    writer.writeheader()
    writer.writerows(hop_le)
print("Luu:", len(hop_le), "| Loi:", so_loi)
