min_temperature = 0
max_temperature = 100
step = 10

print('Celsius\tFahrenheit')
for celsius in range(min_temperature,max_temperature+step,step):
	fahrenheit = 32 + celsius * 1.8
	print(f'{celsius:7d}\t{fahrenheit:10.0f}')

# range(1,5)  [1,2,3,4] 不包含5
# f‘my name is {name}’  f 很重要 python3.6新用法
# fahrenheit:10.0f   10个字符占位 小数点后保留0位的float