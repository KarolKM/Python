import bmi

# def show_advice(state):
#     filename = state + '.txt'
#     with open(filename) as fopen:
#         content = fopen.read()
#
#     print('----Twoja porada:')
#     print(content)


def main():
    try:
        w = float(input('Podaj swoją wagę [kg]: '))
        h = float(input('Podaj swoj wzrost [m]: '))
        print(bmi.get_bmi_value(w, h))
        # show_advice(result)
    except ValueError:
        print("To jest niprawidłowa wartość, podaj wartość liczbowo!")
    except:
        print(w)

if __name__ == '__main__':
    main()
