from itertools import permutations
from random import shuffle


def scorecalc(guess, chosen):       # 輸入兩組數字，以後者判斷前者為幾A幾B
    a = 0                           # 數字對、位置對，預設為0
    b = 0                           # 數字對、位置錯，預設為0
    for g, c in zip(guess, chosen):
        if g == c:
            a += 1
        elif g in chosen:
            b += 1
    return a, b


digits = '0123456789'               # 答案由哪些數字組成
size = 4                            # 答案是幾個數字
choices = list(permutations(digits, size))  # 全部符合條件的答案
shuffle(choices)                    # 打亂答案的組合
fre = 0                             # 猜的次數
items = [i for i in range(0, 10)]   # 將0到9依序放入items
shuffle(items)                      # 打亂items順序
corAns = ""                         # 正確答案
for i in range(size):               # 將items前size個數字放入corAns
    corAns += str(items[i])
print("正在進行 %i 個數字的 1A2B 遊戲\n" % size)

while True:
    fre += 1
    ans = choices[0]                # 答案組合中的第一個
    print("(還剩下 %i 種組合)" % len(choices))
    enterNum = ''.join(ans)
    score = scorecalc(enterNum, corAns)
    print("第 %i 猜是 %*s， (A, B)： %s"
          % (fre, size, ''.join(ans), score))
    if score == (size, 0):
        print("答得真好!")
        break
    choices = [c for c in choices if scorecalc(c, ans) == score]
    # 符合新條件的答案組合
