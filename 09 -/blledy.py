age = input("Podaj wiek")
if age.isdigit():
    print(age)
else:
    print("nieprawidlowa wartość")

try:
    age = int(input("Podaj wiek"))
except ValueError:
    print("nieprawidłowa wartość")

