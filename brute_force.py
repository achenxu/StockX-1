from itertools import product
from random import randint

password = str(randint(1000, 9999))  # creates a random 4 digit pin
print('Password:', password)

for guess in product([a for a in range(10)], repeat=4):  # creates cartesian product of all the digits, 4 digits / tuple
    guess = ''.join(str(n) for n in guess)  # convert int tuple into str to use .join
    if guess == password:  # check if the guessed pin is the password
        print('PIN: {:>9}'.format(guess))
        break  # break when the pin is found
