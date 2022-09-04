

coordinates = [
                            # y
                             '|',
                             '|',
                             '|',
    '-', '-', '-', '-', '-', '0', '-' , '-', '-', '-', '-', # x
                             '|',
                             '|',
                             '|',

]

def get_graph(x, y):
    centre_x = int(x / 2)
    centre_y = int(y / 2)
    default_x = x
    grph = []

    for y in range(y):
        grph.append(['.' for i in range(x)])

    grph[centre_y] = ['-' for i in range(x)]

    for i in grph:
        i[centre_x] = '|'

    grph[centre_y][centre_x] = 'O'

    return grph

def func_y(x):
    return x**2

d = {}
for i in range(-5, 6):
    d[i] = round(func_y(i))

print(d)

x = 39
y = 80

r = get_graph(x, y)


centre_x = int(x / 2)
centre_y = int(y / 2)
# {-5: 0, -4: 1, -3: 2, -2: 3, -1: 4, 0: 5, 1: 6, 2: 7, 3: 8, 4: 9, 5: 10}
for k in d:

    r[centre_y - d[k]][centre_x + k] = '#'


for i in r:
    print(i, '\n')

