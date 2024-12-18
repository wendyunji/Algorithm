n = int(input())

array = [0]*(n+3)
d = [0]*(n+3)
for i in range(1,n+1):
    array[i] = int(input())

d[1] = array[1]
d[2] = array[1] + array[2]
d[3] = max(array[1]+array[3], array[2]+array[3])


for i in range(4,n+1):
    d[i] = max(d[i-3]+array[i-1]+array[i], d[i-2]+array[i])

print(d[n])
