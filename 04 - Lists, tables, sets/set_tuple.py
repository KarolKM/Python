#Tuple:

#ex 1:
animal = ('pies', 'samoyed', 'Dog')
(typ, race, name) = animal
print(f'Moj {typ} rasy {race} wabi sie {name}.')

#ex 2:
elements = ("kot", "pies", "mysz", "kot", "ptak")
print(elements)
for i in elements:
    count = elements.count(i)
    if count > 1:
        print(i)
        el_list = list(elements)
        el_list.remove(i)
        elements = tuple(el_list)

#ex 3:
liczby = 1, 2, 3, 4, 5, 56, 6, 7, 5, 213, 123, 321, 432, 54234, 243
user_choice = int(input("Zgadnij moją liczbę: "))
n = 0
for i in liczby:
    if user_choice == i:
        print(f'Liczba znalezione po indeksem numer {n}')
    else:
        n += 1


#SETS:
# ex 1:

elements = (1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 7, 6, 4, 3, 3, 5)
new_elements = set(elements)
print(new_elements)

#ex 2:
L_test = [1, 2, 3, 4]
T_test = (1, 2, 3, 4)
S_test = {1, 2, 3, 4}


#ex 3:

el_1 = ("Ala", "Ewa", "Ola", "Jola")
el_2 = ("Adam", "Jan", "Michał", "Paweł")
L_el_1 = list(el_1)
L_el_2 = list(el_2)
full_list = L_el_1 + L_el_2
set_el = set(full_list)
print(set_el)

#ex 4:
lista = [1, 2, 3, 4, 11, 12, 13, 14, 21, 22, 23, 24]
splited_1 = []
splited_2 = []
splited_3 = []

splited_1.append(lista[:4])
splited_2.append(lista[4:8])
splited_3.append(lista[8:])
print(splited_1, '\n', splited_2, '\n', splited_3)

#ex 5:

new_list = L_el_1[1::2] + L_el_2[::2]
S_new_list = set(new_list)
print(new_list)
print(S_new_list)
