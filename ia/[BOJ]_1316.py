n = int(input())

words = []

for _ in range(n):
    words.append(input())

def group(word):
    alphas = []
    for alpha in word:

        if alpha not in alphas:
            alphas.append(alpha)
        elif alpha == alphas[-1]:
            continue
        else:
            return False
    return True
        
cnt = 0
for word in words:
    if group(word) == True:
        cnt += 1

print(cnt)