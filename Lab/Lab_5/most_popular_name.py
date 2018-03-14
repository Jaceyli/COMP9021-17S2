import os
from collections import defaultdict

male_name = {}  #{name:[freq, year]}
female_name = {}
male_year = {}
female_year = {}

dictionay = 'names'

searchname = input('Enter a first name: ')

# 先把每年名字总数存起来
for filename in os.listdir(dictionay):
    if not filename.endswith('txt'):
        continue
    else:
        with open(dictionay + '/' + filename) as names:
            year = filename[3:7]
            male_total = 0
            female_total = 0
            for line in names:
                line = line.rstrip()
                name, gender, count = line.split(',')
                count = int(count)
                if gender == 'M':
                    male_total += count
                else:
                    female_total += count
            male_year[year] = male_total
            female_year[year] = female_total

for filename in os.listdir(dictionay):
    if not filename.endswith('txt'):
        continue
    else:
        with open(dictionay + '/' + filename) as names:
            year = filename[3:7]
            for line in names:
                line = line.rstrip()
                name, gender, count = line.split(',')
                count = int(count)
                # print(count,'-----')
                if gender == 'M':
                    if name in male_name.keys():
                        if male_name[name][0] < '%.2f' % (count/male_year[year]*100):
                            male_name[name][0] = '%.2f' % (count/male_year[year]*100)
                            male_name[name][1] = year
                    else:
                        male_name[name] = ['%.2f' % (count/male_year[year]*100), year]
                else:
                    if name in female_name.keys():
                        if female_name[name][0] < '%.2f' % (count/female_year[year]*100):
                            female_name[name][0] = '%.2f' % (count/female_year[year]*100)
                            female_name[name][1] = year
                    else:
                        female_name[name] = ['%.2f' % (count/female_year[year]*100), year]



if searchname in female_name.keys():
    freq, year = female_name[searchname]

    print(f'In terms of frequency, {searchname} was the most popular as a female name first in the year {year}.\n'
          f"It then accounted for {freq}% of all female names.")
else:
    print(f'In all years, {searchname} was never given as a female name.')

if searchname in male_name.keys():
    freq,year = male_name[searchname]

    print(f'In terms of frequency, {searchname} was the most popular as a male name first in the year {year}.\n'
          f"It then accounted for {freq}% of all male names.")
else:
    print(f'In all years, {searchname} was never given as a male name.')
