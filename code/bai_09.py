import csv
import json
from pathlib import Path

root = Path(__file__).resolve().parent.parent
nguon = root / "data" / "nhiet_do_mau.csv"
dich = root / "output" / "tom_tat_bai09.json"
dich.parent.mkdir(parents=True, exist_ok=True)
hop_le, loi = [], 0
with nguon.open("r", encoding="utf-8", newline="") as f:
    for dong in csv.DictReader(f):
        try:
            t = float(dong["temp_c"])
        except (ValueError, KeyError, TypeError):
            loi += 1
            continue
        hop_le.append(t)
tom_tat = {"so_hop_le": len(hop_le), "so_loi": loi}
with dich.open("w", encoding="utf-8") as f:
    json.dump(tom_tat, f, ensure_ascii=False, indent=2)
print(tom_tat)
