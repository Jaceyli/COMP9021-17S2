from random import seed, randrange
import sys

arg_for_seed = input('Input a seed for the random number generator: ')
try:
	arg_for_seed = int(arg_for_seed)
except ValueError:
	print('Input is not an integer, giving up.')
	sys.exit()

nb_of_elements = input('How many elements do you want to generate? ')
try:
	nb_of_elements = int(nb_of_elements)
except ValueError:
	print('Input is not an integer, giving up.')
	sys.exit()
if nb_of_elements <= 0 :
	print('Input should be strictly positive, giving up.')
	sys.exit()

seed(arg_for_seed)
L = [randrange(20) for _ in range(nb_of_elements)]
print('\nThe list is:', L)

count = [0] * 4
for i in range(nb_of_elements):
        count[L[i] // 5] += 1
##	if(L[i] < 5):
##		count[0] += 1
##	elif(L[i] < 10):
##		count[1] += 1
##	elif(L[i] < 15):
##		count[2] += 1
##	else:
##		count[3] += 1
for i in range(4):
	if count[i] == 0:
		print('There is no element', end = ' ')
	else : 
		print(f'There is {count[i]} element', end = ' ')
	print(f'between {i*5} and {(i+1)*5-1}.') 
