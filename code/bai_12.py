from pathlib import Path
import pandas as pd

root = Path(__file__).resolve().parent.parent
df = pd.read_csv(root / "data" / "nhiet_do_mau.csv")
so_goc = len(df)
df["timestamp"] = pd.to_datetime(df["timestamp"], errors="coerce")
df["temp_c"] = pd.to_numeric(df["temp_c"], errors="coerce")
df = df.dropna(subset=["timestamp", "temp_c"]).copy()
df = df[df["temp_c"].between(-40, 125)].copy()
df["hour"] = df["timestamp"].dt.floor("h")
nhom = df.groupby("hour")["temp_c"].mean()
print(f"Goc={so_goc}, hop le={len(df)}, loai={so_goc-len(df)}")
print(nhom.round(2).to_string())
