import random

figures = {'k': 'kamień', 'p': 'papier', 'n': 'nożyce', 's': 'koniec gry'}
comp_option = ['k', 'p', 'n']
print('Witaj w grze Papier, Kamień, Nożyce!!! :)')
user_name = input("Podaj Swoje imie: ")
rounds = int(input("Podaj ilość rund, które chcesz rozegrać: "))

user_choice = []
user_points = 0
comp_choice = []
comp_points = 0

for i in range(rounds):
    print('Runda', i+1)
    user_choice.append(input('Aby przerwać, napisz "s" \nPodaj Twoją figurę (kamień (k) / papier (p) / nożyce (n)): '))
    comp_choice.append(random.choice(comp_option))
    print('Wybrałeś: ', figures[user_choice[i]])
    print('komputer wybrał: ', figures[comp_choice[i]])
    if user_choice[i] == comp_choice[i]:
        print(f'REMIS!!! \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'k' and comp_choice[i] == "p":
        comp_points += 1
        print(f'Wygrywa PAPIER!!! Punkt dla Komputera \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'k' and comp_choice[i] == "n":
        user_points += 1
        print(f'Wygrywa KAMIEŃ!!! Punkt dla {user_name} \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'p' and comp_choice[i] == "k":
        user_points += 1
        print(f'Wygrywa PAPIER!!! Punkt dla {user_name} \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'p' and comp_choice[i] == "n":
        comp_points += 1
        print(f'Wygrywają NOŻYCE!!! Punkt dla Komputera \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'n' and comp_choice[i] == "k":
        comp_points += 1
        print(f'Wygrywa KAMIEŃ!!! Punkt dla Komputera \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 'n' and comp_choice[i] == "p":
        user_points += 1
        print(f'Wygrywają NOŻYCE!!! Punkt dla {user_name} \nKomputer: {comp_points} : {user_points} : {user_name}')
    elif user_choice[i] == 's':
        break

print("dzieki za gre!!")
