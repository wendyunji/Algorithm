n = int(input())

d = [0] * 19

for i in range(4,n+1):

    d[i] = 5001

    if ((i - 5) == 0) or ((i - 5) == 3):
        d[i] = d[i-5] + 1
    
    if (i-3) == 0:
        d[i] = d[i-3] + 1

    # if i % 3 == 0:
    #     d[i] = min(d[i], d[i//3] + 1)

    # if i % 5 == 0:
    #     d[i] = min(d[i], d[i//5] + 1)

print(d)
print(d[n])

