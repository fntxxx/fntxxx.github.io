import random
items = [i for i in range(0, 10)]   # 將0到9依序放入items
random.shuffle(items)               # 打亂items順序
answer = ""
for i in range(4):                  # 將items前四個數字放入前四個數字放入answer
    answer += str(items[i])
print("正確答案為:", answer)
a = 0                               # a預設為0
b = 0                               # b預設為0
while 1:
    enterNum = input("請輸入您猜的四位數字:")
    if not enterNum.isdigit():      # 若輸入非數字，則要重新輸入
        continue
    if len(enterNum) != 4:          # 若輸入數字不是四個，則要重新輸入
        continue
    if enterNum == answer:          # 若輸入數字與答案一樣，則輸出結果，結束迴圈
        print("恭喜您猜對了!")
        break
    for i in range(4):
        for j in range(4):
            if j == i and enterNum[j] == answer[i]:
                a += 1              # 若數字與位置都正確，則a+1
            elif enterNum[j] == answer[i]:
                b += 1              # 若數字正確、位置不正確，則b+1
    print(a, "A", b, "B")
    a = 0                           # a重置為0
    b = 0                           # b重置為0
