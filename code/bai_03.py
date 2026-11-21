nhiet_do_c = 31.0
nguong_c = 30.0
if not -50 <= nhiet_do_c <= 150:
    trang_thai = "KHONG HOP LE"
elif nhiet_do_c > nguong_c:
    trang_thai = "CANH BAO"
else:
    trang_thai = "BINH THUONG"
print(trang_thai)
