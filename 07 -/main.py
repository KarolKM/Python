# f = open('plik.txt')
# print(f.readlines())
#
# f.close()
#
#
# with open('plik.txt') as f:
#     print(f.readlines())

filename = 'tekst.txt'

# with open(filename, 'r') as f:
#     content = f.read()
#     print(content)
#
# try:
#     with open(filename, 'r') as f:
#         con = f.read()
# except FileExistsError:
#     print('Twoj plik się nie otworzył')

# with open(filename, 'r') as fopen:
#   while True:
#     current_line = fopen.readline()
#
#     # aktualna linia jest pusta
#     if current_line == '':
#       # dotarlismy do konca
#       break
#     print(current_line)


# with open(filename, 'r') as fopen:
#     lines = fopen.readlines()
#
# # for nr in range(len(lines)):
# #   print(f'Linia {nr} -> {lines[nr]}')
#
#
# for nr, value in enumerate(lines):
#     print(f'linia {nr} --> {value}')
#
# with open('save.txt', 'w') as f:
#     f.write('Line 1\n')
#     f.write('Line 2\n')
#     f.write('Line 3\n')
#     f.write('Line 4\n')

# sweets_list = ['chocolate', 'lollipop', 'cookie', 'candy']
#
# with open('save.txt', 'w') as f:
#     f.write('\n'.join(sweets_list))

with open('tekst.txt', 'r', encoding='cp1250') as fopen:
  content = fopen.read()
print(content)
