from random import seed, randint

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
	
if nb_of_elements <= 0:
    print('Input should be strictly positive, giving up.')
    sys.exit()
    
seed(arg_for_seed)

L = [randint(0,99) for e in range(nb_of_elements)]
print('\nThe list is:', L)

max_element, min_element = 0, 100
for x in L:
	if x > max_element:
		max_element = x
	if x < min_element:
		min_element = x

print('\nThe maximum difference between largest and smallest values in this list is:',max_element-min_element)
print('Confirming with builtin operation:', max(L) - min(L))
