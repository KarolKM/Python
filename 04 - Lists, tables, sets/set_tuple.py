#Tuple:

#ex 1:
animal = ('pies', 'samoyed', 'Dog')
(typ, race, name) = animal
print(f'Moj {typ} rasy {race} wabi sie {name}.')

#ex 2:


#ex 3:


#SETS:
# ex 1:

elements = (1, 1, 2, 2, 3, 3, 4, 5, 7, 7, 7, 6, 4, 3, 3, 5)
new_elements = set(elements)
print(new_elements)

#ex 2:


#ex 3:

el_1 = ("Ala", "Ewa", "Ola", "Jola")
el_2 = ("Adam", "Jan", "Michał", "Paweł")
L_el_1 = list(el_1)
L_el_2 = list(el_2)

#ex 4:


#ex 5:

new_list = L_el_1[1::2] + L_el_2[::2]
S_new_list = set(new_list)
print(new_list)
print(S_new_list)
