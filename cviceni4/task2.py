roky = list(range(1890,2031))
prestupne_roky = [
    rok
    for rok in range(1890, 2031)
    if(rok % 4 == 0 and not rok % 100 == 0) or rok % 400 == 0
]

max_na_radek = 10

for i in range(0, len(prestupne_roky), max_na_radek):
    print(*(prestupne_roky[i:i + max_na_radek]), "počet přetupých roků: ", len(prestupne_roky))

    