def mood():
    print('How are You?')

mood()
def my_mood(answear):
    print('My mood today: ')
    print(answear)

resp = input('How are you? \n')
my_mood(resp)

def my_mood(answear):
    return answear * 5

resp = input('How are you?')
twiced = my_mood(input("sprawdz"))
print("My mood is like", twiced)

zestaw = {}

def save_book_score():
    book_title = input("Podaj tytuł ksiązki: ")
    score = input("Podaj ocene książki w skali 1 - 10: ")
    zestaw[book_title] = score
def show_book(title):
    print(f'Książka {title} ma ocenę {zestaw[title]}')

for i in range(3):
    save_book_score()
    print("-------------")

print(zestaw)

while(True):
    given_title = input("Podaj tytul do sprawdzenia: ")
    if given_title in zestaw.keys():
        break

    print("Podaj inny tytul: ")

show_book(given_title)

