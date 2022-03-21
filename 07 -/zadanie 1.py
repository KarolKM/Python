import random


def open_file(filename):
    with open(filename, 'r', encoding='utf-8') as fopen:
        quotes = fopen.readlines()
    return quotes


def Cytat_Dnia(content):
    quote = random.choice(content).strip()
    quote = quote.split('-')
    width = len(quote[0]) * 2

    print('Quote of the day: \n')
    print(width * '*')
    print(quote[0].center(width))
    print(quote[1].center(width))
    print(width * '*')

quotes_list = open_file('cytaty.txt')
Cytat_Dnia(quotes_list)
