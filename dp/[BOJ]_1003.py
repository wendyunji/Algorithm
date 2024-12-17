t = int(input())

d = [0]*41

d[0] = 0
d[1] = 1
d[2] = 1

for n in range(3, 41):
    if d[n] == 0:
        d[n] = d[n-1] + d[n-2]

results_z = []
results_o = []

for _ in range(t):
    n = int(input())
    if n == 0:
        results_z.append(1)
        results_o.append(d[n])
    else:
        results_z.append(d[n-1])
        results_o.append(d[n])

for i in range(t):
    print(results_z[i],results_o[i])