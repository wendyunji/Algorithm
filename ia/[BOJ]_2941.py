arr = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
a = input()
answer = 0

for e in arr:
  while a.find(e)>-1 :
    i = a.find(e)
    a = a[:i]+' '+a[i+len(e):]
    answer += 1

answer += len(a.replace(' ', ''))
    
print(answer)