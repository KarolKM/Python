txt = 'Mata'
new_txt = 't' + txt[1:]
print(txt.replace('M', 't'))
print(new_txt)
print(type(txt))

print("-"*15)

#ex 1:
print("ex 1: \n")
tekst = 'Alamakota'
mid = len(tekst)//2
print(tekst[(mid-1):(mid+2)])
print("-"*15)

#ex 2:
print("ex 2: \n")
s1 = 'zameczek'
s2 = 'koło'
s3 = s1[:len(s1)//2] + s2 + s1[len(s1)//2:]
print(s3)
print("-"*15)

#ex 3:
print("ex 3: \n")
quote = "Honesty is the first chapter in the book of wisdom."
print('Liczba wszystkich znaków: ', len(quote)+1)
print(quote[(-(len('wisdom')+1)):-1])
print(quote[:len(quote)//2])
print(quote[-1])
print(quote[len(quote)//2::3])
print("nie mam pojęcia, póki co. :)")
print(quote.replace('wisdom', 'friendship'))
print("-"*15)

#ex 4:
print("ex 4: \n")
title = input("Podaj tytuł Twojej ulubionej książki: ")
author = input("Podaj Autora Twojej ulubionej książki: ")
pages = input("Podaj ilość stron Twojej ulubionej książki: ")
print("Czy tytuł ksiązki zawiera tylko litery? ", title.isalpha())
print("Czy Nazwisko składa sie tylko z liter? ", author.isalpha())
print("Czy Liczba stron składa sie tylko z cyfr? ", pages.isdigit())
print("Pozwól, że poprawię wielkość liter: ", title.capitalize(), '\n', author.capitalize(),)
book = title + " " + author + " " + pages
print("To są pełne informacje dotyczące Twojej ulubionej książki: ", book)
print("Liczba wszystkich znaków użytych w Twojej ulubionej książce: ", len(book))
print("-"*15)

#ex 5:
print("ex 5: \n")
text = input("Wprowadź swoj tekst: ")
palindrom = text[::-1]
print("Czy", palindrom, " jest palindromem? ", text == palindrom)
print("-"*15)

#ex 6:
print("ex 6: \n")
this = ('''The Zen of Python, by Tim Peters
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!''')
print("liczbę wystąpień słowa 'better': ", this.count('better'))
print("-"*15)
print(this.replace('*',''))
print("-"*15)
print(this.replace('explain', 'understand',1))
print("-"*15)
print(this.replace(' ', '-'))
print("-"*15)
print(this.split('.'))
print("-"*15)

#ex 7:
print("ex 7: \n")
print("-"*15)
