n = int(input())

d = [0]*91

d[1] = 1
d[2] = 1

for i in range(3, 91):
    d[i] = d[i-1] + d[i-2]

print(d[n])