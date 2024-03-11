for i in range(0,5):
    for j in range(0,5):
        print('*', end=" ")
    print()


print('Siguiente ejercicio')

size = 5
for i in range(size):
    for j in range(size):
        if i == 0 or i == size-1 or j == 0 or j == size-1:
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()

print('Siguiente ejercicio')

for i in range(1, size+1):
    for j in range(1, i+1):
        print('*', end=' ')
    print()

print('Siguiente ejercicio')

for i in range(size):
    for j in range(size - i - 1):
        print('', end=' ')
    for k in range(i +1):
        print('*',end=' ')
    print()
