# Prompts the user for an amount, and outputs the minimal number of banknotes
# needed to match that amount, as well as the detail of how many banknotes
# of each type value are used.
# The available banknotes have a face value which is one of
# $1, $2, $5, $10, $20, $50, and $100.


import sys

desired_number = input('Input the desired amount: ')
try:
    desired_number = int(desired_number)
except ValueError:
    sys.exit()

d = {}
banknote = [100, 50, 20, 10, 5, 2, 1]
for e in banknote:
    n = desired_number // e
    d[e] = n
    desired_number = desired_number - n * e

number_of_banknot = sum(d.values())
if number_of_banknot == 1:
    print('\n1 banknote is needed.')
else:
    print(f'\n{number_of_banknot} banknotes are needed.')

print('The detail is:')
for e in d.items():
    if e[1]:
        # {   :>4}!!!
        print(f'{"$" + str(e[0]):>4}: {e[1]}')   