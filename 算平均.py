scores = []
names = []
score = 0
n = int(input("請輸入全班學生人數")) #輸入人數
total = 0
high = 0
low = 100
for i in range(n) :
    score = int(input("請輸入成績")) #成績輸入
    name = input("輸入姓名") #輸入姓名
    scores.append(score)
    names.append(name)
    total += score
    if score >= high :
        high = score
        highn = name
    if score <= low :
        low = score
        lown = name
total /= n #算出平均
print(" ")
print("全班平均是：" , total , "分") #輸出平均
print(" ")
print("分數最高的人是：", highn , "他" , high , "分") #輸出最高分的人和分數
print(" ")
print("分數最低的人是：", lown , "他" , low , "分") #輸出最低分的人和分數