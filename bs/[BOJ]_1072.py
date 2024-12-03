x, y = map(int, input().split())

start = 0
end = x     # x가 분자
a = x       # a는 더해지는 수 이걸 x로 세팅 y+x/x+x = 적어도 0.5 이상이니깐 최대치

# 예외 조건
if ((100*y) // x) >= 99:
    print(-1)

else:
    while start <= end:
        mid = (start+end) // 2    # 최대치의 중간에서 시작함 그래서 계속 임계점을 찾아나가는 거임
        if ((100*(y+mid)) // (x+mid)) > ((100*y) // x):
            a = mid               # 근데 완전히 같아질 수는 없으니 큰 값에서 계속 a를 갱신 시켜 나감 그러다 start랑 end가 같아지면 출력
            end = mid - 1
        else:
            start = mid + 1
        print(mid)

    print(a)