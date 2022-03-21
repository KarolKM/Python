import shapes


def show_menu():
    print('Wybierz kształto pomieszczenia: ')
    print("1. Kwadrat")
    print("2. Prostokąt")
    print("3. Trapez")


def main():
    rooms_number = int(input('Podaj liczbę pokoi: '))

    for r in range(rooms_number):
        show_menu()
        room_shape = input()

        if room_shape == '1':
            a = float(input("Podaj długość ściany [m]: "))
            room_area = shapes.square(a)
            print(room_area)
        elif room_shape == '2':
            a = float(input("Podaj długość  pirwszej ściany [m]: "))
            b = float(input("Podaj długość drugiej ściany [m]: "))
            room_area = shapes.rectangle(a, b)
            print(room_area)
        elif room_shape == '3':
            a = float(input("Podaj długość  pirwszej ściany [m]: "))
            b = float(input("Podaj długość drugiej ściany [m]: "))
            h = float(input("Podaj wysokość [m]: "))
            room_area = shapes.trapezoid(a, b, h)
            print(room_area)


if __name__ == '__main__':
    main()
