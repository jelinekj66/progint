class Rectangle:
    def __init__(self, width: float, height: float):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

    def is_square(self):
        return self.width == self.height

    def scale(self, factor: float):
        self.width *= factor
        self.height *= factor

    def describe(self):
          shape_name = "Čtverec" if self.is_square() else "Obdélník"
          return f"{shape_name} {self.width} × {self.height}, obsah {self.area()}, obvod {self.perimeter()}."

rectangles = [
    Rectangle(3, 4),
    Rectangle(5, 5),
    Rectangle(2, 8),
    Rectangle(6, 3)
]


rectangles[0].scale(2)

# 2. Vypsání popisů všech obdélníků v seznamu
print("Seznam obdélníků:")
for rect in rectangles:
    print(f"- {rect.describe()}")

# 3. Nalezení obdélníku s největším obsahem
# Funkce max() porovnává objekty na základě klíče (key), kterým je metoda area()
max_rect = max(rectangles, key=lambda r: r.area())

print("\nNejvětší obdélník:")
print(f"-> {max_rect.describe()}")