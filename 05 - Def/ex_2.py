# Napisać funkcję, która sprawdza czy liczba jest parzysta.

def is_even(number):
    if number % 2 == 0:
        print('liczba jest parzysta')
    else:
        print('liczba nieparzysta')

user_number = int(input("Podaj Twoją liczbę: "))
is_even(user_number)

