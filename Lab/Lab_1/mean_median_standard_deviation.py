from random import seed, randint
import sys
from math import sqrt
from statistics import mean, median, pstdev


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
L = [randint(-50,50) for _ in range(nb_of_elements)]
print('\nThe list is:', L)

# mean：
my_mean = sum(L)/nb_of_elements
print(f'The mean is {my_mean:.2f}.')	

# median
L.sort()
if nb_of_elements % 2 == 0:
	my_median = (L[int(nb_of_elements/2)] + L[int(nb_of_elements/2)-1] )/2
	print(f'The median is {my_median:.2f}.')
else :
	print(f'The median is {L[nb_of_elements/2+1]:.2f}.')

# standard deviationt
my_deviation = sqrt(sum((x - my_mean) ** 2 for x in L) / nb_of_elements)
print(f'The standard deviation is {my_deviation:.2f}.')


print('Confirming with functions from the statistics module:')
print(f'The mean is {mean(L):.2f}.')
print(f'The median is {median(L):.2f}.')
print(f'The standard deviation is {pstdev(L):.2f}.')