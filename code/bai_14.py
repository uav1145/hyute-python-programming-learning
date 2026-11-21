from scipy.optimize import brentq

def chenhlech_ap(q):
    ap_quat_pa = 500 - 0.5 * q**2
    ap_he_pa = 20 + 0.7 * q**2
    return ap_quat_pa - ap_he_pa

a, b = 0.0, 30.0
assert chenhlech_ap(a) * chenhlech_ap(b) < 0
q_nghiem = brentq(chenhlech_ap, a, b)
phan_du_pa = chenhlech_ap(q_nghiem)
print(f"q* = {q_nghiem:.3f} (don vi quy uoc)")
print(f"Phan du = {phan_du_pa:.3e} Pa")
