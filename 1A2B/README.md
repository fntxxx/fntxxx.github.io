# 1A2B2程式碼－人出題，電腦猜
```
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

print("正在進行 %i 個數字的 1A2B 遊戲\n" % size)

while True:
    fre += 1
    ans = choices[0]                # 答案組合中的第一個
    print("(還剩下 %i 種組合)" % len(choices))
    score = input("第 %i 猜是 %*s， A,B： "
                  % (fre, size, ''.join(ans)))      # EX 1,2
    score = score.strip().split(',')                # EX ['1', '2']
    score = tuple(int(s.strip()) for s in score)    # EX (1,2)
    if score == (size, 0):
        print("答得真好!")
        break
    choices = [c for c in choices if scorecalc(c, ans) == score]
    # 符合新條件的答案組合
    if not choices:
        print("輸入錯誤， 按照以上提示將沒有任何答案")
        break

```
# 1A2B執行圖－電腦出題，人猜
![1A2B程式執行](https://github.com/fntxxx/fntxxx.github.io/blob/master/1A2B/1A2B%E7%A8%8B%E5%BC%8F%E5%9F%B7%E8%A1%8C.jpg)

# 1A2B程式碼－電腦出題，人猜
```
from random import shuffle
items = [i for i in range(0, 10)]   # 將0到9依序放入items
shuffle(items)                      # 打亂items順序
size = 4                            # 答案是幾個數字
corAns = ""                         # 正確答案
for i in range(size):               # 將items前size個數字放入corAns
    corAns += str(items[i])
print("正確答案為:", corAns)
fre = 0                             # 猜的次數，預設為0
while True:
    enterNum = input("請輸入您猜的 %i 位數字:" % size)
    if not enterNum.isdigit():      # 若輸入非數字，則要重新輸入
        print("輸入錯誤")
        continue
    if len(enterNum) != size:       # 若輸入數字個數錯誤，則要重新輸入
        print("輸入錯誤")
        continue
    fre += 1                        # 每猜一次，fre+1
    if enterNum == corAns:          # 若輸入數字與答案一樣，則輸出結果，結束迴圈
        print("猜對了! 您共猜了 %i 次" % fre)
        break
    a = 0                           # 數字對、位置對，預設為0
    b = 0                           # 數字對、位置錯，預設為0
    for e, c in zip(enterNum, corAns):  # 以corAns判斷enterNum為幾A幾B
        if e == c:
            a += 1
        elif e in corAns:
            b += 1
    print("這組數字為: %i A %i B" % (a, b))

```
# 1A2B執行圖－電腦出題，人猜
![1A2B程式執行](https://github.com/fntxxx/fntxxx.github.io/blob/master/1A2B/1A2B%E7%A8%8B%E5%BC%8F%E5%9F%B7%E8%A1%8C.jpg)
