example = {
  'a': 1,
  'b': 2,
  'c':3
}

print(example)


for key, value in example.items():
  print(key, '--->', value)

#ex 1
lists_to_dict = [(1, 'jeden'),(2,'dwa')]
dict_from_list = dict(lists_to_dict)
print(dict_from_list)
for i in dict_from_list.items():
  print(i)

#ex 2


#ex 3
print('Podaj wymiar tablicy.')
n = int(input())

array = [['_'] * n] * n
print(array)
print('--------------')

for row in array:
    for col in row:
      print(col, end=' ')
    print()

#ex 4

#ex 5
txt = """Szybko, zbudź się, szybko, wstawaj
Szybko, szybko, stygnie kawa
Szybko, zęby myj i ręce"""


txt = txt.replace(',', '')
txt = txt.lower()
words = txt.split()
# print(words)

counting_dict = {}

for word in words:
  if word in counting_dict:
    counting_dict[word] += 1
  else: #jeszcze słowa nie ma w słowniku
    counting_dict[word] = 1 # dodaj klucz do słownika po raz pierwszy - wartość 1

# print(counting_dict)

for k, v in counting_dict.items():
  print(k, '---->', v)

#ex 6:


#ex 7:


#ex 8:


#ex 9:


#ex 10:

