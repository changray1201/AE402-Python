score = input("請輸入成績")
score = int(score)
if score > 100 or score < 0 :
    score = input("請輸入0~100之間的數")
elif score >= 90 :
    print("A")
elif score >= 80 :
    print("B")
elif score >= 70 :
    print("C")
elif score >= 60 :
    print("D")
else :
    print("E")
