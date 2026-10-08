celkovy_cas = int(input("celočíselně zadejte čas v sekundách: "))
d = celkovy_cas // 86400
zbytek_d = celkovy_cas % 86400
h = zbytek_d // 3600
zbytek_h = zbytek_d % 3600
m = zbytek_h // 60
s = zbytek_h % 60
if celkovy_cas >= 86400:
    print(f"{d:02d}:{h:02d}:{m:02d}:{s:02d}")
else:
    print(f"{h:02d}:{m:02d}:{s:02d}")
