length = float(input("délka [mm]: "))
cm = length / 10
m = length / 1000
pal = length / 25.4

print(f"{length:.3f}mm = {cm:.3f}cm = {m:.3f} = {pal:.3f}in")