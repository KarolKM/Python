#ex 1
print("*"*7, "ex_1", "*"*7)
age = int(input("Podaj swój wiek: "))
if age < 18:
    print("Użytkownik niepełnoletni")
    print("do pełnoletności brakuje", 18 - age, "wiosen")
else:
    print("Użytkownik pełnoletni")
    if age > 99:
        print("200 lat ♫")

#ex 2
print("*"*7, "ex_2", "*"*7)
weight = int(input('podaj swoja wage --> (kg) '))
high = float(input('podaj swoja wysokosc --> (m) '))

BMI = weight / high**2
if BMI < 18.5:
    print("Niedowaga")
elif BMI >= 18.5 and BMI <24:
    print("Waga normalna")
elif BMI >= 24 and BMI < 26.5:
    print("Lekka nadwaga")
elif BMI >= 26.5 and BMI < 30:
    print("Nadwaga")
elif BMI >= 30 and BMI < 35:
    print("Otyłość I stopnia")
elif BMI >= 35 and BMI < 40:
    print("Otyłość II stopnia")
elif BMI >= 40:
    print("Otyłość III stopnia")

#ex 3
print("*"*7, "ex_3", "*"*7)
num_1 = int(input("Wprowadź pierwszą z trzech liczb: "))
num_2 = int(input("Wprowadź drugą z trzech liczb: "))
num_3 = int(input("Wprowadź trzecią z trzech liczb: "))
all_nums = [num_1, num_2, num_3]
print(max(all_nums))
