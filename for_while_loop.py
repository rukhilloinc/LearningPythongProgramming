
# while

count = 1
while count < 9:
    print(f'This is # {count} of iteration')
    count +=1


while True:
    print('Running this infinitely')
    break


# For loop
s = 'book'
for i in s:
    print(i)

i = 10
for i in range(10):
    print(i)

# data_list = [{'previous': {'Date': '20210119  13:30:00', 'Open': 3794.0, 'High': 3795.0, 'Low': 3791.5, 'Close': 3793.25, 'Volume': 7615}},
#              {'latest': {'Date': '20210119  13:35:00', 'Open': 3793.25, 'High': 3793.5, 'Low': 3791.5, 'Close': 3791.5, 'Volume': 5553}}]

data_list = ['Book', 'Pen', 'Water', 10, 1.25]
for i in data_list:
    print(i)

d = {'Date': '20210119  13:35:00', 'Open': 3793.25, 'High': 3793.5, 'Low': 3791.5, 'Close': 3791.5, 'Volume': 5553}


for i in d.keys():
    print(i)

for i in d.values():
    print(i)



