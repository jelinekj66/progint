def circle_area(d):
    r = d / 2
    area = 3.14 * r ** 2
    return area

def tube_cross_section(d_out, d_in):
    return circle_area(d_out) - circle_area(d_in)

def tube_mass(d_out, d_in, length, density=7850):
    cross_section = tube_cross_section(d_out, d_in)
    volume = cross_section * length
    return volume * density

print(round(tube_mass(0.060, 0.050, 6):.2f))
print(round(tube_mass(0.060, 0.050, 6, density=2700):.2f))

    