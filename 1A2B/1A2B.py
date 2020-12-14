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
