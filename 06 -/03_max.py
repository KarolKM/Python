def user_numbers():
    user = range(0, int(input('Ile chcesz podać liczb: ')))
    user_list = []
    for i in user:
        user_list.append(int(input(f'Podaj swoją{i+1} liczbę: ')))
    user_list.sort()
    print(user_list[-1])


user_numbers()





