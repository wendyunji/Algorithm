n = int(input())

array = [0]
d = [0]*(n+1)
for _ in range(n):
    array.append(int(input()))

for i in range(0,n+1):
    d[i] = d[i-1] + array[i]

    if d[i-2] > d[i-2]:


print(d)
