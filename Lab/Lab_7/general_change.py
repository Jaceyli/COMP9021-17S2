import sys
from collections import defaultdict

print("Input pairs of the form 'value : number'\n"
      "   to indicate that you have 'number' many banknotes of face value 'value'.\n"
      "Input these pairs one per line, with a blank line to indicate end of input.\n")

banknotes = {}
while 1:
    line = input()
    if line.rstrip():
        line = line.rstrip().split(':')
        try:
            banknotes[int(line[0])] = int(line[1])
        except ValueError:
            sys.exit()
    else:
        break

# banknotes.sort(key=lambda x: x[0], reverse=True)
print(banknotes)
desired_number = input('Input the desired amount:')
try:
    desired_number = int(desired_number)
except ValueError:
    sys.exit()


# giving up here---------------------
solutions = defaultdict(list)
for i in range(1, desired_number + 1):
    for e in banknotes.keys():
        if i // e == 0:
            solutions[i].append([(e, i // e)])

print(solutions)
if len(solutions) == 0:
    print('\nThere is no solution.')
elif len(solutions) == 1:
    print('\nThere is a unique solution:')
else:
    print(f'\nThere are {len(solutions)} solutions:')