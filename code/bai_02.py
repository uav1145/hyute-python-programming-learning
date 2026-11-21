dien_ap_v = 12.0
dong_dien_a = 5.0
thoi_gian_h = 2.0
cong_suat_w = dien_ap_v * dong_dien_a
dien_nang_wh = cong_suat_w * thoi_gian_h
dien_nang_kwh = dien_nang_wh / 1000
print(f"P = {cong_suat_w:.0f} W")
print(f"E = {dien_nang_wh:.0f} Wh = {dien_nang_kwh:.3f} kWh")
