nhiet_do_c = [25.1, 31.0, 29.5, 31.0]
nguong_c = 30.0
chi_so_vuot = []
for i, gia_tri in enumerate(nhiet_do_c):
    if gia_tri > nguong_c:
        chi_so_vuot.append(i)
nguong_cauhinh = (20.0, 30.0)  # tuple 2 nguong minh hoa
print("Vi tri vuot:", chi_so_vuot)
print("Cau hinh:", nguong_cauhinh)
