price = 15
while (price > 10):
    print(price, "$ - za drogo")
    price -= 2
print(price,'$ super cena!')

#ex 1:
print('-'*7, 'ex 1', '-'*7)

for i in range(0,201,20):
    print(i, "F to ", round((i-32)*5/9,2), "C")

f = 0
while (f<=200):
    C = round(5/9 * (f-32), 2)
    print(C)

    f+=20

#ex 2:
print('-'*7, 'ex 2', '-'*7)
secret_number = 9
user_number = int(input("Zgadnij liczbę od 0 do 20: "))
while user_number != secret_number:
    user_number = (int(input("Błędna liczba, spróbuj ponownie: ")))
print('Dokłądnie, prawidłowa liczba to', secret_number)
