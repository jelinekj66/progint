bity_list = [8, 16, 32, 64]
for bity in bity_list:
    unsigned_max = (2**bity) - 1
    
    signed_min = -(2 ** (bity - 1))
    signed_max = (2 ** (bity - 1)) - 1
    print(f"{bity:2} bitů: 0 až {unsigned_max}, {signed_min} až {signed_max}")
