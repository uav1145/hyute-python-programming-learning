from datetime import datetime

def tach_ban_ghi(dong: str):
    truong = [phan.strip() for phan in dong.split(",")]
    if len(truong) != 3:
        raise ValueError("Can dung 3 truong")
    thoi_diem = datetime.fromisoformat(truong[0])
    nhiet_do_c = float(truong[1])
    if truong[2] not in {"OK", "ALARM"}:
        raise ValueError("Trang thai khong hop le")
    return thoi_diem, nhiet_do_c, truong[2]

moc, nhiet_do, trang_thai = tach_ban_ghi(
    "2026-11-20T08:00:00,25.6,OK"
)
print(moc.isoformat(), f"{nhiet_do:.1f} °C", trang_thai)
