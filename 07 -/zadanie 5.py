def get_tekst(file):
    with open(file, 'r', encoding='utf-8') as f:
        tekst = f.read()
    return tekst


def erase_extras(content):
    special_signs = ',./?()!;:'

    for s in special_signs:
        content = content.replace(s, "")
    print(content)

    return content


def longest_word(content):
    words_list = content.split(' ')
    a = ""
    for i in words_list:
        if len(i) > len(a):
            a = i
    return a



tekst = get_tekst('tekst.txt')
tekst = erase_extras(tekst)
find_word = longest_word(tekst)

print(find_word, "o dlugosci = ", len(find_word))



