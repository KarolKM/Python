
season = input("Wprowadź nazwę pory roku: ")

if season == 'wiosna':
    print('zasadź rośliny')
elif season == 'lato':
    print('podlewaj ogród')
elif season == 'jesien':
    print('zbierz owoce')
elif season == 'zima':
    print('brrr za zimno!')
else:
    print('nie ma takiej pory roku')

# ex 1 IF:
print("-"*7,"ex 1 IF:","-"*7,"\n")
number = int(input("wprowadź liczbe: "))
if number % 3 == 0:
    print("Twoja liczba jest podzielna przez 3!!")
else:
    print("nie podzielna przez 3")

# ex 2 IF:
print("-"*7,"ex 2 IF:","-"*7,"\n")
x1 = int(input("Wprowadź pierwszą liczbę całkowitą: "))
x2 = int(input("wprowadź drugą liczbę całkowitą: "))
if x1 + x2 > 100:
    print(x1 + x2)
else:
    print("Koniec")

# ex 3 IF:
print("-" * 7, "ex 3 IF:", "-" * 7, "\n")
score1 = int(input("Podaj pierwsza ocene w skali 1-10: "))
score2 = int(input("Podaj drugą ocene w skali 1-10: "))
score3 = int(input("Podaj trzecią ocene w skali 1-10: "))
if (score3 + score2 + score1)/3 > 7:
    print("Bardzo dobra")
elif (score3 + score2 + score1)/3 < 5:
    print("Nie warta uwagi")
else:
    print("Przeciętna")

# ex 4 IF:
print("-" * 7, "ex 4 IF:", "-" * 7, "\n")

# ex 5 IF:
print("-" * 7, "ex 5 IF:", "-" * 7, "\n")
password = input("Wprowadź nowe hasło: ")
if len(password) < 8:
    print("Twoje haslo jest za krotkie! :)")
elif password.islower():
    print("W twoim haśle brakuje wielkiej litery! :(")
elif password.isupper():
    print("W Twoim haśle brakuje malych liter!! :(")
elif password.isalpha() or password.isdigit():
    print("Hasło nieprawidłowe")
else:
    print("Twoje hasło zostało zapisane!!")
