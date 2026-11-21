def dien_nang_kwh(cong_suat_kw: float, gio: float) -> float:
    """Tinh dien nang kWh; P >= 0 kW, gio >= 0 h."""
    if cong_suat_kw < 0 or gio < 0:
        raise ValueError("Cong suat va thoi gian phai khong am")
    return cong_suat_kw * gio

ket_qua = dien_nang_kwh(1.5, 3.0)
assert abs(ket_qua - 4.5) < 1e-12
print(f"E = {ket_qua:.2f} kWh")
