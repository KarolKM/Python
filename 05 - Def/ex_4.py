#Napisać funkcję, która wypisze wszystkie parzyste z przekazanej listy elementów (wykorzystać funkcje z pkt 2)
def user_choice():
    user_elements = []
    amount_of_numbers = int(input("Ile chcesz podać liczb? ---> "))
    for x in range(0, amount_of_numbers):
        x = int(input(f"wprowadz {x+1} swoją liczbę : "))
        user_elements.append(x)
    return user_elements


def is_even(elements):
    print("To są liczby parzyste z Twojej listy: ", end=" ")
    for x in elements:
        if x % 2 == 0:
            print(x, end=" ")


def main():
    lista = user_choice()
    is_even(lista)

if __name__ == '__main__':
    main()
