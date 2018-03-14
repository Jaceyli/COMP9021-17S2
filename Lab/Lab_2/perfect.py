#question 2

number = input('Input a integer: ')
try:
    number = int(number)
except ValueError:
    print('Incorrect input, giving up.')
    sys.exit()
    
for x in range(1,number + 1):
    L = [e for e in range(1 , x) if x % e == 0]
    if x == sum(L):
        print(f'{x} is a perfect number.')