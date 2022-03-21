def fibonnaci_numbers():
    n=int(input('Podaj ilość liczb w ciągu Fibonnaciego: '))
    fibonacci(n)
    for n in range(n):
        print(fibonacci(n))

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)

def main():
