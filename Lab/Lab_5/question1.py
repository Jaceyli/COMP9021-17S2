import os 
directory = 'name'
for filename in os.listdir(directory):
    if not filename.endswith('.txt'):
        continue
    with open(directory + '/' + filename, 'r', encoding = 'utf-8') as file:
        print('open',filename)
        for line in file:
            line = line.rstrip()
            name, gender, count = line.split()
            print (name,count)
