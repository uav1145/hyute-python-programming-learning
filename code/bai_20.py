import csv
import json
from pathlib import Path

def doc_du_lieu(duong_dan):
    hop_le, so_loi = [], 0
    with duong_dan.open(encoding="utf-8", newline="") as f:
        for dong in csv.DictReader(f):
            try:
                t = float(dong["temp_c"])
            except (ValueError, KeyError, TypeError):
                so_loi += 1
                continue
            hop_le.append(t)
    return hop_le, so_loi

def thong_ke(mau, so_loi):
    if not mau:
        raise ValueError("Khong co du lieu hop le")
    return {"so_hop_le": len(mau), "so_loi": so_loi,
            "tb_c": round(sum(mau) / len(mau), 3),
            "so_vuot_30_c": sum(t > 30 for t in mau)}

root = Path(__file__).resolve().parent.parent
mau, so_loi = doc_du_lieu(root / "data" / "nhiet_do_mau.csv")
bao_cao = thong_ke(mau, so_loi)
assert bao_cao["so_hop_le"] == 7
out = root / "output" / "bao_cao_bai20.json"
out.parent.mkdir(exist_ok=True)
out.write_text(json.dumps(bao_cao, ensure_ascii=False, indent=2), encoding="utf-8")
print(bao_cao)
