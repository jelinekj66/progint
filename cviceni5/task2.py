def convert_temperature(value, from_unit, to_unit):
    valid_units = {"C", "F", "K"}
    if from_unit not in valid_units or to_unit not in valid_units:
        return None
    if from_unit == "C":
        celsius = value
    elif from_unit == "F":
        celsius = (value - 32) * 5 / 9
    elif from_unit == "K":
        celsius = value - 273.15
        
    if to_unit == "C":
        return celsius
    elif to_unit == "F":
        return celsius * 9 / 5 + 32
    elif to_unit == "K":
        return celsius + 273.15

print(convert_temperature(100, "C", "F"))   # 212.0
print(convert_temperature(0, "K", "C"))     # -273.15
print(convert_temperature(-40, "C", "F"))   # -40.0
print(convert_temperature(20, "C", "X"))  

for c in range(-40, 101, 20):
    f = convert_temperature(c, "C", "F")
    k = convert_temperature(c, "C", "K")
    print(f"{c:6.1f} | {f:6.1f} | {k:8.2f}")

     
        
