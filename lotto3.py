import random
x = random.sample(range(1, 50), 6)          #隨機產生6個1~49中的號碼放入x[]
x.sort()                                    #將x[]中的號碼排序
print("開獎號碼為:",x)
p=0
while p==0:
    y=list(map(int,input("請輸入對獎號碼，以逗號隔開:").split(',')))
    if len(y)!=len(x):
        print("對獎號碼個數應與開獎號碼個數相同")
        continue
    p=0
    for i in range(len(y)):                 #檢測是否輸入重複的號碼
        for j in range(i):
            if y[j]==y[i]:
                print("請勿輸入重複號碼")
                p=1
                break
        if p==1:
            break
    if p==1:
        p=0
        continue
    star=0
    for i in range(len(x)):
        if y[i] in x:
            star+=1
    if star==len(x):
        print("恭喜您號碼全中!!!")
    else:
        print("您中了",star,"個號碼")