import os.path

d = {}

if os.path.isfile("score.txt") :
    doc = open("score.txt","r")
    print("old file")
    
else :
    doc = open("score.txt","w")
    doc = open("score.txt","r")
    print("new file")
    
for row in doc.readlines() :
    data = row.split(':')

    key = data[0]
    value = data[1]
    value = value.strip()
    
    d[key] = value
doc.close()

scores = []
names = []
score = 0
n = int(input("請輸入全班學生人數")) #輸入人數
total = 0
high = 0
low = 100
for i in range(n) :
    name = input("請輸入姓名")
    score = int(input("請輸入分數")) #姓名輸入
    d[name] = score
    
    doc = open("score.txt","w")
    for k,v in d.items() :
        doc.write(k)
        doc.write(':')
        doc.write('\n')
    doc.close()
    
    scores.append(score)
    names.append(name)
    if score >= high :
        high = score
        highn = name
    if score <= low :
        low = score
        lown = name
    total += score
total /= n #算出平均
print(" ")
print("全班平均是：" , total , "分") #輸出平均
print(" ")
print("分數最高的人是：", highn , "他" , high , "分") #輸出最高分的人和分數
print(" ")
print("分數最低的人是：", lown , "他" , low , "分") #輸出最低分的人和分數