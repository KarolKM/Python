#1▹ Skorzystaj ze swojego kodu bmi.py. Rozbij liczenie bmi
# na funkcję obliczającą bmi na podstawie danych użytkownika oraz zwracającą odpowiednią wartość
# (niedowaga, waga normalna, nadwaga, otyłość) w zależności od otrzymanego parametru.

def bmi():
    weight = int(input("Podaj swoją wagę: "))
    height = float(input("Podaj swoją wysokość: "))
    result = weight / height**2

def bmi_state(bmi):
    if bmi < 18:
        return 'nidowaga'
    elif bmi < 25:
        return 'w normie'
    elif bmi < 30:
        return 'nadwaga'
    else:
        return 'otyłość'


result = bmi()
check_helth = float(bmi_state(result))
print(result)
print(check_helth)

