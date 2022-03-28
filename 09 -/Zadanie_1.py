elements = [13, "string", 2.45, 0, ('1', '2'), [], {1,2}, {'klucz': 123}, range(10)]

for elem in elements:
    try:
        result = 10 / elem
    except (TypeError, ZeroDivisionError):
        print(f'{elem} - nie może być dzielnikiem')
    except:
        print('Nie spodziewany błąd')

print('Koniec')