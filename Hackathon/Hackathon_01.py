# Książka adresowa:
def first_screen():
    print("Wybierz z menu wpisując odpowiednią cyfrę (1-4): "
          "\n1. Pokaż wszystkie kontakty "
          "\n2. Stwórz nowy kontakt "
          "\n3. Usuń isntniejący kontakt "
          "\n4. Wyjdź z Książki adresowej ")


def menu():
    if user_choice == 1:
        if not address_book:
            contacts_list(address_book)
        else:
            show(address_book)
    elif user_choice == 2:
        new_contact(address_book)
    elif user_choice == 3:
        delete_contact(address_book)
    else:
        print('Błędna wartość, prosze podać liczbę przypisaną do opcji z mane')


def contacts_list(book):
    for i in range(len(lista_imion)):
        book.append([lista_imion[i], lista_nazwisk[i], lista_miast[i], lista_numer[i]])
        i += 1
    show(book)
    return book


def generate_contact(book):
    for i in range(len(lista_imion)):
        book.append([lista_imion[i], lista_nazwisk[i], lista_miast[i], lista_numer[i]])
        i += 1

    return book


def show(contact):
    for i in contact:
        print(i)


def new_contact(new):
    lista_imion.append(input('Podaj imie nowego kontaktu: '))
    lista_nazwisk.append(input('Podaj nazwisko nowego kontaku: '))
    lista_miast.append(input('Podaj miasto nowego kontaktu: '))
    lista_numer.append(input('Poadaj numer nowego kontaktu: '))
    new.append([lista_imion[-1], lista_nazwisk[-1], lista_miast[-1], lista_numer[-1]])
    print(f'Nowy kontakt "{lista_imion[len(lista_imion) - 1]}" o numerze {lista_numer[len(lista_imion) - 1]} dodany')

    return new


def delete_contact(contact):
    print(contact)
    deletion_choice = int(input("Podaj ID kontaktu do usunięcia: "))
    contact.pop(deletion_choice)
    print('Kontakt został usunięty!')

    return contact


lista_imion = ['Michał', 'Jannina', 'Marek', 'Jan']
lista_nazwisk = ['Woźniak', "Kowalska", "Nowak", 'Wiśnia']
lista_miast = ['Sopot', 'Gdańsk', 'Gdynia', 'Puck']
lista_numer = ['+48 111 111 111', '+48 222 222 222', '+48 333 333 333', '+48 444 444 444']
address_book = []
first_screen()
user_choice = int(input('-----> '))

while user_choice != 4:
    if not address_book:
        generate_contact(address_book)
    else:
        menu()
        first_screen()
        user_choice = int(input('-----> '))
print('Koniec programu, dziękuje i życzę dużo zdrowia!! :)')

# print(dic_full_name)
# for i in range(len(lista_imion)):
#     dic_name_city[dic_full_name] = lista_miast[i]
#     i += 1
# print(dic_name_city)
# print(contacts['Sopot'])

# if user_choise >= 1 and user_choise < 5:
#     menu()
# else:
#     print("błędna wartość, podaj liczbę przypisaną do opcji w menu")
