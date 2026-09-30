# number of valuse (constant)
N = 5
total = 0

print(f"Zadej {N} čísel")

for i in range(1, 6):
    x = float(input(f"Hodnota #{i}: "))
    total += x

avarage = total / N
print("Průměrná hodnota:", avarage)