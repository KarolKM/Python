#1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi
# na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

# def bmi():
#     weight = int(input("Podaj swoją wagę: "))
#     height = float(input("Podaj swoją wysokość: "))
#     result = weight / height**2
#
# def bmi_state(bmi):
#     if bmi < 18:
#         return 'nidowaga'
#     elif bmi < 25:
#         return 'w normie'
#     elif bmi < 30:
#         return 'nadwaga'
#     else:
#         return 'otyłość'
#
#
# result = bmi()
# check_helth = float(bmi_state(result))
# print(result)
# print(check_helth)
#

#Zadanie_2:
# def user_num():
#     liczby = []
#     print('Podaj 3 cyfry a ja znajdę najmniejszą :) ---> ')
#     for i in range(0, 3):
#         i = int(input(f"Podaj {i+1} liczbę: "))
#         liczby.append(i)
#     return liczby
#
#
# def minimum(elem):
#     a = elem[0]
#     for i in elem:
#         if i < a:
#             a = i
#     print(f' Najmniejsza liczba to: {a}')
#
#
# def main():
#     min = user_num()
#     minimum(min)
#
#
# if __name__ == '__main__':
#     main()

# Zadanie 3:
# def user_num():
#     liczby = []
#     print('Podaj 3 cyfry a ja znajdę najmniejszą :) ---> ')
#     for i in range(0, 3):
#         i = int(input(f"Podaj {i+1} liczbę: "))
#         liczby.append(i)
#     return liczby
#
#
# def maximum(elem):
#     a = elem[0]
#     for i in elem:
#         if i > a:
#             a = i
#     print(f' Najmniejsza liczba to: {a}')
#
#
# def main():
#     max = user_num()
#     maximum(max)
#
#
# if __name__ == '__main__':
#     main()

#Zadanie_4:

# def zakres():
#     ilosc = 0
#     liczby = []
#     while ilosc < 2:
#         liczby.append(int(input(f'Podaj {ilosc + 1} liczbę z zakresu: ')))
#         ilosc += 1
#
#     return liczby
#
#
# def is_exist(zakres):
#     user_number = int(input("zgadnij jaka liczba znajduje sie w tym zakresie: "))
#     if user_number >= zakres[0] and user_number <= zakres[1]:
#         print("tak, liczba x znajduje się w zadanym zakresie")
#     else:
#         print("nie, liczba x jest z poza zakresu")
#
# def main():
#     lista = zakres()
#     is_exist(lista)
#
# if __name__ == '__main__':
#     main()

#Zadanie_5:



#Zadanie_6:


#Zadanie_7:

# def is_american_express(card_number):
#     card_length = len(card_number)
#     return card_length == 15 and (card_number[0:2] == '34' or card_number[0:2] == '37')
#
#
# def is_visa(card_number):
#     card_length = len(card_number)
#     return card_length in [13, 16] and card_number[0] == '4'
#
#
# def is_mastercard(card_number):
#     card_length = len(card_number)
#     starts_with_51_55 = 51 <= int(card_number[0:2]) <= 55
#     starts_with_2221_2720 = 2221 <= int(card_number[0:4]) <= 2720
#
#     return card_length == 16 and (starts_with_51_55 or starts_with_2221_2720)
#
# def get_card_number():
#     cards_lengths = [13, 15, 16]
#     while(True):
#         card_number = input('Podaj numer karty: ')
#         card_number = card_number.replace(' ', '')
#
#         if card_number.isdigit() and len(card_number) in cards_lengths:
#             break
#         else:
#             print('To nie jest nr karty, spróbuj jeszcze raz ')
#
#     return card_number
#
#
# #--- main code
#
# card_number = get_card_number()
# print('Numer karty użytkownika -->', card_number)
#
# if is_visa(card_number):
#     print("To jest visa")
# elif is_mastercard(card_number):
#     print("To jest master card")
# elif is_american_express(card_number):
#     print("To jest american express")
# else:
#     print("To może być inna karta")