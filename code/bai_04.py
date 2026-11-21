nhiet_do_c = [24.1, 27.2, 31.0, 29.2]
nguong_c = 30.0
if not nhiet_do_c:
    raise ValueError("Danh sach rong")
tong = 0.0
so_mau_canh_bao = 0
for t in nhiet_do_c:
    tong += t
    if t > nguong_c:
        so_mau_canh_bao += 1
trung_binh = tong / len(nhiet_do_c)
print(f"TB = {trung_binh:.3f} °C")
print(f"Max = {max(nhiet_do_c):.1f} °C; vuot = {so_mau_canh_bao}")
