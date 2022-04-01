miejsca = [
'dom', 'szkoła', 'kościół', 'bar', 'szpital', 'kino', 'teatr'
]
macierz_sasiedztwa = [
    [0, 1, 1, 1, 0, 0, 0],
    [1, 0, 0, 0, 1, 0, 0],
    [1, 0, 0, 1, 0, 1, 0],
    [1, 0, 1, 0, 1, 0, 0],
    [0, 1, 0, 1, 0, 1, 1],
    [0, 0, 1, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 1, 0]
]

for row in range(0, len(miejsca)):
    for col in range(0, len(miejsca)):
        if macierz_sasiedztwa[row][col] == 1:
            print(miejsca[row], '--->', miejsca[col])


