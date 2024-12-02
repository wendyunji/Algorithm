# 이게 왜 이진 탐색?

x, y = map(int, input().split())

# 아래의 숫자 보다 큰 숫자 찾기
# a = (x*x) / ((99*x) - (100*y))
r = (x*x) % ((99*x) - (100*y))
z = (x*x) // ((99*x) - (100*y))

if x == y:
    print(-1)
elif r == 0:
    print(z)
else:
    print(z+1)



# k = 2
# print((47+k) / (53+k))