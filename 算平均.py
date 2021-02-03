scores = []
score = 0
n = int(input("請輸入全班學生人數")) #輸入人數
total = 0
high = 0
low = 100
for i in range(n * 2) :
    score = input("依序輸入姓名和分數") #姓名輸入
    scores.append(score)
    if i % 2 == 1 :
        scores[i] = int(scores[i]) 
        if scores[i] >= high :
            high = scores[i]
            highn = scores[i - 1]
        if scores[i] <= low :
            low = scores[i]
            lown = scores[i - 1]
        total += scores[i]
total /= n #算出平均
print(" ")
print("全班平均是：" , total , "分") #輸出平均
print(" ")
print("分數最高的人是：", highn , "他" , high , "分") #輸出最高分的人和分數
print(" ")
print("分數最低的人是：", lown , "他" , low , "分") #輸出最低分的人和分數