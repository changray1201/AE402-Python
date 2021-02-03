scores = []
names = []
score = 0
n = int(input("請輸入全班學生人數")) #輸入人數
high = 0
low = 100
global highn,lown,avg
avg = 0
highn = ""
lown = ""

def highscore(scores):
    high = 0
    n = len(scores)
    for i in range(n) :
        if scores[i] >= high :
            high = scores[i]
            highn = names[i]
    person = list()
    person.append(highn)
    person.append(high)
    return person
def lowscore(scores) :
    low = 100
    n = len(scores)
    for i in range(n) :
        if scores[i] <= low :
            low = scores[i]
            lown = names[i]
    person = list()
    person.append(lown)
    person.append(low)
    return person
def average(scores) :
    total = 0
    n = len(scores)
    for i in scores :
        total += i
    average = total / n
    return average

for i in range(n) :
    name = input("輸入名字")
    score = int(input("輸入分數")) #分數輸入
    scores.append(score)
    names.append(name)
    print(scores)
    print(names)


print("全班平均是：" , average(scores)) #算出平均
print(" ")
print("分數最高的人是：", highscore(scores),"分") #輸出最高分的人和分數
print(" ")
print("分數最低的人是：", lowscore(scores) ,"分") #輸出最低分的人和分數