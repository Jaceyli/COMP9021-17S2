# Uses data available at http://data.worldbank.org/indicator
# on Forest area (sq. km) and Agricultural land area (sq. km).
# Prompts the user for two distinct years between 1990 and 2004
# as well as for a strictly positive integer N,
# and outputs the top N countries where:
# - agricultural land area has increased from oldest input year to most recent input year;
# - forest area has increased from oldest input year to most recent input year;
# - the ratio of increase in agricultural land area to increase in forest area determines
#   output order.
# Countries are output from those whose ratio is largest to those whose ratio is smallest.
# In the unlikely case where many countries share the same ratio, countries are output in
# lexicographic order.
# In case fewer than N countries are found, only that number of countries is output.


# Written by JINGXUAN LI and Eric Martin for COMP9021


import sys
import os
import csv
from collections import defaultdict

agricultural_land_filename = 'API_AG.LND.AGRI.K2_DS2_en_csv_v2.csv'
if not os.path.exists(agricultural_land_filename):
    print(f'No file named {agricultural_land_filename} in working directory, giving up...')
    sys.exit()
forest_filename = 'API_AG.LND.FRST.K2_DS2_en_csv_v2.csv'
if not os.path.exists(forest_filename):
    print(f'No file named {forest_filename} in working directory, giving up...')
    sys.exit()
try:
    years = {int(year) for year in
                           input('Input two distinct years in the range 1990 -- 2014: ').split('--')
            }
    if len(years) != 2 or any(year < 1990 or year > 2014 for year in years):
        raise ValueError
except ValueError:
    print('Not a valid range of years, giving up...')
    sys.exit()
try:
    top_n = int(input('Input a strictly positive integer: '))
    if top_n < 0:
        raise ValueError
except ValueError:
    print('Not a valid number, giving up...')
    sys.exit()


countries = []
year_1, year_2 = None, None


# Insert your code here
tmp_1 = years.pop()
tmp_2 = years.pop()
if tmp_1 <= tmp_2:
    year_1 = tmp_1
    year_2 = tmp_2
else:
    year_2 = tmp_1
    year_1 = tmp_2
    
agri = defaultdict(list)
forest  = defaultdict(list)
# D['paul'].append(1887)

with open(agricultural_land_filename,encoding='UTF-8') as file:
    readfile = csv.reader(file)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    for line in readfile:
        agri[line[0]] = line[4:]

with open(forest_filename, encoding='UTF-8') as file:
    readfile = csv.reader(file)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    headers = next(readfile)
    for line in readfile:
        forest[line[0]] = line[4:]

result = defaultdict(list)
for e in agri.keys():
    if agri[e][year_2-1960] is not '' and agri[e][year_1-1960] is not '' and forest[e][year_2-1960] is not '' and forest[e][year_1-1960] is not '' \
            and float(forest[e][year_2-1960])-float(forest[e][year_1-1960]) > 0 and float(forest[e][year_2-1960])-float(forest[e][year_1-1960])>0:
            a = (float(agri[e][year_2-1960])-float(agri[e][year_1-1960]))/ (float(forest[e][year_2-1960])-float(forest[e][year_1-1960]))
            if a > 0:
                result[e] = a

result = sorted(result.items(), key=lambda x:x[1], reverse=True)
# print(result)
# countries[:4]

for e in range(top_n):
    countries.append(f"{result[e][0]} ({str('%.2f' % result[e][1])})")

print(f'Here are the top {top_n} countries or categories where, between {year_1} and {year_2},\n'
      '  agricultural land and forest land areas have both strictly increased,\n'
      '  listed from the countries where the ratio of agricultural land area increase\n'
      '  to forest area increase is largest, to those where that ratio is smallest:')
print('\n'.join(country for country in countries))

