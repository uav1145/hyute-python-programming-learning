cam_bien = {
    "S1": {"gia_tri": 26.5, "don_vi": "°C"},
    "S2": {"gia_tri": 31.2, "don_vi": "°C"},
}
nguong_c = 30.0
so_canh_bao = 0
for ma, ho_so in cam_bien.items():
    if ho_so["don_vi"] == "°C" and ho_so["gia_tri"] > nguong_c:
        so_canh_bao += 1
ma_duy_nhat = set(cam_bien.keys())
print("So cam bien:", len(ma_duy_nhat))
print("So canh bao:", so_canh_bao)
print("S3:", cam_bien.get("S3", "CHUA CO"))
