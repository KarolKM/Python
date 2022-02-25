txt = 'Mata'
new_txt = 't' + txt[1:]
print(txt.replace('M', 't'))
print(new_txt)
print(type(txt))
print("----------------")

#ex 1:
print("ex 1: \n")
tekst = 'Alamakota'
mid = len(tekst)//2
print(tekst[(mid-1):(mid+2)])
print("----------------")

#ex 2 do domu!!!!
print("ex 2: \n")
s1 = 'zameczek'
s2 = 'koło'
s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]
print(s3)
print("----------------")

#ex 3:
print("ex 3: \n")
quote = "Honesty is the first chapter in the book of wisdom."
print('Liczba wszystkich znaków: ', len(quote)+1)
print(quote[(-(len('wisdom')+1)):-1])
print(quote[:len(quote)//2])
print(quote[-1])
print(quote[len(quote)//2::3])
print()
print(quote.replace('wisdom', 'friendship'))


print("----------------")

#ex 4:
print("ex 4: \n")

print("----------------")