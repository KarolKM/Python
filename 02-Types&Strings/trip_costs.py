distance = 120
fuel_cost = 5.04
used_fuel = (6.4/100)

x = round(distance * used_fuel * fuel_cost, 2)
print(f"Koszt wyprawy bedzie wynosil: {x} zl")

new_distance = int(input('Podaj ile kilometrów przejechałeś: '))
new_fuel_cost = float(input("Podaj jak była cena paliwa: "))
new_used_fuel = float(input('Podaj jakie było spalanie [l/100km]: '))/100

result = round(new_distance * new_fuel_cost * new_used_fuel, 2)
print(f'Koszt Twojej wyprawy wynosi {result} zł')
