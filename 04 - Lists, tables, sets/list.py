# lista = [1, 2, 3]
# print(sum(lista))
#
# lista[1] = "pipin"
# lista.append(8)
# lista.insert(1, "new")
# nowa_lista = lista.pop(1)
# lista.remove(1)
# del lista
#
# print(lista[1])
# print(lista)
#
# #ex 1
# print("*"*7,"ex 1","*"*7)
# bag = ["latarka", 'nóż', 'czapka']
# bag.sort()
# print(bag)
#
# #ex 2
# print("*"*7,"ex 2","*"*7)
# print('Podaj 10 liczb: ')
# numery = []
#
# for i in range(1,11):
#     numery.append(int(input(f"wprowadz {i} liczbe: ")))
#     i+=1
# print(f'To są Twoje liczby: {numery[:]}\n Teraz ja wyświetle tylko liczby nieparzyst: ')
# for i in numery:
#     if i % 2 != 0:
#         print(i)
#
# #ex 3
# items = ['namiot', 'latarka', 'bidon', 'namiot']
#
# counter = len(items)
# first = items[0]
# last = items[counter-1]
#
# print(first == last)
#
# print(items[0] == items[-1])
#
# # ex 4
print("*"*7,"ex 4","*"*7)
elements = []
amount = int(input("Ile elementów chcesz wprowadzić? Podaj liczbę parzystą: "))
choice = ""

#### Próba z jedną pętlą:
# while len(elements) % 2 != 0:
#     for i in range(amount):
#         elements.append(input(f'Podaj {i+1} element: '))
#         i += 1
#         if len(elements) % 2 == 0:
#             print('Czy chcesz dodadac kolejne dwa elementy? (yes / no)')
#             choice = input(str)
#             if choice == 'yes':
#                 continue
#             continue

###Próba z dwoma pętlami:
while amount % 2 != 0:
    print('Lizcba nieparzysta')
    amount = int(input('Ponownie podaj liczbę parzystą, elementów które chcesz wprowadzić: '))
for i in range(amount):
    elements.append(input(f'Podaj {i+1} element: '))
    i += 1
print(f'To jest Twoja lista {len(elements)} elementów:  {elements[:]}')
el_s1 = elements[int((len(elements)/2))-1]
el_s2 = elements[int(len(elements)/2)]

if el_s2 == el_s1:
    print(f"Oba elementy środkowe {el_s1} i {el_s2} są takie same")
else:
    print(f"Oba środkowe {el_s1} i {el_s2} elemnety sie różnią")

# # ex 5
# print("*"*7,"ex 5","*"*7)
# people = [
#     ["Dorota", "Wellman", "dziennikarka"],
#     ["Adam", "Małysz", "sportowiec"],
#     ["Robert", "Lewandowski", "piłkarz"],
#     ["Krystyna", "Janda", "aktorka"]
# ]
# for i in people:
#     print("*"*40)
#     for item in i:
#         print(item, end=' ')
#     print()
