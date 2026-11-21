"""Chạy kiểm tra nhanh toàn bộ 20 mã mẫu của khóa học.
Dùng: python kiem_tra_20_bai.py, sau khi pip install -r requirements.txt.
"""
from pathlib import Path
import subprocess,sys

ROOT=Path(__file__).resolve().parent
EXPECTED={1: 'Điện năng: 4.50 kWh', 2: 'P = 60 W', 3: 'CANH BAO', 4: 'TB = 27.875 °C', 5: 'E = 4.50 kWh', 6: '2026-11-20T08:00:00 25.6 °C OK', 7: 'Vi tri vuot: [1, 3]', 8: 'So cam bien: 2', 9: "{'so_hop_le': 7, 'so_loi': 1}", 10: 'S1 True', 11: 'K: [293.15, 298.15, 303.15]', 12: 'Goc=8, hop le=7, loai=1', 13: 'So diem: 7 | Da luu: bai13_do_thi.png', 14: 'q* = 20.000 (don vi quy uoc)', 15: 'a=99.80 °C/V, b=-49.76 °C', 16: 'E = 3.500 kWh', 17: 'Sai lech lon nhat = 0.1892 °C', 18: 'Luu: 2 | Loi: 1', 19: 'Dien lanh: n=7, Tmax=31.2 °C', 20: "{'so_hop_le': 7, 'so_loi': 1, 'tb_c': 27.743, 'so_vuot_30_c': 1}"}
failed=[]
for n in range(1,21):
    f=ROOT / "code" / f"bai_{n:02d}.py"
    r=subprocess.run([sys.executable,str(f)],cwd=ROOT,capture_output=True,text=True,timeout=30)
    ok=r.returncode==0 and EXPECTED[n] in r.stdout
    print(f"Bài {n:02d}: {'PASS' if ok else 'FAIL'}")
    if not ok:failed.append((n,r.stderr[-200:],r.stdout[:200]))
if failed:
    print(failed);sys.exit(1)
print("20/20 chương trình chạy và khớp dữ liệu mẫu.")
