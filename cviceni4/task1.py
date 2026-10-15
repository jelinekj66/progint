diameters = [25.01, 24.97, 25.06, 25.00, 24.94, 25.03, 25.05, 24.95, 25.10, 24.99]
zmetci = 0
rozmer = 25.00
tol = 0.05
minl = rozmer - tol
maxl = rozmer + tol
for position, d in enumerate(diameters, start=1):
    if d > maxl:
           zmetci += 1
           print(position,":", d, "Velký")
    elif d < minl:
     zmetci += 1
     print(position,":", d, "Malý")     
    else:
       print(position,":", d, "Ok")
procentozmetku = zmetci / len(diameters) * 100
print("zmetků: ", zmetci, "z", len(diameters), "(", int(procentozmetku),"%", ")")