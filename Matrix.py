n = int(input("Enter the Value of N: "))
temp = n-1
arr = [[n for i in range(2*n-1)] for j in range(2*n-1)]
for i in range(1, n):
    for j in range(i, 2*n-1-i):
        for k in range(i, 2*n-1-i):
            arr[j][k] = temp
    temp -= 1
for i in arr:
    print(i)
