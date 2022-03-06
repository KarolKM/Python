text = "kot"

for letter in text:
    print("_", letter)

my_list = ["Ada", "Ruby", "Julia"]
for step in my_list:
    print("Hello", step)

for i in range(5, 10):
    print(i)
for i in range(5, 21, 2):
    print(i)

for i in range(3):
    print(i, ":", my_list[i])

#ex 1:
print('-'*7, 'ex 1', '-'*7)
tool = ['buty', 'scyzoryk', 'woda']
for i in tool:
    print(i)
print("Great, we are ready!")

#ex 2:
print('-'*7, 'ex 2', '-'*7)
dish = ['mieso', 'cebula', 'czosnek', 'pomidory', 'zioła']
for i in dish:
    print('Dodaj: ', i)
print('Smaż na patelni przez 10-15 minut.')
print('Podaj z ugotowanym makaronem na głębokim talerzu.')
print('Smacznego!! :D')

#ex 3:
print('-'*7, 'ex 3', '-'*7)
items = 0
for i in range(1, 11):
    items += i
    print(items)

#ex 4:
print('-'*7, 'ex 4', '-'*7)
s = 1
power = int(input("Podaj liczbę od 0 do 7, a ja policzę silnię: "))
if power < 8:
    if power in (0,1):
        print(power, '! = 1')
    else:
        for i in range(2, power+1):
            s = s*i
        print (power, '! = ', s)
else:
    print("Nieprawidłowa liczba!!")
