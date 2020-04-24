k = 0 #password length
counter = 0 # current step in 10

alphabet = '0123456789abcdefghijklmnopqrstuvwxyz'
base = len(alphabet)
while k < 4:
    number = '' #password string in our count sys

    #code
    i = counter
    while i > 0:
        r = i % base
        number = alphabet[r] + number
        i = i // base

    number = alphabet[0] * (k - len(number)) + number

    print(counter, number)

    counter += 1
    if number ==alphabet[-1] * k: #максимальный_для_текущей_длины:
        k += 1
        counter = 0