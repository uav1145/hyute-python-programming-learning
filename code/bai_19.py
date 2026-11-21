from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
lanh = pd.read_csv(root / "data" / "nhiet_do_mau.csv")
oto = pd.read_csv(root / "data" / "dien_ap_acquy.csv")
lanh["temp_c"] = pd.to_numeric(lanh["temp_c"], errors="coerce")
oto["voltage_v"] = pd.to_numeric(oto["voltage_v"], errors="coerce")
lanh = lanh.dropna(subset=["temp_c"])
oto = oto.dropna(subset=["voltage_v"])
print(f"Dien lanh: n={len(lanh)}, Tmax={lanh['temp_c'].max():.1f} °C")
print(f"O to: n={len(oto)}, Umin={oto['voltage_v'].min():.2f} V")
