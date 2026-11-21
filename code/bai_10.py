from dataclasses import dataclass

@dataclass
class SensorReading:
    ma: str
    nhiet_do_c: float

    def is_alert(self, nguong_c: float) -> bool:
        return self.nhiet_do_c > nguong_c

s1 = SensorReading("S1", 31.5)
s2 = SensorReading("S2", 29.0)
print(s1.ma, s1.is_alert(30.0))
print(s2.ma, s2.is_alert(30.0))
