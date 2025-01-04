import sys
input = sys.stdin.readline


n = int(input())

array = []

for _ in range(n):
  a = int(input())
  if a == 0:
    array = array[:-1]
  else:
    array.append(a)

# print(array)
print(sum(array))

