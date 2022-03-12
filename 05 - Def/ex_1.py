#Napisać funkcję, która oblicza pole koła na podstawie zadanego promienia.

def circle_field(radius):
    pi = 3.14
    area = pi * radius**2
    print(area)

circle_field(int(input("podaj promień kołą: ")))

