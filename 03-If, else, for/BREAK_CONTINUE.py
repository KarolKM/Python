#Zadania podsumowujące całość:

#ex 1
print('*'*7, "ex 1", '*'*7)
names = input("Podaj imiona wszystkich graczy (oddziel każdą nazwę gracza ','): ")
name = names.split(",")
for i in name[0:]:
    print('hello', i)

#ex 2
print('*'*7, "ex 2", '*'*7)
text = input("Podaj dowolny ciąg znaków: ")
print(text[1::2])
for i in text[1::2]:
    print(i)

#ex 3
print('*'*7, "ex 3", '*'*7)
tekst = input('Podaj swój tekst: ')
w = 0
m = 0
c = 0
s = 0
for i in tekst:
    if i.isupper():
        w += 1
    elif i.islower():
        m += 1
    elif i.isnumeric():
        c += 1
    else:
        s += 1
print('W Twoim tekscie występuje', w,'wielkich liter')
print('W Twoim tekscie występuje', m, 'małych liter')
print('W twoim tekscie wystepuje', c, 'cyfr')
print('W twoim tekscie wystepuje', s, 'znaków specjalnych')
