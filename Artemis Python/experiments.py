n = 7 

for i in range(1, n +1):

    print('1' * i)

for i in range(n - 1,0,-1):

    print('1' * i)
print("novo")

for i in range(1, n + 1):

    for r in range(1, i + 1):
        print(r, end=" ")
    print()
print("fin")
