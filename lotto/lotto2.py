import random
x = random.sample(range(1, 50), 6)  # 隨機產生6個1~49中的號碼放入x[]
x.sort()  # 將x[]中的號碼排序
print("開獎號碼為:", x)
y = random.sample(range(1, 50), 6)  # 隨機產生6個1~49中的號碼放入y[]
y.sort()  # 將y[]中的號碼排序
print("對獎號碼為:", y)
star = 0  # star為中獎的號碼個數，預設為0
for i in range(6):
    if y[i] in x:  # 若對中號碼，則star+1
        star += 1
if star == 6:
    print("恭喜您號碼全中!!!")
else:
    print("您中了", star, "個號碼")
